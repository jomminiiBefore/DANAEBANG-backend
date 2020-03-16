import jwt

from .models     import User
from my_settings import SECRET

from django.http import (
    JsonResponse,
    HttpResponse
)

def requirelogin(func):
    
    def wrapper(self, request, *args, **kwargs):

        try:
            token = request.headers.get('token', None)
            user_id = jwt.decode(
                token, 
                SECRET['secret'], 
                algorithm = SECRET['algorithm']
            ).get('user_id', None)
            
            if User.objects.filter(id = user_id).exists():
                user = User.objects.get(id = user_id)
                request.user = user 
            else:
                return HttpResponse(status = 401)
            
        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status = 403)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status = 401)

        return func(self, request, *args, **kwargs)
    return wrapper