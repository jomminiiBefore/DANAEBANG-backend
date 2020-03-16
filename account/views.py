import json
import bcrypt
import jwt
import re
import requests

from my_settings            import SECRET
from .models                import (
    User,
    SocialLoginType
)

from django.views           import View
from django.core.validators import validate_email
from django.core.validators import ValidationError
from django.http            import (
    JsonResponse,
    HttpResponse
)

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