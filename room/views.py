import datetime

from .models                import Complex, ComplexSpaceInfo, ComplexPriceInfo

from django.views           import View
from django.http            import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models       import Avg

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
