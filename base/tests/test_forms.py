from django.test import SimpleTestCase
from base.forms import Remedioforms

class TestForms(SimpleTestCase):

    def test_remedio_form_valid_data(self):
        form = Remedioforms(data={
            'nome': 'Amanda',
            'horario': '16:00',
            'descricao': 'Tome seu remedio'
        })

        self.assertTrue(form.is_valid())

    def test_remedio_form_no_data(self):
        form = Remedioforms(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
