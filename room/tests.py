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
