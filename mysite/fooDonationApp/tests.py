from django.test import TestCase

# Create your tests here.
from .models import Donate

class DonateTestCase(TestCase):
    def setUp(self):
        Donate.objects.create(donarName= "jyoti singh", foodItem= "vegies" ,address= "bhaluhi")
        

    def test_queryset_exists(self):
        qs = Donate.objects.all()
        self.assertTrue(qs.exists())
