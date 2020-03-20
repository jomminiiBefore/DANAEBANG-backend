# Generated by Django 3.0.3 on 2020-03-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'building_uses',
            },
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('enter_date', models.CharField(max_length=45, null=True)),
                ('household_num', models.IntegerField(null=True)),
                ('building_num', models.IntegerField(null=True)),
                ('parking_average', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('build_cov_ratio', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('floor_area_index', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('lowest_floor', models.IntegerField(null=True)),
                ('highest_floor', models.IntegerField(null=True)),
                ('provider_name', models.CharField(max_length=45)),
                ('jibun_address', models.CharField(max_length=45, null=True)),
                ('road_address', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'complexes',
            },
        ),
        migrations.CreateModel(
            name='ComplexPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_average_pyeong_price', models.IntegerField(null=True)),
                ('lease_average_pyeong_price', models.IntegerField(null=True)),
                ('trade_region_average_pyeong_price', models.IntegerField(null=True)),
                ('lease_region_average_pyeong_price', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'complex_price_infos',
            },
        ),
        migrations.CreateModel(
            name='ComplexSpaceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyeong_type', models.CharField(max_length=10)),
                ('room_size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('provision_size', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('contract_size', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('maintenance_price', models.IntegerField(null=True)),
                ('beds_num', models.IntegerField(null=True)),
                ('bath_num', models.IntegerField(null=True)),
                ('lay_out_image_URL', models.URLField(max_length=2000, null=True)),
                ('extend_lay_out_image_URL', models.URLField(max_length=2000, null=True)),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Complex')),
            ],
            options={
                'db_table': 'complex_space_infos',
            },
        ),
        migrations.CreateModel(
            name='ComplexType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'complex_types',
            },
        ),
        migrations.CreateModel(
            name='ConvenienceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'convenience_categories',
            },
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'education_categories',
            },
        ),
        migrations.CreateModel(
            name='EntranceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'entrance_types',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'floors',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fuel_types',
            },
        ),
        migrations.CreateModel(
            name='HeatType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'heat_types',
            },
        ),
        migrations.CreateModel(
            name='MovingDateType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'moving_date_types',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_quick', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('confirmed_date', models.DateField(null=True)),
                ('is_agent', models.BooleanField(default=False, null=True)),
                ('is_short_lease', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=10000, null=True)),
                ('room_size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('provision_size', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('contract_size', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('is_maintenance_nego', models.BooleanField(default=False)),
                ('maintenance_price', models.IntegerField(null=True)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('address', models.CharField(max_length=45, null=True)),
                ('moving_date', models.DateField(null=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Agent')),
                ('belonged_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.BelongedAgent')),
                ('building_floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building_floor_set', to='room.Floor')),
                ('building_use', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.BuildingUse')),
                ('complex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Complex')),
                ('complex_space_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.ComplexSpaceInfo')),
                ('heat_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.HeatType')),
                ('moving_date_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.MovingDateType')),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomAddInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_builtin', models.BooleanField()),
                ('is_elevator', models.BooleanField()),
                ('is_pet', models.BooleanField()),
                ('is_balcony', models.BooleanField()),
                ('is_loan', models.BooleanField()),
                ('is_parking', models.BooleanField()),
                ('parking_fee', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'room_add_infos',
            },
        ),
        migrations.CreateModel(
            name='RoomSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'room_sub_types',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='SafetyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'safety_categories',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('option', models.DecimalField(decimal_places=2, max_digits=5)),
                ('near', models.DecimalField(decimal_places=2, max_digits=5)),
                ('maintenance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('traffic', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'scores',
            },
        ),
        migrations.CreateModel(
            name='TradeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'trade_types',
            },
        ),
        migrations.CreateModel(
            name='TradeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.IntegerField()),
                ('fee', models.IntegerField(null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room')),
                ('trade_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.TradeType')),
            ],
            options={
                'db_table': 'trade_infos',
            },
        ),
        migrations.CreateModel(
            name='TradeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('deposit', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('floor', models.IntegerField()),
                ('complex_space_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.ComplexSpaceInfo')),
                ('trade_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.TradeType')),
            ],
            options={
                'db_table': 'trade_histories',
            },
        ),
        migrations.CreateModel(
            name='SafetyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('safety_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.SafetyCategory')),
            ],
            options={
                'db_table': 'safety_infos',
            },
        ),
        migrations.CreateModel(
            name='RoomLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'db_table': 'room_likes',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Room')),
            ],
            options={
                'db_table': 'room_images',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='room_add_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomAddInfo'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_floor_set', to='room.Floor'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_like',
            field=models.ManyToManyField(related_name='room_like_set', through='room.RoomLike', to='account.User'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_sub_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomSubType'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.RoomType'),
        ),
        migrations.AddField(
            model_name='room',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.Score'),
        ),
        migrations.AddField(
            model_name='room',
            name='trade_info',
            field=models.ManyToManyField(related_name='trade_info_set', through='room.TradeInfo', to='room.TradeType'),
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.User'),
        ),
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('education_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.EducationCategory')),
            ],
            options={
                'db_table': 'education_infos',
            },
        ),
        migrations.CreateModel(
            name='ConvenienceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('convenience_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.ConvenienceCategory')),
            ],
            options={
                'db_table': 'convenience_infos',
            },
        ),
        migrations.AddField(
            model_name='complexspaceinfo',
            name='entrance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.EntranceType'),
        ),
        migrations.CreateModel(
            name='ComplexLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Complex')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
            options={
                'db_table': 'complex_likes',
            },
        ),
        migrations.CreateModel(
            name='ComplexImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.Complex')),
            ],
            options={
                'db_table': 'complex_images',
            },
        ),
        migrations.AddField(
            model_name='complex',
            name='complex_like',
            field=models.ManyToManyField(through='room.ComplexLike', to='account.User'),
        ),
        migrations.AddField(
            model_name='complex',
            name='complex_price_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.ComplexPriceInfo'),
        ),
        migrations.AddField(
            model_name='complex',
            name='complex_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.ComplexType'),
        ),
        migrations.AddField(
            model_name='complex',
            name='entrance_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.EntranceType'),
        ),
        migrations.AddField(
            model_name='complex',
            name='fuel_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.FuelType'),
        ),
        migrations.AddField(
            model_name='complex',
            name='heat_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='room.HeatType'),
        ),
    ]
