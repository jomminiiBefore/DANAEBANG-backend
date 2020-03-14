# Generated by Django 3.0.3 on 2020-03-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('face_name', models.CharField(max_length=10)),
                ('face_number', models.CharField(max_length=13)),
                ('business_id', models.CharField(max_length=12)),
                ('registration_id', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=100)),
                ('profile_image_URL', models.URLField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'agents',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('image_url', models.URLField(max_length=2000, null=True)),
                ('kakao_id', models.CharField(max_length=45, null=True)),
                ('facebook_id', models.CharField(max_length=45, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='BelongedAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Agent')),
            ],
            options={
                'db_table': 'belonged_agents',
            },
        ),
    ]
