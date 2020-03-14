import json

from .models     import (
    Complex,
    ComplexImage,
    ComplexPriceInfo,
    ComplexSpaceInfo,
    ComplexType,
    EntranceType,
    HeatType,
    FuelType,
    TradeHistory,
    TradeType
    ConvenienceCategory,
    ConvenienceInfo,
    SafetyCategory,
    SafetyInfo,
    EducationCategory,
    EducationInfo
)

from django.test import TestCase, Client

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
        print(response.json())
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
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json(),{})

    def test_near_info_TypeError(self):
        client   = Client()
        response = client.get('/room/near?latitude=ff&longitude=127.052472')
        self.assertEqual(response.status_code, 400)
