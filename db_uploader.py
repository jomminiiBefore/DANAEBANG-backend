# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'danaebang.settings')

import django
django.setup()

import csv

from account.models import *
from room.models import *

### Agent
with open('./resource/Agent.csv', mode='r') as agents:
    reader = csv.reader(agents, delimiter=',')

    for agent in list(reader)[1:]:
        Agent.objects.create(
            name=agent[1],
            face_name = agent[2],
            face_number = agent[3],
            business_id = agent[4],
            registration_id = agent[5],
            address = agent[6],
            profile_image_URL = agent[7]
            )

### BelongedAgent
with open('./resource/BelongedAgent.csv', mode='r') as belonged_agents:
    reader = csv.reader(belonged_agents, delimiter=',')

    for agent in list(reader)[1:]:
        BelongedAgent.objects.create(
            name=agent[1],
            phone_number = agent[2],
            agent_id = agent[3],
            )

#   SocialLoginType
with open('./resource/SocialLoginType.csv', mode='r') as social_login_types:
    reader = csv.reader(social_login_types, delimiter=',')

    for type in list(reader)[1:]:
        SocialLoginType.objects.create(
            name=type[1],
            )

##### 단지 ####

### FuelType
with open('./resource/FuelType.csv', mode='r') as fuel_types:
    reader = csv.reader(fuel_types, delimiter=',')

    for type in list(reader)[1:]:
        FuelType.objects.create(name=type[1])

