import csv
import json
import requests

limit = 9500 

#단지 기본정보
complex_info_results =[
    {
        'complex_id' : 'complex_id',
        'complex_longitude' : 'complex_longitude',
        'complex_latitude' : 'complex_latitude',
    }
]
#        'complex_name' : 'complex_name',
#        'fuel_type' : 'fuel_type',
#        'heat_type' : 'heat_type',
#        'entrance_type' : 'entrace_type',
#        'address' : 'address',
#        'enter_date' : 'enter_date',
#        'household_num' : 'household_num',
#        'building_num' : 'building_num',
#        'parking_average' : 'parking_average',
#        'build_cov_ratio' : 'build_cov_ratio',
#        'floor_area_index' : 'floor_area_index',
#        'lowest_floor' : 'lowest_floor',
#        'highest_floor' : 'highest_floor',
#        'provider_name' : 'provider_name',
#        'jibun_address' : 'jibun_address',
#        'road_address' : 'road_address',
#        'complex_type' : 'complex_type',
#        'trade_average_pyeong_price' : 'trade_average_pyeong_price',
#        'lease_average_pyeong_price' : 'lease_average_pyeong_price',
#        'trade_region_average_pyeong_price' : 'trade_region_average_pyeong_price',
#        'lease_region_average_pyeong_price' : 'lease_region_average_pyeong_price',
#        }
#    ]
#
#image_results = [
#    {
#        'complex_id' : 'complex_id',
#        'image_url' : 'image_url'
#    }
#]
#
#space_results = [
#    {
#        'complex_id' : 'complex_id',
#        'space_seq' : 'space_seq',
#        'pyeong_type' : 'pyeong_type',
#        'exclusive_space' : 'exclusive_space',
#        'supply_space' : 'supply_space',
#        'contract_space' : 'contract_space',
#        'layout_image' : 'layout_image',
#        'extend_layout_image' : 'extend_layout_image',
#        'maintenance_price' : 'maintenance_price',
#        'beds_num' : 'beds_num',
#        'bath_num' : 'bath_num',
#        'entrance_type' : 'entrance_type'
#    }
#]

with open('./results/02_room_info_lists.csv', mode = 'r') as room_info_lists:
    reader = csv.reader(room_info_lists, delimiter = ',')

    for room in list(reader)[1:limit]:
        complex_url = room[31]

        req = requests.get(f'https://www.dabangapp.com/api/3/complex/detail2?api_version=3.0.1&call_type=web&complex_id={complex_url}')
        data = req.json()
        comp = data.get('complex')
        if comp:
            spaces = data['spaces']
            complex_dict = {
                'complex_id' : complex_url,
                'complex_longitude' : comp['location'][0],
                'complex_latitude' : comp['location'][1],
            }
#                'complex_name' : comp['complex_name'],
#                'fuel_type' : comp['fuel_type_str'],
#                'heat_type' : comp['heat_type_str'],
#                'entrance_type' : comp['entrance_type_str'],
#                'address' : comp['address'],
#                'enter_date' : comp['enter_date_str'],
#                'household_num' : comp['household_num'],
#                'building_num' : comp['building_num'],
#                'parking_average' : comp['parking_average'],
#                'build_cov_ratio' : comp['build_cov_ratio'],
#                'floor_area_index' : comp['floor_area_index'],
#                'lowest_floor' : comp['complex_lowest_floor'],
#                'highest_floor' : comp['complex_highest_floor'],
#                'provider_name' : comp['provider_name'],
#                'jibun_address' : comp['jibun_address'],
#                'road_address' : comp['road_address'],
#                'complex_type' : comp['complex_type_str'],
#                'trade_average_pyeong_price' : comp['trade_average_pyeong_price'],
#                'lease_average_pyeong_price' : comp['lease_average_pyeong_price'],
#                'trade_region_average_pyeong_price' : comp['trade_region_average_pyeong_price'],
#                'lease_region_average_pyeong_price' : comp['lease_region_average_pyeong_price'],
#            }
            complex_info_results.append(complex_dict)

#            for image in comp['images']:
#                image_info = {
#                    'complex_id' : complex_url,
#                    'image_url' : image['image']
#                }
#                image_results.append(image_info)
#
#            for space in spaces:
#                space_info = {
#                    'complex_id'          : complex_url,
#                    'space_seq'           : space['space_seq'],
#                    'pyeong_type'         : space['pyeong_type'],
#                    'exclusive_space'     : space['exclusive_space'],
#                    'supply_space'        : space['supply_space'],
#                    'contract_space'      : space['contract_space'],
#                    'layout_image'        : space['layout_image'],
#                    'extend_layout_image' : space['extend_layout_image'],
#                    'maintenance_price'   : space['maintenance_total_price'],
#                    'beds_num'            : space['beds_num'],
#                    'bath_num'            : space['bath_num'],
#                    'entrance_type'       : space['entrance_type_str']
#                    }
#                space_results.append(space_info)

