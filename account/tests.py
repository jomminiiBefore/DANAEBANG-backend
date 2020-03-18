import json
import json
import jwt
import bcrypt
import time

from my_settings    import SECRET, SMS
from account.models     import User, SocialLoginType, AuthSMS

from unittest.mock  import patch, MagicMock
from django.test    import TestCase, Client

class SignUpTest(TestCase):
    def setUp(self):
        User.objects.create(
            name         = 'hyun',
            email        = 'hyun@email.com',
            password     = 'hyun!1234',
            phone_number = '010-0000-0000', 
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_sign_up_success(self):
        user = {
            'name'        : 'jang',
            'email'       : 'jang@email.com',
            'password'    : 'jang!1234',
            'phone_number': '010-1111-0000',
        }

        client   = Client()
        response = client.post('/account/sign-up', json.dumps(user), content_type='application/json')
        user     = User.objects.get(email = user['email'])
        token    = jwt.encode({'user_id': user.id}, SECRET['secret'], algorithm = SECRET['algorithm']).decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'token': token
            }
        )

    def test_sign_up_duplicate_phone_number(self):
        user = {
            'name'        : 'hyun',
            'email'       : 'hyun@email.com',
            'password'    : 'hyun!1234',
            'phone_number': '010-0000-0000'
        }
        client   = Client()
        response = client.post('/account/sign-up', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'DUPLICATE_PHONE_NUMBER'
            }
        )
        
    def test_sign_up_duplicate_email(self):
        user = {
            'name'        : 'hyun',
            'email'       : 'hyun@email.com',
            'password'    : 'hyun!1234',
            'phone_number': '010-1111-0000'
        }
        client   = Client()
        response = client.post('/account/sign-up', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'DUPLICATE_EMAIL'
            }
        )
        
    def test_sign_up_invalid_key(self):
        user = {
            'name_en'     : 'hyun',
            'email_en'    : 'hyun@email.com',
            'password'    : 'hyun!1234',
            'phone_number': '010-0000-0000'
        }

        client   = Client()
        response = client.post('/account/sign-up', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_KEY'
            }
        )

    def test_sign_up_invalid_email(self):
        user = {
            'name'        : 'hyun',
            'email'       : 'hyun!email.com',
            'password'    : 'hyun!1234',
            'phone_number': '010-0000-0000'
        }
        client   = Client()
        response = client.post('/account/sign-up', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_EMAIL'
            }
        )

class SignInTest(TestCase):
    def setUp(self):
        password = bcrypt.hashpw('hyun!1234'.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            email        = 'hyun@email.com',
            password     = password, 
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_sign_in_success(self):
        user = {
            'email'       : 'hyun@email.com',
            'password'    : 'hyun!1234',
        }

        client   = Client()
        response = client.post('/account/sign-in', json.dumps(user), content_type='application/json')
        user     = User.objects.get(email = user['email'])
        token    = jwt.encode({'user_id': user.id}, SECRET['secret'], algorithm = SECRET['algorithm']).decode()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'token': token
            }
        )

    def test_sign_in_email_fail(self):
        user = {
            'email'       : 'jang@email.com',
            'password'    : 'hyun!1234',
        }

        client   = Client()
        response = client.post('/account/sign-in', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_sign_in_password_fail(self):
        user = {
            'email'       : 'hyun@email.com',
            'password'    : 'jang!1234',
        }

        client   = Client()
        response = client.post('/account/sign-in', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_sign_in_invalid_key(self):
        user = {
            'email_en'    : 'hyun@email.com',
            'password'    : 'hyun!1234',
        }
        
        client   = Client()
        response = client.post('/account/sign-in', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_KEY'
            }
        )

    def test_sign_in_invalid_email(self):
        user = {

            'email'       : 'hyun!email.com',
            'password'    : 'hyun!1234',
        }

        client   = Client()
        response = client.post('/account/sign-in', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message': 'INVALID_EMAIL'
            }
        )

class KakaoLoginTest(TestCase):
    def setUp(self):
        SocialLoginType.objects.create(name = 'kakao')
        User.objects.create(
            name                 = 'hyun',
            email                = 'hyun@email.com',
            phone_number         = '010-0000-0000',
            social_login_id      = '12345678',
            social_login_type_id = SocialLoginType.objects.get(name = 'kakao').id
        )
        
    def tearDown(self):
        User.objects.all().delete()
        SocialLoginType.objects.all().delete
        
    @patch('account.views.requests')
    def test_kakao_login_true(self, mocked_request):
        class FakeResponse:
            def json(self):
                return {
                    "id" : '12345678',
                    "properties" : {"nickname": "이름"},
                }
                 
        mocked_request.get = MagicMock(return_value = FakeResponse())
        
        client = Client()
        header = {'HTTP_Authorization':'fake.token1'}
        response = client.get('/account/kakao-login', **header, content_type='applications/json')
        self.assertEqual(response.status_code, 200)
    
    @patch('account.views.requests')
    def test_kakao_login_false(self, mocked_request):
        class FakeResponse:
            def json(self):
                return {
                    "id" : '857465848',
                    "properties" : {"nickname": "이름"},
                }
                 
        mocked_request.get = MagicMock(return_value = FakeResponse())

        client = Client()
        header = {'HTTP_Authorization':'fake.token2'}
        response = client.get('/account/kakao-login', **header, content_type='applications/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'social_login_data':
                {
                    'name'                : '이름',
                    'social_login_id'     : '857465848',
                    'social_login_type_id': SocialLoginType.objects.get(name = 'kakao').id
                }
            }
        )

