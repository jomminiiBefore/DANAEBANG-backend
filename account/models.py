from django.db import models

class User(models.Model):
    name         = models.CharField(max_length = 45)
    email        = models.EmailField(max_length = 100, unique = True)
    password     = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 13, unique = True)
    image_url    = models.URLField(max_length = 2000, null = True)
    kakao_id     = models.CharField(max_length = 45, null = True)
    facebook_id  = models.CharField(max_length = 45, null = True)
    create_at    = models.DateTimeField(auto_now_add = True)
    update_at    = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'users'
