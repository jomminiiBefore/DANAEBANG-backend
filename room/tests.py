import json
import jwt

from my_settings      import SECRET
from account.models   import User
from .models          import *

from django.db.models import Q
from django.test      import TestCase, Client

class DetailTest(TestCase):
    maxDiff = None
    def setUp(self):
        ComplexType.objects.create(
            id = 1,
            name = '오피스텔'
        )
        EntranceType.objects.create(
            id = 1,
            name = '계단식'
        )
        HeatType.objects.create(
            id = 3,
            name = '중앙난방'
        )
        FuelType.objects.create(
            id = 1,
            name = '도시가스'
        )
        price_info = ComplexPriceInfo.objects.create(
            trade_average_pyeong_price        = None,
            lease_average_pyeong_price        = None,
            trade_region_average_pyeong_price = 964,
            lease_region_average_pyeong_price = 928,
        )
        complex = Complex.objects.create(
            id                 = 5,
            complex_type_id    = 1,
            address            = "서울특별시 동대문구 휘경동",
            name               = "휘경코업레지던스",
            enter_date         = "2002.12 준공",
            household_num      = 132,
            parking_average    = "0.3",
            building_num       = 1,
            heat_type_id       = 3,
            fuel_type_id       = 1,
            provider_name      = '대성산업',
            lowest_floor       = 9,
            highest_floor      = 9,
            entrance_type_id   = 1,
            build_cov_ratio    = "360.0",
            floor_area_index   = "53.0",
            complex_price_info = price_info
        )
        image_urls= [
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
        ]
        for image in image_urls:
            ComplexImage.objects.create(
                image_url = image,
                complex   = complex
            )
        ComplexSpaceInfo.objects.create(
            complex                 = complex,
            id                      = 260,
            pyeong_type             = "22",
            room_size               = "13.86",
            provision_size          = None,
            contract_size           = "22.03",
            maintenance_price       = None,
            beds_num                = 1,
            bath_num                = 1,
            entrance_type_id        = 1,
            lay_out_image_URL       = None,
            extend_lay_out_image_URL= None
        )
        ComplexSpaceInfo.objects.create(
            complex                 = complex,
            id                      = 543,
            pyeong_type             = "22",
            room_size               = "13.86",
            provision_size          = None,
            contract_size           = "22.03",
            maintenance_price       = None,
            beds_num                = 1,
            bath_num                = 1,
            entrance_type_id        = 1,
            lay_out_image_URL       = None,
            extend_lay_out_image_URL= None
        )
        ComplexSpaceInfo.objects.create(
            complex                 = complex,
            id                      = 1030,
            pyeong_type             = "22",
            room_size               = "13.86",
            provision_size          = None,
            contract_size           = "22.03",
            maintenance_price       = None,
            beds_num                = 1,
            bath_num                = 1,
            entrance_type_id        = 1,
            lay_out_image_URL       = None,
            extend_lay_out_image_URL= None
        )
        ComplexSpaceInfo.objects.create(
            complex                 = complex,
            id                      = 1834,
            pyeong_type             = "22",
            room_size               = "13.86",
            provision_size          = None,
            contract_size           = "22.03",
            maintenance_price       = None,
            beds_num                = 1,
            bath_num                = 1,
            entrance_type_id        = 1,
            lay_out_image_URL       = None,
            extend_lay_out_image_URL= None
        )

    def test_complex_detail_success(self):
        client   = Client()
        response = client.get('/room/detail?type=complex&id=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                            "complex_detail": {
                                "complex_id": "5",
                                "complex_type": "오피스텔",
                                "address": "서울특별시 동대문구 휘경동",
                                "name": "휘경코업레지던스",
                                "enter_date": "2002.12 준공",
                                "household_num": 132,
                                "parking_average": "0.3",
                                "building_num": 1,
                                "heat_type": "중앙난방",
                                "fuel_type": "도시가스",
                                "provider_name": "대성산업",
                                "lowest_floor": 9,
                                "highest_floor": 9,
                                "entrance_type": "계단식",
                                "build_cov_ratio": "360.0",
                                "floor_area_index": "53.0",
                                "image_urls": [
                                    "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
                                ],
                                "trade_average_pyeong_price": None,
                                "lease_average_pyeong_price": None,
                                "trade_region_average_pyeong_price": 964,
                                "lease_region_average_pyeong_price": 928,
                                "pyeong_infos": [
                                    {
                                        "complex_space_info_id": 260,
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "complex_space_info_id": 543,
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "complex_space_info_id": 1030,
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "complex_space_info_id": 1834,
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    }
                                ]
                            }
                            }
                        )
    def test_complex_detail_wrong_result(self):
        client   = Client()
        response = client.get('/room/detail?type=complex&id=5')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),
                         {
                            "complex_detail": {
                                "complex_id": "6",
                                "complex_type": "오피스텔",
                                "address": "서울특별시 동대문구 휘경동",
                                "name": "휘경코업레지던스",
                                "enter_date": "2002.12 준공",
                                "household_num": 132,
                                "parking_average": "0.3",
                                "building_num": 1,
                                "heat_type": "중앙난방",
                                "lowest_floor": 9,
                                "highest_floor": 9,
                                "entrance_type": "계단식",
                                "build_cov_ratio": "360.0",
                                "floor_area_index": "53.0",
                                "image_urls": [
                                    "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
                                ],
                                "trade_average_pyeong_price": None,
                                "lease_average_pyeong_price": None,
                                "trade_region_average_pyeong_price": 964,
                                "lease_region_average_pyeong_price": 928,
                                "pyeong_infos": [
                                    {
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    },
                                    {
                                        "pyeong_type": "22",
                                        "room_size": "13.86",
                                        "provision_size": None,
                                        "contract_size": "22.03",
                                        "maintenance_price": None,
                                        "beds_num": 1,
                                        "bath_num": 1,
                                        "entrance_type": "계단식",
                                        "lay_out_image_URL": None,
                                        "extend_lay_out_image_URL": None
                                    }
                                ]
                            }
                            }
                        )

    def test_complex_detail_invalid_complex_id(self):
        client   = Client()
        response = client.get('/room/detail?type=complex&id=5000')
        self.assertEqual(response.status_code, 400)