### EntranceType
with open('./resource/EntranceType.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        EntranceType.objects.create(name=type[1])

### HeatType
with open('./resource/HeatType.csv', mode='r') as heat_types:
    reader = csv.reader(heat_types, delimiter=',')

    for type in list(reader)[1:]:
        HeatType.objects.create(name=type[1])

### ComplexType
with open('./resource/ComplexType.csv', mode='r') as complex_types:
    reader = csv.reader(complex_types, delimiter=',')

    for type in list(reader)[1:]:
        ComplexType.objects.create(name=type[1])

### EducationCategory
with open('./resource/EducationCategory.csv', mode='r') as categories:
    reader = csv.reader(categories, delimiter=',')

    for category in list(reader)[1:]:
        EducationCategory.objects.create(name=category[1])

### EducationInfo
with open('./resource/EducationInfo.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for info in list(reader)[1:]:
        EducationInfo.objects.create(
            name                  = info[1],
            longitude             = info[2],
            latitude              = info[3],
            education_category_id = info[4]
            )

### ConvenienceCategory
with open('./resource/ConvenienceCategory.csv', mode='r') as categories:
    reader = csv.reader(categories, delimiter=',')

    for category in list(reader)[1:]:
        ConvenienceCategory.objects.create(name=category[1])

### ConvenienceInfo
with open('./resource/ConvenienceInfo.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for info in list(reader)[1:]:
        ConvenienceInfo.objects.create(
            name=info[1],
            longitude = info[2],
            latitude = info[3],
            convenience_category_id = info[4]
            )

### SafetyCategory
with open('./resource/SafetyCategory.csv', mode='r') as categories:
    reader = csv.reader(categories, delimiter=',')

    for category in list(reader)[1:]:
        SafetyCategory.objects.create(name=category[1])

### SafetyInfo
with open('./resource/SafetyInfo.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for info in list(reader)[1:]:
        SafetyInfo.objects.create(
            name=info[1],
            longitude = info[2],
            latitude = info[3],
            safety_category_id = info[4]
            )

### Complex_price_info / Complex /
with open('./resource/Complex.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for infos in list(reader)[1:]:
        info = []
        for element in infos:
            if element == "":
                element = None
            info.append(element)

        price = ComplexPriceInfo.objects.create(
            trade_average_pyeong_price = info[18],
            lease_average_pyeong_price = info[19],
            trade_region_average_pyeong_price = info[20],
            lease_region_average_pyeong_price = info[21]
        )
        Complex.objects.create(
            name = info[1],
            address = info[2],
            enter_date = info[3],
            household_num = info[4],
            building_num = info[5],
            parking_average = info[6],
            build_cov_ratio = info[7],
            floor_area_index = info[8],
            lowest_floor = info[9],
            highest_floor = info[10],
            provider_name = info[11],
            jibun_address = info[12],
            road_address = info[13],
            complex_type_id = info[14],
            heat_type_id = info[15],
            fuel_type_id = info[16],
            entrance_type_id = info[17],
            longitude = info[22],
            latitude = info[23],
            complex_price_info = price
        )

### ComplexImage
with open('./resource/ComplexImage.csv', mode='r') as images:
    reader = csv.reader(images, delimiter=',')

    for image in list(reader)[1:]:
        ComplexImage.objects.create(
            image_url = image[1],
            complex_id = image[2]
        )

### ComplexSpaceInfo
with open('./resource/ComplexSpaceInfo.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for infos in list(reader)[1:]:
        info = []
        for element in infos:
            if element == "":
                element = None
            info.append(element)
        ComplexSpaceInfo.objects.create(
            pyeong_type              = info[1],
            room_size                = info[2],
            provision_size           = info[3],
            contract_size            = info[4],
            maintenance_price        = info[5],
            beds_num                 = info[6],
            bath_num                 = info[7],
            complex_id               = info[8],
            entrance_type_id         = info[9],
            lay_out_image_URL        = info[10],
            extend_lay_out_image_URL = info[11]
        )

# 유저 정보 생기면 실행
# # ComplexLike
# with open('./resource/ComplexLike.csv', mode='r') as likes:
#     reader = csv.reader(likes, delimiter=',')

#     for like in list(reader)[1:]:
#         ComplexLike.objects.create(
#             user_id    = like[1],
#             complex_id = like[2]
#         )

###### 방 #####

### TradeType
with open('./resource/TradeType.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        TradeType.objects.create(
            name = type[1]
        )

### TradeHistory
with open('./resource/TradeHistory.csv', mode='r') as histories:
    reader = csv.reader(histories, delimiter=',')

    for infos in list(reader)[1:]:
        history = []
        for element in infos:
            if element == "":
                element = None
            history.append(element)
        TradeHistory.objects.create(
            trade_type_id         = history[1],
            complex_space_info_id = history[2],
            date                  = history[3],
            deposit               = history[4],
            price                 = history[5],
            floor                 = history[6]
        )

### RoomType
with open('./resource/RoomType.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        RoomType.objects.create(
            name = type[1]
        )

### RoomSubType
with open('./resource/RoomSubType.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        RoomSubType.objects.create(
            name = type[1]
        )

### BuildingUse
with open('./resource/BuildingUse.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        BuildingUse.objects.create(
            name = type[1]
        )

# RoomAddInfo
with open('./resource/RoomAddInfo.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for infos in list(reader)[1:]:
        info = []
        for element in infos:
            if element == "":
                element = None
            info.append(element)
        RoomAddInfo.objects.create(
            is_builtin         = info[1],
            is_elevator        = info[2],
            is_pet             = info[3],
            is_balcony         = info[4],
            is_loan            = info[5],
            is_parking         = info[6],
            parking_fee        = info[7]
        )

### Floor
with open('./resource/Floor.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        Floor.objects.create(
            name = type[1]
        )

### MovingDateType
with open('./resource/MovingDateType.csv', mode='r') as types:
    reader = csv.reader(types, delimiter=',')

    for type in list(reader)[1:]:
        MovingDateType.objects.create(
            name = type[1]
        )

### Score
with open('./resource/Score.csv', mode='r') as scores:
    reader = csv.reader(scores, delimiter=',')

    for infos in list(reader)[1:]:
        score = []
        for element in infos:
            if element == "":
                element = 0
            score.append(element)
        Score.objects.create(
            price       = score[1],
            option      = score[2],
            near        = score[3],
            maintenance = score[4],
            traffic     = score[5]
        )

### Room
with open('./resource/Room.csv', mode='r') as rooms:
    reader = csv.reader(rooms, delimiter=',')

    for infos in list(reader)[1:]:
        room = []
        for element in infos:
            if element == "":
                element = None
            room.append(element)
        Room.objects.create(
            is_quick              = room[1],
            is_confirmed          = room[2],
            confirmed_date        = room[3],
            is_agent              = room[4],
            is_short_lease        = room[5],
            title                 = room[6],
            description           = room[7],
            room_size             = room[8],
            provision_size        = room[9],
            contract_size         = room[10],
            room_floor_id         = room[11],
            building_floor_id     = room[12],
            is_maintenance_nego   = room[13],
            maintenance_price     = room[14],
            longitude             = room[15],
            latitude              = room[16],
            address               = room[17],
            heat_type_id          = room[18],
            moving_date_type_id   = room[19],
            moving_date           = room[20],
            building_use_id       = room[21],
            room_type_id          = room[22],
            room_sub_type_id      = room[23],
            score_id              = room[24],
            complex_id            = room[25],
            complex_space_info_id = room[26],
            room_add_info_id      = room[27],
            agent_id              = room[28],
            belonged_agent_id     = room[29],
        )

### RoomImage
with open('./resource/RoomImage.csv', mode='r') as images:
    reader = csv.reader(images, delimiter=',')

    for image in list(reader)[1:]:
        RoomImage.objects.create(
            image_url = image[1],
            room_id = image[2]
        )

# 유저 정보 생기면 실행
# # RoomLike
# with open('./resource/RoomLike.csv', mode='r') as likes:
#     reader = csv.reader(likes, delimiter=',')

#     for like in list(reader)[1:]:
#         RoomLike.objects.create(
#             user_id = like[1],
#             room_id = like[2]
#         )

### TradeInfo(전세 매매 거래정보)
with open('./resource/TradeInfoAll.csv', mode='r') as infos:
    reader = csv.reader(infos, delimiter=',')

    for info in list(reader)[1:]:
        TradeInfo.objects.create(
            deposit        = info[1],
            fee            = info[2],
            room_id        = info[3],
            trade_type_id  = info[4],
        )

#### TradeInfo(전세 매매 거래정보)
#with open('./resource/TradeInfo.csv', mode='r') as infos:
#    reader = csv.reader(infos, delimiter=',')
#
#    for info in list(reader)[1:]:
#        TradeInfo.objects.create(
#            deposit        = info[1],
#            trade_type_id  = info[2],
#            room_id        = info[3]
#        )
#
#### MonthlyTradeInfo(월세 거래정보)
#with open('./resource/MonthlyTradeInfo.csv', mode='r') as infos:
#    reader = csv.reader(infos, delimiter=',')
#
#    for info in list(reader)[1:]:
#        MonthlyTradeInfo.objects.create(
#            deposit        = info[1],
#            fee            = info[2],
#            room_id        = info[3]
#        )
