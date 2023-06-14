from django.test import TestCase, Client
from django.urls import reverse
from base.models import Remedio
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.remedio1 = Remedio.objects.create(nome='Benzetacil', horario='16:00', descricao='tome')
        self.delete_url = reverse('delete', args=[1])
        self.detail_url = reverse('detail', args=[1])
        self.update_url = reverse('update', args=[1])
        self.email_url = reverse('email', args=[1])
        self.user = User.objects.create_user(
            
            username='Larissa', email='larissa123@gmail.com',
            password='abc123#',            
        )
            
            

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_POST_add_new_medicine(self):
        response = self.client.post(self.home_url, {
            
            'nome': 'Benzetacil',
            'horario': '16:00',
            'descricao': 'tomar depois de comer',
            'user': self.user.id
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.remedio1.nome, 'Benzetacil')

    def test_delete_GET(self):
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_delete_POST(self):
        response = self.client.post(self.delete_url)
        self.assertEquals(response.status_code, 302)

    def test_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

    def test_update_GET(self):
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')

    def test_update_POST(self):
        response = self.client.post(self.update_url, {
            
            'nome': 'Benzetacil',
            'descricao': 'nao beber suco de maracuja',
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.remedio1.nome, 'Benzetacil')

    def test_envio_email_POST(self):
        response = self.client.post(self.email_url)

        self.assertEquals(response.status_code, 200)