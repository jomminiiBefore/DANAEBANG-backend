import json
import datetime
from haversine              import haversine

from account.my_utils       import requirelogin
from .models                import *

from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models       import Avg
from django.db.models       import Q

class DetailView(View):
    def get(self, request):
        try:
            type = request.GET.get('type', None)
            id   = request.GET.get('id', None)
            if type == 'complex':
                complex = Complex.objects.select_related('complex_price_info').get(id = id)
                complex_detail = {
                    'complex_id'                        : id,
                    'complex_type'                      : complex.complex_type.name,
                    'address'                           : complex.address,
                    'name'                              : complex.name,
                    'enter_date'                        : complex.enter_date,
                    'household_num'                     : complex.household_num,
                    'parking_average'                   : complex.parking_average,
                    'building_num'                      : complex.building_num,
                    'heat_type'                         : complex.heat_type.name,
                    'fuel_type'                         : complex.fuel_type.name,
                    'provider_name'                     : complex.provider_name,
                    'lowest_floor'                      : complex.lowest_floor,
                    'highest_floor'                     : complex.highest_floor,
                    'entrance_type'                     : complex.entrance_type.name,
                    'build_cov_ratio'                   : complex.build_cov_ratio,
                    'floor_area_index'                  : complex.floor_area_index,
                    'image_urls'                        : [image.image_url for image in complex.compleximage_set.all()],
                    'trade_average_pyeong_price'        : (complex.complex_price_info.trade_average_pyeong_price),
                    'lease_average_pyeong_price'        : complex.complex_price_info.lease_average_pyeong_price,
                    'trade_region_average_pyeong_price' : complex.complex_price_info.trade_region_average_pyeong_price,
                    'lease_region_average_pyeong_price' : complex.complex_price_info.lease_region_average_pyeong_price,
                    'pyeong_infos' :[{
                        'complex_space_info_id'    : pyeong.id,
                        'pyeong_type'              : pyeong.pyeong_type,
                        'room_size'                : pyeong.room_size,
                        'provision_size'           : pyeong.provision_size,
                        'contract_size'            : pyeong.contract_size,
                        'maintenance_price'        : pyeong.maintenance_price,
                        'beds_num'                 : pyeong.beds_num,
                        'bath_num'                 : pyeong.bath_num,
                        'entrance_type'            : pyeong.entrance_type.name,
                        'lay_out_image_URL'        : pyeong.lay_out_image_URL,
                        'extend_lay_out_image_URL' : pyeong.extend_lay_out_image_URL
                        } for pyeong in complex.complexspaceinfo_set.all()]
                    }
                return JsonResponse({"complex_detail": complex_detail}, status = 200)
            else:
                pass
        except Complex.DoesNotExist:
            return JsonResponse({"message": "INVALID_COMPLEX_ID"}, status = 400)

class TradeHistoryView(View):
    def get(self, request):
        try:
            id                = request.GET.get('id', None)
            now               = datetime.datetime.now().strftime('%Y%m')
            three_year_before = f'{int(now[:4])-3}{now[4:]}'
            pyeong            = (
                ComplexSpaceInfo
                .objects
                .prefetch_related('tradehistory_set')
                .get(id = id)
            )

            rent_month            = [date_dict['date'] for date_dict in pyeong.tradehistory_set
                                     .filter(date__gte = three_year_before, trade_type_id = 1)
                                     .values('date').distinct()]
            monthly_rent_lists    = [pyeong
                                     .tradehistory_set
                                     .filter(date = date, trade_type_id = 1)
                                     .all() for date in rent_month]

            lease_month           = [date_dict['date'] for date_dict in pyeong.tradehistory_set
                                     .filter(date__gte = three_year_before, trade_type_id = 2)
                                     .values('date').distinct()]
            monthly_lease_lists   = [pyeong
                                     .tradehistory_set
                                     .filter(date = date, trade_type_id = 2)
                                     .all() for date in lease_month]

            selling_month         = [date_dict['date'] for date_dict in pyeong.tradehistory_set
                                     .filter(date__gte = three_year_before, trade_type_id = 3)
                                     .values('date').distinct()]
            monthly_selling_lists = [pyeong
                                     .tradehistory_set
                                     .filter(date = date, trade_type_id = 3)
                                     .all() for date in selling_month]

            results = {
                'rent_history' : [{
                    'date'            : monthly_rent[0].date,
                    'rent_count'      : monthly_rent.count(),
                    'histories'       : [{
                        'type'    : rent.trade_type.name,
                        'date'    : rent.date,
                        'deposit' : rent.deposit,
                        'price'   : rent.price,
                        'floor'   : rent.floor
                        } for rent in monthly_rent]
                    } for monthly_rent in monthly_rent_lists],
                'lease_history' : [{
                    'date'            : monthly_lease[0].date,
                    'lease_count'     : monthly_lease.count() ,
                    'average_deposit' : int(monthly_lease.aggregate(Avg('deposit'))['deposit__avg']),
                    'histories'       : [{
                        'type'    : lease.trade_type.name,
                        'date'    : lease.date,
                        'deposit' : lease.deposit,
                        'floor'   : lease.floor
                        } for lease in monthly_lease]
                    } for monthly_lease in monthly_lease_lists],
                'selling_history' : [{
                    'date'            : monthly_selling[0].date,
                    'selling_count'   : monthly_selling.count(),
                    'average_deposit' : int(monthly_selling.aggregate(Avg('deposit'))['deposit__avg']),
                    'histories'       : [{
                        'type'    : selling.trade_type.name,
                        'date'    : selling.date,
                        'deposit' : selling.deposit,
                        'floor'   : selling.floor
                        } for selling in monthly_selling]
                    } for monthly_selling in monthly_selling_lists]
                }
            return JsonResponse({"result":results}, status = 200)
        except ComplexSpaceInfo.DoesNotExist:
            return JsonResponse({"message":"INVALID_COMPLEXSPACEINFO_ID"}, status = 400)

