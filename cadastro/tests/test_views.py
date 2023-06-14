from django.test import TestCase, Client
from django.urls import reverse
from base.models import Remedio
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.cadastro_url = reverse('cadastro')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(
            username='Larissa', email='larissa123@gmail.com',
            password='abc123#'   
        )

    def test_cadastro_GET(self):
        response = self.client.get(self.cadastro_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_POST(self):
        response = self.client.post(self.cadastro_url, {      
            'username': 'Maria',
            'email': 'Maria@gmail.com',
            'password': 'abc123#'
        })

        self.assertEquals(response.status_code, 302)
   
    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_POST(self):
        response = self.client.post(self.login_url, {      
            'username': 'Larissa',
            'senha': 'abc123#'
        })

        self.assertEquals(response.status_code, 302)  

    def test_logout_POST(self):
        response = self.client.post(self.logout_url, {      
            'username': 'Larissa',
            'senha': 'abc123#'
        })

        self.assertEquals(response.status_code, 302) 