class TradeHistoryTest(TestCase):
    maxDiff = None
    def setUp(self):
        ComplexType.objects.create(
            id = 1,
            name = '오피스텔'
        )
        EntranceType.objects.create(
            id = 1,
            name = '계단식'
        )
        HeatType.objects.create(
            id = 3,
            name = '중앙난방'
        )
        TradeType.objects.create(
            id = 1,
            name = '월세'
        )
        TradeType.objects.create(
            id = 2,
            name = '전세'
        )
        price_info = ComplexPriceInfo.objects.create(
            trade_average_pyeong_price        = None,
            lease_average_pyeong_price        = None,
            trade_region_average_pyeong_price = 964,
            lease_region_average_pyeong_price = 928,
        )
        complex = Complex.objects.create(
            id                 = 5,
            complex_type_id    = 1,
            address            = "서울특별시 동대문구 휘경동",
            name               = "휘경코업레지던스",
            enter_date         = "2002.12 준공",
            household_num      = 132,
            parking_average    = "0.3",
            building_num       = 1,
            heat_type_id       = 3,
            lowest_floor       = 9,
            highest_floor      = 9,
            entrance_type_id   = 1,
            build_cov_ratio    = "360.0",
            floor_area_index   = "53.0",
            complex_price_info = price_info
        )
        image_urls= [
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
        ]
        for image in image_urls:
            ComplexImage.objects.create(
                image_url = image,
                complex   = complex
            )
        SpaceInfo = ComplexSpaceInfo.objects.create(
            complex                 = complex,
            id                      = 260,
            pyeong_type             = "22",
            room_size               = "13.86",
            provision_size          = None,
            contract_size           = "22.03",
            maintenance_price       = None,
            beds_num                = 1,
            bath_num                = 1,
            entrance_type_id        = 1,
            lay_out_image_URL       = None,
            extend_lay_out_image_URL= None
        )
        TradeHistory.objects.create(
            trade_type_id      = 1,
            complex_space_info = SpaceInfo,
            date               = '201901',
            deposit            = 1000,
            price              = 50,
            floor              = 15
        )
        TradeHistory.objects.create(
            trade_type_id      = 1,
            complex_space_info = SpaceInfo,
            date               = '201901',
            deposit            = 1000,
            price              = 40,
            floor              = 15
        )
        TradeHistory.objects.create(
            trade_type_id      = 2,
            complex_space_info = SpaceInfo,
            date               = '201903',
            deposit            = 10000,
            price              = None,
            floor              = 15
        )
    
    def test_trade_history_success(self):
        client   = Client()
        response = client.get('/room/trade-history?id=260')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             "result": {
                                 "rent_history": [
                                     {
                                         "date": "201901",
                                         "rent_count": 2,
                                         "histories": [
                                             {
                                                 "type": "월세",
                                                 "date": "201901",
                                                 "deposit": 1000,
                                                 "price": 50,
                                                 "floor": 15
                                                 },
                                             {
                                                 "type": "월세",
                                                 "date": "201901",
                                                 "deposit": 1000,
                                                 "price": 40,
                                                 "floor": 15
                                             }
                                         ]
                                     }],
                                 "lease_history": [
                                     {
                                         "date": "201903",
                                         "lease_count": 1,
                                         "average_deposit": 10000,
                                         "histories": [
                                             {
                                                 "type": "전세",
                                                 "date": "201903",
                                                 "deposit": 10000,
                                                 "floor": 15
                                             }
                                             ]
                                         }
                                     ],
                                 'selling_history': []
                                 }
                             }
                         )

    def test_trade_history_wrong_result(self):
        client   = Client()
        response = client.get('/room/trade-history?id=260')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),
                         {
                             "result":{}
                         })

    def test_trade_history_invalid_complexspaceinfo_id(self):
        client   = Client()
        response = client.get('/room/trade-history?id=200060')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message":"INVALID_COMPLEXSPACEINFO_ID"})

