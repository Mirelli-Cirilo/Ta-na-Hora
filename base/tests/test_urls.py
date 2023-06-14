from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home, delete, update, detail, envio_email

class TestUrls(SimpleTestCase):

    def test_home_url_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_delete_url_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, delete)    

    def test_update_url_resolved(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func, update)       

    def test_detail_url_resolved(self):
        url = reverse('detail', args=[1])
        self.assertEquals(resolve(url).func, detail)       

    def test_envio_email_url_resolved(self):
        url = reverse('email', args=[1])
        self.assertEquals(resolve(url).func, envio_email) 
             