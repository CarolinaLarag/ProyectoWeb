from django.test import TestCase
from blog.forms import ProveedorForm
from blog.views import post_new

# Create your tests here.
class TestProv(TestCase):
    def test_expense_form_valid_data(self):
        form = ProveedorForm(data={
            'name': 'prueba test',
            'text': 'prueba unitaria',
            'image': ''
        })

        self.assertTrue(form.is_valid())

class TestURL(TestCase):
    def teset_index(self):
        url = reverse('post_new')
        print(resolve(url))
        self.assertEquals(resolve(url).func,post_new)