class NearInfosTest(TestCase):
    maxDiff = None
    def setUp(self):
        ConvenienceCategory.objects.bulk_create([
            ConvenienceCategory(id = 1, name = '지하철역'),
            ConvenienceCategory(id = 2, name = '편의점'),
            ConvenienceCategory(id = 4, name = '은행'),
            ConvenienceCategory(id = 6, name = '마트'),
            ConvenienceCategory(id = 7, name = '약국')
        ])
        SafetyCategory.objects.bulk_create([
            SafetyCategory(id = 1, name = '치안'),
            SafetyCategory(id = 2, name = 'cctv')
        ])
        EducationCategory.objects.bulk_create([
            EducationCategory(id = 1, name = '어린이집'),
            EducationCategory(id = 2, name = '유치원' ),
            EducationCategory(id = 3, name = '초등학교'),
            EducationCategory(id = 4, name = '중학교'),
            EducationCategory(id = 5, name = '고등학교')
        ])
        ConvenienceInfo.objects.bulk_create([
            ConvenienceInfo(
                name = '역삼역 2호선',
                latitude = 37.50067442,
                longitude = 127.0364695,
                convenience_category_id = 1
            ),
            ConvenienceInfo(
                name = 'CU 삼성현대점',
                latitude = 37.5172997,
                longitude = 127.0468571,
                convenience_category_id = 2
            ),
            ConvenienceInfo(
                name = '한국씨티은행 역삼동지점',
                latitude = 37.49954779,
                longitude = 127.0315111,
                convenience_category_id = 4
            ),
            ConvenienceInfo(
                name = '이마트 역삼점',
                latitude = 37.49930421,
                longitude = 127.0483974,
                convenience_category_id = 6
            ),
            ConvenienceInfo(
                name = '강남동물약국',
                latitude = 37.49479508,
                longitude = 127.0400762,
                convenience_category_id = 7
            )
        ])

        SafetyInfo.objects.bulk_create([
            SafetyInfo(
                name = '논현2파출소',
                latitude = 37.52108842,
                longitude = 127.0532259,
                safety_category_id = 1
            ),
            SafetyInfo(
                name = '생활방법',
                latitude =  37.4925545,
                longitude =  127.0372172,
                safety_category_id = 2
            )
        ])

        EducationInfo.objects.bulk_create([
            EducationInfo(
                name = '신한마리오어린이집',
                latitude = 37.50067442,
                longitude = 127.0364695,
                education_category_id = 1
            ),
            EducationInfo(
                name = '선경유치원',
                latitude = 37.5172997,
                longitude = 127.0468571,
                education_category_id = 2
            ),
            EducationInfo(
                name = '서울대도초등학교',
                latitude = 37.49954779,
                longitude = 127.0315111,
                education_category_id = 3
            ),
            EducationInfo(
                name = '언주중학교',
                latitude = 37.49930421,
                longitude = 127.0483974,
                education_category_id = 4
            ),
            EducationInfo(
                name = '경기고등학교',
                latitude = 37.49479508,
                longitude = 127.0400762,
                education_category_id = 5
            )
        ])
    def tearDown(self):
        ConvenienceCategory.objects.all().delete()
        ConvenienceInfo.objects.all().delete()
        SafetyCategory.objects.all().delete()
        SafetyInfo.objects.all().delete()
        EducationCategory.objects.all().delete()
        EducationInfo.objects.all().delete()

    def test_near_info_success(self):
        client = Client()
        response = client.get('/room/near?latitude=37.505776&longitude=127.052472')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             'results':{
                                 'convenience': {
                                     'subway': [{
                                         'name': '역삼역 2호선',
                                         'position': [
                                             '37.500674420000003', '127.036469499999995'
                                         ]}],
                                     'convenient_store': [{
                                         'name': 'CU 삼성현대점',
                                         'position': [
                                             '37.517299700000002', '127.046857099999997'
                                         ]}],
                                     'bank': [{
                                         'name': '한국씨티은행 역삼동지점',
                                         'position': [
                                             '37.499547790000001', '127.031511100000003'
                                         ]}],
                                     'mart': [{
                                         'name': '이마트 역삼점',
                                         'position': [
                                             '37.499304209999998', '127.048397399999999'
                                         ]}],
                                     'pharmacy': [{
                                         'name': '강남동물약국',
                                         'position': [
                                             '37.494795080000003', '127.040076200000001'
                                         ]}]},
                                 'safety': {
                                     'police': [{
                                         'name': '논현2파출소',
                                         'position': [
                                             '37.521088419999998', '127.053225900000001'
                                         ]}],
                                     'cctv': [
                                     ]},
                                 'education': {
                                     'nursery_school': [{
                                         'name': '신한마리오어린이집',
                                         'position': [
                                             '37.500674420000003', '127.036469499999995'
                                         ]}],
                                     'kinder_school': [{
                                         'name': '선경유치원',
                                         'position': [
                                             '37.517299700000002', '127.046857099999997'
                                         ]}],
                                     'elementary_school': [{
                                         'name': '서울대도초등학교',
                                         'position': [
                                             '37.499547790000001', '127.031511100000003'
                                         ]}],
                                     'middle_school': [{
                                         'name': '언주중학교',
                                         'position': [
                                             '37.499304209999998', '127.048397399999999'
                                         ]}],
                                     'high_school': [{
                                         'name': '경기고등학교',
                                         'position': [
                                             '37.494795080000003', '127.040076200000001'
                                         ]}]
                                 }}})

    def test_near_info_fail(self):
        client = Client()
        response = client.get('/room/near?latitude=37.505776&longitude=127.052472')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),{})

    def test_near_info_TypeError(self):
        client   = Client()
        response = client.get('/room/near?latitude=ff&longitude=127.052472')
        self.assertEqual(response.status_code, 400)

