import json
import jwt
import bcrypt

from account.models     import User
from my_settings        import SECRET

from django.test        import (
    TestCase,
    Client
)

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