class NearInfoView(View):
    def get(self, request):
        try:
            longitude = float(request.GET.get('longitude', None))
            latitude  = float(request.GET.get('latitude', None))
            position  = (latitude,longitude)
            condition = (
                Q(latitude__range  = (latitude - 0.01, latitude + 0.01)) |
                Q(longitude__range = (longitude - 0.015, longitude + 0.015))
            )

            convenience_infos = (
                ConvenienceInfo
                .objects
                .filter(condition)
                .all()
            )
            near_convenience_infos = [info for info in convenience_infos
                                      if haversine(position, (info.latitude, info.longitude)) <= 2]

            safety_infos = (
                SafetyInfo
                .objects
                .filter(condition)
                .all()
            )
            near_safety_infos = [info for info in safety_infos
                                 if haversine(position, (info.latitude, info.longitude)) <= 2]

            education_infos = (
                EducationInfo
                .objects
                .filter(condition)
                .all()
            )
            near_education_infos = [info for info in education_infos
                                    if haversine(position, (info.latitude, info.longitude)) <= 2]

            results = {
                "convenience" : {
                    "subway" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_convenience_infos
                        if info.convenience_category_id == 1],
                    "convenient_store" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_convenience_infos
                        if info.convenience_category_id == 2],
                    "bank" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_convenience_infos
                        if info.convenience_category_id == 4],
                    "mart" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_convenience_infos
                        if info.convenience_category_id == 6],
                    "pharmacy" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_convenience_infos
                        if info.convenience_category_id == 7]
                    },
                "safety" : {
                    "police" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_safety_infos
                        if info.safety_category_id == 1],
                    "cctv" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_safety_infos
                        if info.safety_category_id == 2]
                    },
                "education" : {
                    "nursery_school" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_education_infos
                        if info.education_category_id == 1],
                    "kinder_school" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_education_infos
                        if info.education_category_id == 2],
                    "elementary_school" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_education_infos
                        if info.education_category_id == 3],
                    "middle_school" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_education_infos
                        if info.education_category_id == 4],
                    "high_school" : [{
                        "name" : info.name,
                        "position" : (info.latitude, info.longitude)
                        } for info in near_education_infos
                        if info.education_category_id == 5]
                    }
            }
            return JsonResponse({"results":results}, status = 200)
        except ValueError:
            return JsonResponse({"message":"INVALID_POSITION"}, status = 400)

class RoomUploadView(View):
    def get(self, request):
        room_info = {
            'room_type'        : list(RoomType.objects.values('name')),
            'trade_type'       : list(TradeType.objects.values('name')),
            'floor'            : list(Floor.objects.values('name')),
            'heat_type'        : list(HeatType.objects.values('name')),
            'moving_date_type' : list(MovingDateType.objects.values('name')),
            'room_sub_type'    : list(RoomSubType.objects.values('name'))
        }
        return JsonResponse(room_info, status = 200)
        
    @requirelogin
    def post(self, request):
        data = json.loads(request.body)
        
        try:
            fee_list      = data.get('fee_list')
            deposit_list  = data.get('deposit_list')
            room_add_info = RoomAddInfo.objects.create(
                is_builtin  = data['is_builtin'],
                is_elevator = data['is_elevator'],
                is_pet      = data['is_pet'],
                is_balcony  = data['is_balcony'],
                is_loan     = data['is_loan'],
                is_parking  = data['is_parking'],
                parking_fee = data.get('parking_fee')
            )

            room = Room.objects.create(
                room_type_id        = data['room_type_id'],
                address             = data['address'],
                longitude           = data['longitude'],
                latitude            = data['latitude'],
                is_short_lease      = data.get('is_short_lease'),
                room_size           = data['room_size'],
                provision_size      = data.get('provision_size'),
                room_floor_id       = data.get('room_floor_id'),
                building_floor_id   = data.get('building_floor_id'),
                heat_type_id        = data.get('heat_type_id'),
                moving_date_type_id = data.get('moving_date_type_id'),
                moving_date         = data.get('moving_date'),
                room_add_info_id    = room_add_info.id,
                title               = data['title'],
                description         = data['description'],
                user_id             = request.user.id,
                is_maintenance_nego = data['is_maintenance_nego'],
                maintenance_price   = data.get('maintenance_price')
            ) 

            RoomImage.objects.create(
                image_url = data['image_url'],
                room_id   = room.id
            )

            if fee_list:
                for fee in fee_list:
                    MonthlyTradeInfo.objects.create(
                        deposit = fee['deposit'],
                        fee     = fee['fee'],
                        room_id = room.id
                    )
            
            if deposit_list:
                for deposit in deposit_list:
                    TradeInfo.objects.create(
                        deposit       = deposit['deposit'],
                        trade_type_id = data.get('trade_type_id'),
                        room_id       = room.id
                    )
              
            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)