class RoomUploadTest(TestCase):
    def setUp(self):
        User.objects.create(
            name         = 'hyun',
            email        = 'hyun@email.com',
            phone_number = '010-0000-0000', 
        ) 
        RoomType.objects.create(name = '원룸')
        HeatType.objects.create(name = '열병합')
        TradeType.objects.create(name = '전세')
        Floor.objects.create(name = '1층')
        MovingDateType.objects.create(name = '즉시입주')

    def tearDown(self):
        User.objects.all().delete()
        RoomType.objects.all().delete()
        HeatType.objects.all().delete()
        TradeType.objects.all().delete()
        Floor.objects.all().delete()
        MovingDateType.objects.all().delete()

    def test_upload_success(self):
        room = {
            "is_builtin"          : 0,
            "is_elevator"         : 0,
            "is_pet"              : 0,
            "is_balcony"          : 0,
            "is_loan"             : 0,
            "is_parking"          : 0,
            "address"             : "서울시",
            "longitude"           : 1.1,
            "latitude"            : 1.1,
            "is_short_lease"      : 0,
            "room_size"           : 1.1,
            "provision_size"      : 1.1,
            "room_floor_id"       : Floor.objects.get(name = '1층').id,
            "building_floor_id"   : Floor.objects.get(name = '1층').id,
            "heat_type_id"        : HeatType.objects.get(name = '열병합').id,
            "moving_date_type_id" : MovingDateType.objects.get(name = '즉시입주').id,
            "title"               : "title",
            "description"         : "description",
            "image_url"           : "url",
            "trade_info"          : [
                {"deposit":100000, "trade_type_id":TradeType.objects.get(name = '전세').id}
            ],
            "is_maintenance_nego" : 0,
            "room_type_id"        : RoomType.objects.get(name = '원룸').id

        }
        user = {
          'email': 'hyun@email.com'
        }

        client   = Client()
        user     = User.objects.get(email = user['email'])
        token    = jwt.encode({'user_id': user.id}, SECRET['secret'], algorithm = SECRET['algorithm']).decode()
        headers  = {'HTTP_token':token} 
        response = client.post('/room/upload', json.dumps(room), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)

    def test_upload_invalid_key(self):
        room = {
            "is_builtin_test"     : 0,
            "is_elevator"         : 0,
            "is_pet"              : 0,
            "is_balcony"          : 0,
            "is_loan"             : 0,
            "is_parking"          : 0,
            "address"             : "서울시",
            "longitude"           : 1.1,
            "latitude"            : 1.1,
            "is_short_lease"      : 0,
            "room_size"           : 1.1,
            "provision_size"      : 1.1,
            "room_floor_id"       : Floor.objects.get(name = '1층').id,
            "building_floor_id"   : Floor.objects.get(name = '1층').id,
            "heat_type_id"        : HeatType.objects.get(name = '열병합').id,
            "moving_date_type_id" : MovingDateType.objects.get(name = '즉시입주').id,
            "title"               : "title",
            "description"         : "description",
            "image_url"           : "url",
            "trade_info"          : [
                {"deposit":100000, "trade_type_id":TradeType.objects.get(name = '전세').id}
            ],
            "is_maintenance_nego" : 0,
            "room_type_id"        : RoomType.objects.get(name = '원룸').id
            
        }
        user = {
          'email': 'hyun@email.com'
        }

        client   = Client()
        user     = User.objects.get(email = user['email'])
        token    = jwt.encode({'user_id': user.id}, SECRET['secret'], algorithm = SECRET['algorithm']).decode()
        headers  = {'HTTP_token':token} 
        response = client.post('/room/upload', json.dumps(room), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 400)