with open('./results/03_01_complex_location.csv', mode = 'w') as complex_info_lists:
    complex_writer = csv.writer(complex_info_lists)

    for complex in complex_info_results:
        complex_writer.writerow(
            [
                complex['complex_id'],
                complex['complex_longitude'],
                complex['complex_latitude'],
#                complex['complex_name'],
#                complex['fuel_type'],
#                complex['heat_type'],
#                complex['entrance_type'],
#                complex['address'],
#                complex['enter_date'],
#                complex['household_num'],
#                complex['building_num'],
#                complex['parking_average'],
#                complex['build_cov_ratio'],
#                complex['floor_area_index'],
#                complex['lowest_floor'],
#                complex['highest_floor'],
#                complex['provider_name'],
#                complex['jibun_address'],
#                complex['road_address'],
#                complex['complex_type'],
#                complex['trade_average_pyeong_price'],
#                complex['lease_average_pyeong_price'],
#                complex['trade_region_average_pyeong_price'],
#                complex['lease_region_average_pyeong_price'],
            ]
        )

#with open('./results/03_complex_image_lists.csv', mode = 'w') as complex_image_lists:
#    image_writer = csv.writer(complex_image_lists)
#
#    for image in image_results:
#        image_writer.writerow(
#            [
#                image['complex_id'],
#                image['image_url']
#            ]
#        )
#
#with open('./results/03_complex_space_lists.csv', mode = 'w') as space_lists:
#    space_writer = csv.writer(space_lists)
#
#    for space in space_results:
#        space_writer.writerow(
#            [
#                space['complex_id'],
#                space['space_seq'],
#                space['pyeong_type'],
#                space['exclusive_space'],
#                space['supply_space'],
#                space['contract_space'],
#                space['layout_image'],
#                space['extend_layout_image'],
#                space['maintenance_price'],
#                space['beds_num'],
#                space['bath_num'],
#                space['entrance_type']
#            ]
#        )
#
## 위치 및 주변시설
## 학군
#nursery_dict    = {}
#kinder_dict     = {}
#elementary_dict = {}
#middle_dict     = {}
#high_dict      = {}
#
#with open('./results/02_room_info_lists.csv', mode = 'r') as room_info_lists:
#    reader = csv.reader(room_info_lists, delimiter = ',')
#
#    for room in list(reader)[1:limit]:
#        complex_url = room[31]
#
#        req = requests.get(f'https://www.dabangapp.com/api/3/complex/near?api_version=3.0.1&call_type=web&complex_id={complex_url}')
#        data = req.json()
#        education = data.get('education')
#        if education:
#            for nursery in education[0]['pois']:
#                nursery_dict[nursery['name']] = nursery['location']
#
#            for kinder in education[1]['pois']:
#                kinder_dict[kinder['name']] = kinder['location']
#
#            for elementary in education[2]['pois']:
#                elementary_dict[elementary['name']] = elementary['location']
#
#            for middle in education[3]['pois']:
#                middle_dict[middle['name']] = middle['location']
#
#            for high in education[4]['pois']:
#                high_dict[high['name']] = high['location']
#
#with open('./results/03_education_nursery_lists.csv', mode = 'w') as nursery_lists:
#    nursery_writer = csv.writer(nursery_lists)
#
#    for key, value in nursery_dict.items():
#        nursery_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_education_kinder_lists.csv', mode = 'w') as kinder_lists:
#    kinder_writer = csv.writer(kinder_lists)
#
#    for key, value in kinder_dict.items():
#        kinder_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_education_elemantary_lists.csv', mode = 'w') as elementary_lists:
#    elementary_writer = csv.writer(elementary_lists)
#
#    for key, value in elementary_dict.items():
#        elementary_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_education_middle_lists.csv', mode = 'w') as middle_lists:
#    middle_writer = csv.writer(middle_lists)
#
#    for key, value in middle_dict.items():
#        middle_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_education_high_lists.csv', mode = 'w') as high_lists:
#    high_writer = csv.writer(high_lists)
#
#    for key, value in high_dict.items():
#        high_writer.writerow([key, value[0], value[1]])
#
## 편의시설 
#subway_dict     = {}
#mart_dict       = {}
#convenient_dict = {}
#bank_dict       = {}
#pharmacy_dict   = {}
#
#with open('./results/02_room_info_lists.csv', mode = 'r') as room_info_lists:
#    reader = csv.reader(room_info_lists, delimiter = ',')
#
#    for room in list(reader)[1:limit]:
#        complex_url = room[31]
#
#        req = requests.get(f'https://www.dabangapp.com/api/3/complex/near?api_version=3.0.1&call_type=web&complex_id={complex_url}')
#        data = req.json()
#        convenience = data.get('convenience')
#        if convenience:
#            for subway in convenience[0]['pois']:
#                subway_dict[subway['name']] = subway['location']
#
#            for mart in convenience[1]['pois']:
#                mart_dict[mart['name']] = mart['location']
#
#            for convenient in convenience[2]['pois']:
#                convenient_dict[convenient['name']] = convenient['location']
#
#            for bank in convenience[3]['pois']:
#                bank_dict[bank['name']] = bank['location']
#
#            for pharmacy in convenience[4]['pois']:
#                pharmacy_dict[pharmacy['name']] = pharmacy['location']
#
#
#with open('./results/03_convenience_subway_lists.csv', mode = 'w') as subway_lists:
#    subway_writer = csv.writer(subway_lists)
#
#    for key, value in subway_dict.items():
#        subway_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_convenience_mart_lists.csv', mode = 'w') as mart_lists:
#    mart_writer = csv.writer(mart_lists)
#
#    for key, value in mart_dict.items():
#        mart_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_convenience_convenient_lists.csv', mode = 'w') as convenient_lists:
#    convenient_writer = csv.writer(convenient_lists)
#
#    for key, value in convenient_dict.items():
#        convenient_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_convenience_bank.csv', mode = 'w') as bank_lists:
#    bank_writer = csv.writer(bank_lists)
#
#    for key, value in bank_dict.items():
#        bank_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_convenience_pharmacy_lists.csv', mode = 'w') as pharmacy_lists:
#    pharmacy_writer = csv.writer(pharmacy_lists)
#
#    for key, value in pharmacy_dict.items():
#        pharmacy_writer.writerow([key, value[0], value[1]])
#
## 안전시설 
#police_dict = {}
#cctv_dict = {}
#
#with open('./results/02_room_info_lists.csv', mode = 'r') as room_info_lists:
#    reader = csv.reader(room_info_lists, delimiter = ',')
#
#    for room in list(reader)[1:limit]:
#        complex_url = room[31]
#
#        req = requests.get(f'https://www.dabangapp.com/api/3/complex/near?api_version=3.0.1&call_type=web&complex_id={complex_url}')
#        data = req.json()
#        safety = data.get('safety')
#        if safety:
#            if len(safety[0]['pois']) != 0:
#                   for police in safety[0]['pois']:
#                       police_dict[police['gubun']] = police['location']
#
#            if len(safety[1]['pois']) != 0:
#                   for cctv in safety[1]['pois']:
#                       cctv_dict[cctv['location'][0]] = [cctv['usage'], cctv['location']]
#
#with open('./results/03_safety_police_lists.csv', mode = 'w') as police_lists:
#    police_writer = csv.writer(police_lists)
#
#    for key, value in police_dict.items():
#        police_writer.writerow([key, value[0], value[1]])
#
#with open('./results/03_safety_cctv_lists.csv', mode = 'w') as cctv_lists:
#    cctv_writer = csv.writer(cctv_lists)
#
#    for value in cctv_dict.values():
#        cctv_writer.writerow([value[0], value[1][0], value[1][1]])
#
# 실거래 히스토리 
trade_lists = [{
    'complex_id'  : 'complex_id',
    'trade_type'  : 'trade_type',
    'pyeong_type' : 'pyeong_type',
    'date'        : 'date',
    'deposit'     : 'deposit',
    'price'       : 'price',
    'floor'       : 'floor'
    }]

