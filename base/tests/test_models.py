from django.test import TestCase
from base.models import Remedio

class TestModels(TestCase):

    def test_model_str(self):
        remedio1 = Remedio.objects.create(nome='Benzetacil', horario='16:00', descricao='tome')
        self.assertEquals(str(remedio1.nome), 'Benzetacil')

