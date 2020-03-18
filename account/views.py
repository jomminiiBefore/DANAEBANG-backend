import json
import bcrypt
import jwt
import re
import requests
import datetime

from my_settings            import SECRET, SMS
from .models                import (
    User,
    AuthSMS,
    SocialLoginType
)

from random                 import randint
from django.views           import View
from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.http            import JsonResponse, HttpResponse

PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_])[A-Za-z\d!@#$%^&*()_]{8,}$'

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
            user_check = User.objects.filter(email = data['email'])
            social_login_id = data.get('social_login_id', None)
            
            if User.objects.filter(phone_number = data['phone_number']).exists():
                return JsonResponse({'message': 'DUPLICATE_PHONE_NUMBER'}, status = 400)
            
            if not user_check.exists():
                
                if not social_login_id:

                    if not re.match(PASSWORD_VALIDATION, data['password']):
                        return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 400)

                    password = bcrypt.hashpw(
                        data['password'].encode(), 
                        bcrypt.gensalt()
                    ).decode()
                else:
                    password = None

                User.objects.create(
                    name                 = data['name'],
                    email                = data['email'],
                    password             = password,
                    phone_number         = data['phone_number'],
                    social_login_id      = social_login_id,
                    social_login_type_id = data.get('social_login_type_id', None) 
                )

                user  = user_check.get()
                token = jwt.encode(
                    {'user_id': user.id}, 
                    SECRET['secret'], 
                    algorithm = SECRET['algorithm']
                ).decode() 
                return JsonResponse({'token': token}, status = 200)

            return JsonResponse({'message': 'DUPLICATE_EMAIL'}, status = 400)
        
        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status = 400)
        
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)      

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])
            user_check = User.objects.filter(email = data['email'])

            if not re.match(PASSWORD_VALIDATION, data['password']):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status = 400)

            if user_check.exists():
                user = user_check.get()

                if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
                    token = jwt.encode(
                        {'user_id': user.id}, 
                        SECRET['secret'], 
                        algorithm = SECRET['algorithm']
                    ).decode() 
                    return JsonResponse({'token': token}, status = 200)
                
                return HttpResponse(status = 401)
            
            return HttpResponse(status = 401)
        
        except ValidationError:
            return JsonResponse({'message': 'INVALID_EMAIL'}, status = 400)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)

class KakaoLoginView(View):
    def get(self, request):
        access_token    = request.GET.get('code')
        profile_request = requests.get(
            'kapi.kakao.com/v2/user/me', 
            headers = {
                'Authorization': f"Bearer {access_token}"
            }
        )
        profile    = profile_request.json()
        name       = profile.get('properties')['nickname']
        kakao_id   = profile.get('id')
        user_check = User.objects.filter(
            social_login_id = kakao_id, 
            social_login_type__name = 'kakao'
        )
        
        if user_check.exists():
            user  = user_check.get()
            token = jwt.encode(
                {'user_id': user.id}, 
                SECRET['secret'], 
                algorithm = SECRET['algorithm']
            ).decode()
            return JsonResponse({'token': token}, status = 200)

        social_login_type = SocialLoginType.objects.get(name = 'kakao')
        social_login_data = {
            'name'                : name,
            'social_login_id'     : kakao_id,
            'social_login_type_id': social_login_type.id
        }
        return JsonResponse({'social_login_data': social_login_data}, status = 200)

class FacebookSignInView(View):
    def get(self, request):
        facebook_token              = request.headers.get('Authorization')
        facebook_url_user_info      = 'https://graph.facebook.com/v6.0/me'
        user_info_fields            = ['id', 'name']
        param_user_info             = {
            'fields'        : ','.join(user_info_fields),
            'access_token'  : facebook_token
        }
        
        facebook            = SocialLoginType.objects.get(name = 'facebook')
        facebook_user_info  = requests.get(facebook_url_user_info, params = param_user_info)
        facebook_id         = facebook_user_info.json().get('id')
        facebook_name       = facebook_user_info.json().get('name')
        user_check          = User.objects.filter(social_login_type = facebook, social_login_id = facebook_id)
        
        try:
            if user_check.exists():
                user    = (
                    User
                    .objects
                    .get(social_login_type = facebook, social_login_id = facebook_id)
                )
                token   = jwt.encode(
                    {'user_id': user.id},
                    SECRET['secret'],
                    algorithm = SECRET['algorithm'],
                )

                return JsonResponse({'token':token.decode('utf-8')}, status = 200)
            
            social_login_type = SocialLoginType.objects.get(name = 'facebook')
            social_login_data = {
                'name'                  : facebook_name,
                'social_login_id'       : facebook_id,
                'social_login_type_id'  : social_login_type.id
            }
            
            return JsonResponse({'social_login_data' : social_login_data}, status = 200)

        except KeyError:
           return JsonResponse({'message' : 'INVALID_KEYS'}, status = 400)

class AuthSMSView(View):
    def post(self, request):
        try:
            phone_data  = json.loads(request.body)
            auth_number = randint(100000, 1000000)
            auth_data   = AuthSMS.objects.filter(phone_number = phone_data['phone_number'])

            if auth_data.exists():
                auth_data_update_time   = auth_data.values()[0]['updated_at']
                time_limit              = datetime.datetime.now() - auth_data_update_time

                if time_limit.seconds < 120:
                    return HttpResponse(status = 429)

            
            AuthSMS.objects.update_or_create(
                phone_number    = phone_data['phone_number'],
                defaults        = {
                    'phone_number'  : phone_data['phone_number'],
                    'auth_code'     : auth_number
                }
            )

            headers = {
                'Content-Type'          : 'application/json; charset=utf-8',
                'x-ncp-auth-key'        : SMS['ACCESS_KEY'],
                'x-ncp-service-secret'  : SMS['SERVICE_SECRET']
            }

            auth_message = {
                'type'          : 'SMS',
                'contentType'   : 'COMM',
                'countryCode'   : '82',
                'from'          : SMS['FROM'],
                'to'            : [phone_data['phone_number']],
                'content'       : f'[다내방] 인증번호는 \'{auth_number}\' 입니다.'
            }

            requests.post(SMS['URL'], json = auth_message, headers = headers)

            return JsonResponse({'message' : 'SUCCESS'}, status = 200)
        
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)


class AuthSMSConfirmView(View):
    def post(self, request):
        try:
            phone_data  = json.loads(request.body)
            auth_sms    = AuthSMS.objects.get(phone_number = phone_data['phone_number'])
            auth_code   = auth_sms.auth_code

            if auth_code == phone_data['auth_code']:
                return JsonResponse({'message' : 'SUCCESS'}, status = 200)
            
            return JsonResponse({'message' : 'INCORRECT_CODE'}, status = 400)
        
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)

        except AuthSMS.DoesNotExist:
            return HttpResponse(status = 401)