class FacebookSignInViewTest(TestCase):
    def setUp(self):
        SocialLoginType.objects.create(name = 'facebook')
        User.objects.create(
            name                = 'testname',
            email               = 'test@gmail.com',
            phone_number        = '010-1234-5678',
            social_login_id     = '3187176975214272',
            social_login_type   = SocialLoginType.objects.get(name = 'facebook')
        )
    
    def tearDown(self):
        User.objects.all().delete()
        SocialLoginType.objects.all().delete()

    @patch('account.views.requests')
    def test_facebook_signin_view_exists(self, mocked_request):
        class FakeResponse:
            def json(self):
                return {
                    'id'    : '3187176975214272',
                    'name'  : 'testname',
                }

        mocked_request.get  = MagicMock(return_value = FakeResponse())
        client              = Client()
        header              = {'HTTP_Authorization' : 'fake.access_token'}
        response            = client.get(
            '/account/facebook-signin',
            content_type = 'applications/json',
            **header
        )
        
        self.assertEqual(response.status_code, 200)

    @patch('account.views.requests')
    def test_facebook_signin_view_not_exists(self, mocked_request):
        class FakeResponse:
            def json(self):
                return {
                    'id'    : '1293858102939103',
                    'name'  : 'helloman'
                }

        mocked_request.get  = MagicMock(return_value = FakeResponse())
        client              = Client()
        header              = {'HTTP_Authorization' : 'fake.access_token2'}
        response            = client.get(
            '/account/facebook-signin',
            content_type = 'applications/json',
            **header
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'social_login_data': {
                    'name'                  : 'helloman',
                    'social_login_id'       : '1293858102939103',
                    'social_login_type_id'  :  SocialLoginType.objects.get(name = 'facebook').id
                }
            }
        )

class AuthSMSViewTest(TestCase):
    def setUp(self):
        AuthSMS.objects.create(
            phone_number    = '01012345678',
            auth_code       = 123456
        )

    def tearDown(self):
        AuthSMS.objects.all().delete()

    def test_auth_sms_view_success(self):
        time.sleep(120)
        phone_data = {
            'phone_number' : '01012345678'
        }

        client      = Client()
        response    = client.post('/account/auth-mobile',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )

    def test_auth_sms_view_success2(self):
        phone_data = {
            'phone_number' : '01045678900'
        }

        client      = Client()
        response    = client.post('/account/auth-mobile',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )

    def test_auth_sms_view_invalid_key(self):
        phone_data = {
            'phone' : '01056781234'
        }

        client      = Client()
        response    = client.post('/account/auth-mobile',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEY'
            }
        )

class AuthSMSConfirmViewTest(TestCase):
    def setUp(self):
        AuthSMS.objects.create(
            phone_number    = '01012345678',
            auth_code       = 123456
        )
    
    def tearDown(self):
        AuthSMS.objects.all().delete()

    def test_auth_sms_confirm_view_success(self):
        phone_data = {
            'phone_number'  : '01012345678',
            'auth_code'     : 123456
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {
                'message' : 'SUCCESS'
            }
        )

    def test_auth_sms_confirm_view_incorrect_code(self):
        phone_data = {
            'phone_number'  : '01012345678',
            'auth_code'     : 456789
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INCORRECT_CODE'
            }
        )

    def test_auth_sms_confirm_view_invalid_key(self):
        phone_data = {
            'phone'     : '01012345678',
            'auth_code' : 123456
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INVALID_KEY'
            }
        )

    def test_auth_sms_confirm_view_not_exist(self):
        phone_data = {
            'phone_number'  : '01056781234',
            'auth_code'     : 567123
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')

        self.assertEqual(response.status_code, 401)

    def test_auth_sms_confirm_view_empty_data(self):
        phone_data = {
            'phone_number'  : '',
            'auth_code'     : ''
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)

    def test_auth_sms_confirm_view_empty_phone_number(self):
        phone_data = {
            'phone_number'  : '',
            'auth_code'     : 567123
        }

        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)

    def test_auth_sms_confirm_view_empty_auth_code(self):
        phone_data = {
            'phone_number'  : '01012345678',
            'auth_code'     : '',
        }
        
        client      = Client()
        response    = client.post('/account/mobile-confirm',
                                  json.dumps(phone_data),
                                  content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
            {
                'message' : 'INCORRECT_CODE'
            }
        )
