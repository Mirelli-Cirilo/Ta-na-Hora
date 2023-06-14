from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cadastro.views import cadastro, loginPage, logoutPage

class TestUrls(SimpleTestCase):

    def test_cadastro_url_resolved(self):
        url = reverse('cadastro')
        self.assertEquals(resolve(url).func, cadastro) 

    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutPage)         