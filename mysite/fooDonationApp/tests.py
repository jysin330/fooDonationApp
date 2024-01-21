from django.test import TestCase

# Create your tests here.
from .models import Donate
from django.utils.text import slugify
class DonateTestCase(TestCase):
    def setUp(self):
        self.Number_of_foodItem= 5
        for i in range(0,self.Number_of_foodItem):
            Donate.objects.create(donarName= "jyoti singh" , foodItem= "papdichart")


    def test_queryset_exists(self):
        qs = Donate.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Donate.objects.all()
        self.assertEqual(qs.count(),self.Number_of_foodItem)
    
    def test_foodItem_slug(self):
        obj = Donate.objects.all().order_by("id").first()

        foodItem = obj.foodItem
        slug = obj.slug
        slugified_foodItem =slugify(foodItem)

        self.assertEqual(slug, slugified_foodItem)

    def test_foodItem_unique_slug(self):
        # qs = Donate.objects.exclude(slug__iexact = "aalu-paratha")
        qs = Donate.objects.exclude(slug__iexact = "papdichart")
        for obj in qs:
            foodItem = obj.foodItem
            slug = obj.slug
            slugified_foodItem =slugify(foodItem)

            self.assertNotEqual(slug, slugified_foodItem)