class RoomListTest(TestCase):
    maxDiff = None
    def setUp(self):
        roomtype = RoomType.objects.create(
            id = 1,
            name = '원룸'
        )

        tradetype = TradeType.objects.create(
            id = 1,
            name = '월세'
        )
        floor = Floor.objects.create(
            name = '1층'
        )
        room = Room.objects.create(
            id = 321,
            room_size = 33,
            title = '비싼 집',
            maintenance_price = 10,
            latitude = 37.50 ,
            longitude = 127.04,
            address = '서울시 강남구 역삼동' ,
            room_floor = floor,
            room_type = roomtype 
        )
        image_urls= [
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
        ]
        for image in image_urls:
            RoomImage.objects.create(
                image_url = image,
                room      = room
            )
        TradeInfo.objects.create(
            room = room,
            deposit = 500,
            fee     = 40,
            trade_type = tradetype,
            id = 1
        )

    def test_room_list_success(self):
        client   = Client()
        response = client.get('/room/list?latitude=37.505776&longitude=127.052472&zoom=1&offset=1&limit=24&multi_room_type=1&selling_type=1&room_size=0&room_size=50&maintenance_price=0&maintenance_price=10&deposit_range=0&deposit_range=30000&fee_range=0&fee_range=200')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             "results":[
                                 {
                                     "room_id" : 321,
                                     "is_quick" : False,
                                     "is_confirmed" : False,
                                     "confirmed_date" : None,
                                     "title" : "비싼 집",
                                     "image_url" :
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png",
                                     "room_type_str" : "원룸",
                                     "floor_str" : "1층",
                                     "room_size" : "33.00",
                                     "latitude" : 37.5,
                                     "longitude" : 127.04,
                                     "maintenance_price" : 10,
                                     "trade_type_str" : "월세",
                                     "trade_deposit" : 500,
                                     "trade_fee" : 40
                                 },
                                 {'room_count': 1},
                             ]
                         }
                        )

    def test_room_list_invalid_query_parameter(self):
        client   = Client()
        response = client.get('/room/list?latitude=37.505776&longitude=127.052472&zoom=1&offset=1&limit=24&multi_room_type=1&selling_type=1&room_size=0&room_size=50&maintenance_price=0&maintenance_price=10&deposit_range=0&deposit_range=30000&fee_range=0')
        self.assertEqual(response.json(), {"message":"INVALID_QUERY_PARAMETERS"})
        self.assertEqual(response.status_code, 400)