with open('./results/03_complex_space_lists.csv', mode = 'r') as space_lists:
    reader = csv.reader(space_lists, delimiter = ',')

    for space in list(reader)[1:limit]:
        complex_url = space[0]
        space_seq   = space[1]

        req = requests.get(f'https://www.dabangapp.com/api/3/complex/space/real-price-info?api_version=3.0.1&call_type=web&complex_id={complex_url}&space_seq={space_seq}')
        data = req.json()
        trades = data.get('trade_history')
        if trades:
            for trade in trades:
                if trade:
                    if trade['history']:
                        for history in trade['history']['histories']:
                            trade_dict = {
                                'complex_id'  : complex_url,
                                'trade_type'  : history['type'],
                                'pyeong_type' : space[2],
                                'date'        : history['date'],
                                'deposit'     : history['deposit'],
                                'price'       : history['price'],
                                'floor'       : history['floor']
                                }
                        trade_lists.append(trade_dict)

        leases = data.get('lease_history')
        if leases:
            for lease in leases:
                if lease:
                    if lease['history']:
                        for history in lease['history']['histories']:
                            lease_dict = {
                                'complex_id'  : complex_url,
                                'trade_type'  : history['type'],
                                'pyeong_type' : space[2],
                                'date'        :  history['date'],
                                'deposit'     :  history['deposit'],
                                'price'       :  history['price'],
                                'floor'       :  history['floor']
                            }
                        trade_lists.append(lease_dict)

with open('./results/03_real_trade_lists.csv', mode = 'w') as trade_list:
    trade_writer = csv.writer(trade_list)

    for trade in trade_lists:
        print(trade)
        trade_writer.writerow(
            [
                trade['complex_id'],
                trade['trade_type'],
                trade['pyeong_type'],
                trade['date'],
                trade['deposit'],
                trade['price'],
                trade['floor']
            ]
        )
