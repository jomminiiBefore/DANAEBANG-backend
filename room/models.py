from account.models import User, Agent, BelongedAgent

from django.db import models

class FuelType(models.Model):
    name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'fuel_types'

class EntranceType(models.Model):
    name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'entrance_types'

class HeatType(models.Model):
    name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'heat_types'

class ComplexType(models.Model):
    name = models.CharField(max_length = 10)

    class Meta:
        db_table = 'complex_types'

class ComplexPriceInfo(models.Model):
    trade_average_pyeong_price        = models.IntegerField(null = True)
    lease_average_pyeong_price        = models.IntegerField(null = True)
    trade_region_average_pyeong_price = models.IntegerField(null = True)
    lease_region_average_pyeong_price = models.IntegerField(null = True)

    class Meta:
        db_table = 'complex_price_infos'

class Complex(models.Model):
    name               = models.CharField(max_length = 45)
    address            = models.CharField(max_length = 45)
    enter_date         = models.CharField(max_length = 45, null = True)
    household_num      = models.IntegerField(null = True)
    building_num       = models.IntegerField(null = True)
    parking_average    = models.DecimalField(max_digits = 3, decimal_places = 1, null = True)
    build_cov_ratio    = models.DecimalField(max_digits = 5, decimal_places = 1, null = True)
    floor_area_index   = models.DecimalField(max_digits = 5, decimal_places = 1, null = True)
    lowest_floor       = models.IntegerField(null = True)
    highest_floor      = models.IntegerField(null = True)
    provider_name      = models.CharField(max_length = 45)
    jibun_address      = models.CharField(max_length = 45, null = True)
    road_address       = models.CharField(max_length = 45, null = True)
    complex_type       = models.ForeignKey(ComplexType, on_delete = models.SET_NULL, null = True)
    heat_type          = models.ForeignKey(HeatType, on_delete = models.SET_NULL, null = True)
    fuel_type          = models.ForeignKey(FuelType, on_delete = models.SET_NULL, null = True)
    entrance_type      = models.ForeignKey(EntranceType, on_delete = models.SET_NULL, null = True)
    complex_price_info = models.ForeignKey(ComplexPriceInfo, on_delete = models.SET_NULL, null = True)
    complex_like       = models.ManyToManyField(User, through = 'ComplexLike')

    class Meta:
        db_table = 'complexes'

class ComplexImage(models.Model):
    image_url           = models.URLField(max_length = 2000)
    complex                = models.ForeignKey(Complex, on_delete = models.CASCADE)

    class Meta:
        db_table = 'complex_images'

class ComplexSpaceInfo(models.Model):
    pyeong_type       = models.CharField(max_length = 10)
    room_size         = models.DecimalField(max_digits = 6, decimal_places = 2)
    provision_size    = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    contract_size     = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    maintenance_price = models.IntegerField(null = True)
    beds_num          = models.IntegerField(null = True)
    bath_num          = models.IntegerField(null = True)
    complex           = models.ForeignKey(Complex, on_delete = models.CASCADE)
    entrance_type     = models.ForeignKey(EntranceType, on_delete = models.SET_NULL, null = True)
    lay_out_image_URL = models.URLField(max_length = 2000, null = True)
    extend_lay_out_image_URL = models.URLField(max_length = 2000, null = True)

    class Meta:
        db_table = 'complex_space_infos'

class ComplexLike(models.Model):
    user              = models.ForeignKey(User, on_delete = models.CASCADE)
    complex           = models.ForeignKey(Complex, on_delete = models.CASCADE)

    class Meta:
        db_table = 'complex_likes'

class EducationCategory(models.Model):
    name              = models.CharField(max_length = 5)

    class Meta:
        db_table = 'education_categories'

