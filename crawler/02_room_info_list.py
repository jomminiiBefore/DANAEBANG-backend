import csv
import json
import requests

room_info_results = [{
    'room_id':'room_id',
    'is_quick' : 'is_quick',
    'trade_type' : 'trade_type',
    'room_type' : 'room_type',
    'room_sub_type_duplex' : 'room_sub_type_duplex',
    'room_sub_type_division' : 'room_sub_type_division',
    'is_confirmed' : 'is_confirmed',
    'confirmed_date' : 'confirmed_date',
    'title' : 'title',
    'description' : 'description',
    'room_size' : 'room_size',
    'provision_size' : 'provision_size',
    'contract_size' : 'contract_size',
    'room_floor' : 'room_floor',
    'building_floor' : 'building_floor',
    'maintenance_cost' : 'maintenance_cost',
    'is_maintenance_nego' : 'is_maintenance_nego',
    'longitude' : 'longitude',
    'latitude' : 'latitude',
    'address' : 'address',
    'heat_type' : 'heat_type',
    'moving_date' : 'moving_date',
    'building_use' : 'building_use',
    'is_built_in' : 'is_built_in',
    'is_elevator' : 'is_elevator',
    'is_pet' : 'is_pet',
    'is_balcony' : 'is_balcony',
    'is_loan' : 'is_loan',
    'is_parking' : 'is_parking',
    'parking_fee' : 'parking_fee',
    'trade_info_deposit' : 'trade_info_deposit',
    'is_short_lease' : 'is_short_lease',
    'trade_infos' : 'trade_infos',
    'image_urls' : 'image_urls',
    'score' : 'score',
    'complex_id' : 'complex_id',
    'pyeong_type' : 'pyeong_type'
}]

image_results = [
    {
        'room_id' : 'room_id',
        'image_url' : 'image_url'
    }
]

trade_info_results = [
    {
        'room_id' : 'room_id',
        'deposit' : 'deposit',
        'fee' : 'fee',
        'trade_type' : 'trade_type'
    }
]

score_results = [
    {
        'room_id' : 'room_id',
        'price' : 'price',
        'options' : 'options',
        'near' : 'near',
        'maintenance' : 'maintenance',
        'traffic' : 'traffic'
    }
]

with open('./results/01_room_lists.csv', mode = 'r') as room_lists:
    reader = csv.reader(room_lists, delimiter = ',')

    for rooom in list(reader)[1:9500]:
        room_id  = rooom[0]
        is_quick = rooom[2]

        req = requests.get(f'https://www.dabangapp.com/api/3/room/detail?api_version=3.0.1&call_type=web&room_id={room_id}')
        data = req.json()
        room = data.get('room')
        if room:
            room_dict = {
                'room_id' : room_id,
                'is_quick' : is_quick,
                'trade_type' : room['price_info'][0][2],
                'room_type' : room['room_type'],
                'room_sub_type_duplex' : room['duplex'],
                'room_sub_type_division' : room['division'],
                'is_confirmed' : room['is_confirm'],
                'confirmed_date' : room['confirm_date_str'],
                'title' : room['title'],
                'description' : room['memo'],
                'room_size' : room['room_size'],
                'provision_size' : room['provision_size'],
                'contract_size' : room['contract_size'],
                'room_floor' : room['room_floor_str'],
                'building_floor' : room['building_floor_str'],
                'maintenance_cost' : room['maintenance_cost_str'],
                'is_maintenance_nego' : room['maintenance_option'],
                'longitude' : room['location'][0],
                'latitude' : room['location'][1],
                'address'  : room['address'],
                'heat_type' : room['heating'],
                'moving_date' : room['moving_date'],
                'building_use' : room['building_use'],
                'is_built_in' : room['built_in_str'],
                'is_elevator' : room['elevator_str'],
                'is_pet' : room['animal_str'],
                'is_balcony' : room['balcony_str'],
                'is_loan' : room['loan_str'],
                'is_parking' : room['parking_str'],
                'parking_fee' : room['parking_str'],
                'trade_info_deposit' : room['price_info'][0][0],
                'is_short_lease' : room['short_lease_str'],
            }

            if data.get('complex'):
                comp = data['complex']
                room_dict['complex_id'] = comp['complex_id']
            
            if data.get('space'):
                space = data['space']
                room_dict['pyeong_type'] = space['pyeong_type']

            room_info_results.append(room_dict)

# room score
            if data.get('score'):
                score = data['score']['room']

                score_info = {
                    'room_id' : room_id,
                    'price' : score['price'],
                    'options' : score['options'],
                    'near' : score['near'],
                    'maintenance' : score['maintenance'],
                    'traffic' : score['traffic']} 
                score_results.append(score_info)

# image_url
            for image in room['photos']:
                image_info = {
                    'room_id' : room_id,
                    'image_url' : 'https://d1774jszgerdmk.cloudfront.net/1024/' + image
                }
                image_results.append(image_info)

# trade_info
            for trade in room['price_info']:
                trade_info = {
                    'room_id' : room_id,
                    'deposit' : trade[0] ,
                    'fee'     : trade[1],
                    'trade_type' :trade[2]
                }
                trade_info_results.append(trade_info)

with open('./results/02_room_info_lists.csv', mode = 'w') as room_info_lists:
    room_writer = csv.writer(room_info_lists)

    for room in room_info_results:
        room_writer.writerow(
            [
                room['room_id'],
                room['is_quick'],
                room['trade_type'],
                room['room_type'],
                room['room_sub_type_duplex'],
                room['room_sub_type_division'],
                room['is_confirmed'],
                room['confirmed_date'],
                room['title'],
                room['description'],
                room['room_size'],
                room['provision_size'],
                room['contract_size'],
                room['room_floor'],
                room['building_floor'],
                room['maintenance_cost'],
                room['is_maintenance_nego'],
                room['longitude'],
                room['latitude'],
                room['address'],
                room['heat_type'],
                room['moving_date'],
                room['building_use'],
                room['is_built_in'],
                room['is_elevator'],
                room['is_pet'],
                room['is_balcony'],
                room['is_loan'],
                room['is_parking'],
                room['parking_fee'],
                room['trade_info_deposit'],
                room['is_short_lease'],
                room.get('complex_id'),
                room.get('pyeong_type')
            ]
        )

with open('./results/02_room_image_lists.csv', mode = 'w') as image_lists:
    image_writer = csv.writer(image_lists)

    for image in image_results:
        image_writer.writerow(
            [
                image['room_id'],
                image['image_url']
            ]
        )

with open('./results/02_room_score_lists.csv', mode = 'w') as score_lists:
    score_writer = csv.writer(score_lists)

    for score in score_results:
        score_writer.writerow(
            [
                score['room_id'],
                score['price'],
                score['options'],
                score['near'],
                score['maintenance'],
                score['traffic']
            ]
        )

with open('./results/02_room_trade_lists.csv', mode = 'w') as trade_lists:
    trade_writer = csv.writer(trade_lists)

    for trade in trade_info_results:
        trade_writer.writerow(
            [
                trade['room_id'],
                trade['deposit'],
                trade['fee'],
                trade['trade_type']
            ]
        )