class ClustRoomListTest(TestCase):
    maxDiff = None
    def setUp(self):
        roomtype = RoomType.objects.create(
            id = 1,
            name = '원룸'
        )

        tradetype = TradeType.objects.create(
            id = 1,
            name = '월세'
        )
        floor = Floor.objects.create(
            name = '1층'
        )
        room = Room.objects.create(
            id = 321,
            room_size = 33,
            title = '비싼 집',
            maintenance_price = 10,
            latitude = 37.50 ,
            longitude = 127.04,
            address = '서울시 강남구 역삼동' ,
            room_floor = floor,
            room_type = roomtype 
        )
        image_urls= [
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png"
        ]
        for image in image_urls:
            RoomImage.objects.create(
                image_url = image,
                room      = room
            )
        TradeInfo.objects.create(
            room = room,
            deposit = 500,
            fee     = 40,
            trade_type = tradetype,
            id = 1
        )

    def test_find_room_success(self):
        client   = Client()
        response = client.get('/room/cluster?offset=1&limit=24&room_id=321')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {
                             "results":[
                                 {
                                     "room_id" : 321,
                                     "is_quick" : False,
                                     "is_confirmed" : False,
                                     "confirmed_date" : None,
                                     "title" : "비싼 집",
                                     "image_url" :
            "https://d2o59jgeq8ig2.cloudfront.net/complex/default/complex_default_detail2.png",
                                     "room_type_str" : "원룸",
                                     "floor_str" : "1층",
                                     "room_size" : "33.00",
                                     "latitude" : 37.5,
                                     "longitude" : 127.04,
                                     "maintenance_price" : 10,
                                     "trade_type_str" : "월세",
                                     "trade_deposit" : 500,
                                     "trade_fee" : 40
                                 },
                                 {'room_count': 1},
                             ]
                         }
                        )

    def test_cluster_room_list_invalid_query_parameter(self):
        client   = Client()
        response = client.get('/room/cluster?limit=24')
        self.assertEqual(response.json(), {"message":"INVALID_QUERY_PARAMETERS"})
        self.assertEqual(response.status_code, 400)