class EducationInfo(models.Model):
    name               = models.CharField(max_length = 45)
    longitude          = models.DecimalField(max_digits = 20, decimal_places = 15)
    latitude           = models.DecimalField(max_digits = 20, decimal_places = 15)
    education_category = models.ForeignKey(EducationCategory, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'education_infos'

class ConvenienceCategory(models.Model):
    name              = models.CharField(max_length = 5)

    class Meta:
        db_table = 'convenience_categories'

class ConvenienceInfo(models.Model):
    name                 = models.CharField(max_length = 45)
    longitude            = models.DecimalField(max_digits = 20, decimal_places = 15)
    latitude             = models.DecimalField(max_digits = 20, decimal_places = 15)
    convenience_category = models.ForeignKey(ConvenienceCategory, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'convenience_infos'

class SafetyCategory(models.Model):
    name              = models.CharField(max_length = 5)

    class Meta:
        db_table = 'safety_categories'

class SafetyInfo(models.Model):
    name            = models.CharField(max_length = 45)
    longitude       = models.DecimalField(max_digits = 20, decimal_places = 15)
    latitude        = models.DecimalField(max_digits = 20, decimal_places = 15)
    safety_category = models.ForeignKey(SafetyCategory, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'safety_infos'

class TradeType(models.Model):
    name              = models.CharField(max_length = 5)

    class Meta:
        db_table = 'trade_types'

class TradeHistory(models.Model):
    trade_type         = models.ForeignKey(TradeType, on_delete = models.SET_NULL, null = True)
    complex_space_info = models.ForeignKey(ComplexSpaceInfo, on_delete = models.CASCADE)
    date               = models.CharField(max_length = 10)
    deposit            = models.IntegerField(null = True)
    price              = models.IntegerField(null = True)
    floor              = models.IntegerField()

    class Meta:
        db_table = 'trade_histories'

class RoomType(models.Model):
    name               = models.CharField(max_length = 5)

    class Meta:
        db_table = 'room_types'

class RoomSubType(models.Model):
    name               = models.CharField(max_length = 10)

    class Meta:
        db_table = 'room_sub_types'

class BuildingUse(models.Model):
    name               = models.CharField(max_length = 10)

    class Meta:
        db_table = 'building_uses'

class RoomAddInfo(models.Model):
    is_builtin         = models.BooleanField()
    is_elevator        = models.BooleanField()
    is_pet             = models.BooleanField()
    is_balcony         = models.BooleanField()
    is_loan            = models.BooleanField()
    is_parking         = models.BooleanField()
    parking_fee        = models.IntegerField(null = True)

    class Meta:
        db_table = 'room_add_infos'

class Floor(models.Model):
    name              = models.CharField(max_length = 5)

    class Meta:
        db_table = 'floors'

class MovingDateType(models.Model):
    name              = models.CharField(max_length = 10)

    class Meta:
        db_table = 'moving_date_types'

class Score(models.Model):
    price             = models.DecimalField(max_digits = 5, decimal_places = 2)
    option            = models.DecimalField(max_digits = 5, decimal_places = 2)
    near              = models.DecimalField(max_digits = 5, decimal_places = 2)
    maintenance       = models.DecimalField(max_digits = 5, decimal_places = 2)
    traffic           = models.DecimalField(max_digits = 5, decimal_places = 2)

    class Meta:
        db_table = 'scores'

class Room(models.Model):
    is_quick            = models.BooleanField(default = False)
    is_confirmed        = models.BooleanField(default = False)
    confirmed_date      = models.DateField(null = True)
    is_agent            = models.BooleanField(default = False)
    is_short_lease      = models.BooleanField(default = False)
    title               = models.CharField(max_length = 500, null = True)
    description         = models.CharField(max_length = 10000, null = True)
    room_size           = models.DecimalField(max_digits = 6, decimal_places = 2)
    provision_size      = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    contract_size       = models.DecimalField(max_digits = 6, decimal_places = 2, null = True)
    room_floor          = models.ForeignKey(Floor, on_delete = models.SET_NULL, null = True, related_name = 'room_floor_set')
    building_floor      = models.ForeignKey(Floor, on_delete = models.SET_NULL, null = True, related_name = 'building_floor_set')
    is_maintenance_nego = models.BooleanField(default = False)
    maintenance_price   = models.IntegerField(null = True)
    longitude           = models.DecimalField(max_digits = 20, decimal_places = 15)
    latitude            = models.DecimalField(max_digits = 20, decimal_places = 15)
    address             = models.CharField(max_length = 45, null = True)
    heat_type           = models.ForeignKey(HeatType, on_delete = models.SET_NULL, null = True)
    moving_date_type    = models.ForeignKey(MovingDateType, on_delete = models.SET_NULL, null = True)
    moving_date         = models.DateField(null = True)
    building_use        = models.ForeignKey(BuildingUse, on_delete = models.SET_NULL, null = True)
    room_type           = models.ForeignKey(RoomType, on_delete = models.SET_NULL, null = True)
    room_sub_type       = models.ForeignKey(RoomSubType, on_delete = models.SET_NULL, null = True)
    score               = models.ForeignKey(Score, on_delete = models.SET_NULL, null = True)
    complex             = models.ForeignKey(Complex, on_delete = models.SET_NULL, null = True)
    complex_space_info  = models.ForeignKey(ComplexSpaceInfo, on_delete = models.SET_NULL, null = True)
    room_add_info       = models.ForeignKey(RoomAddInfo, on_delete = models.SET_NULL, null = True)
    agent               = models.ForeignKey(Agent, on_delete = models.CASCADE)
    belonged_agent      = models.ForeignKey(BelongedAgent, on_delete = models.CASCADE)
    user                = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    room_like           = models.ManyToManyField(User, through = 'RoomLike', related_name = 'room_like_set')
    trade_info     = models.ManyToManyField(TradeType, through = 'TradeInfo', related_name = 'trade_info_set')

    class Meta:
        db_table = 'rooms'

class RoomImage(models.Model):
    image_url           = models.URLField(max_length = 2000)
    room                = models.ForeignKey(Room, on_delete = models.CASCADE)

    class Meta:
        db_table = 'room_images'

class TradeInfo(models.Model):
    deposit             = models.IntegerField()
    trade_type          = models.ForeignKey(TradeType, on_delete = models.SET_NULL, null = True)
    room                = models.ForeignKey(Room, on_delete = models.CASCADE)

    class Meta:
        db_table = 'trade_infos'

class MonthlyTradeInfo(models.Model):
    deposit             = models.IntegerField()
    fee                 = models.IntegerField()
    room                = models.ForeignKey(Room, on_delete = models.CASCADE)

    class Meta:
        db_table = 'monthly_trade_infos'

class RoomLike(models.Model):
    user                = models.ForeignKey(User, on_delete = models.CASCADE)
    room                = models.ForeignKey(Room, on_delete = models.CASCADE)

    class Meta:
        db_table = 'room_likes'
