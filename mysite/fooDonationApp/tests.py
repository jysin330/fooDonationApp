from django.test import TestCase

# Create your tests here.
from .models import Donate
from .utils import slugify_instance_foodItem
from django.utils.text import slugify
class DonateTestCase(TestCase):
    def setUp(self):
        self.Number_of_foodItem= 500
        for i in range(0,self.Number_of_foodItem):
            Donate.objects.create(donarName= "jyoti singh" , foodItem= "papdichart")


    def test_queryset_exists(self):
        qs = Donate.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Donate.objects.all()
        self.assertEqual(qs.count(),self.Number_of_foodItem)
    
    def test_papdichart_slug(self):
        obj = Donate.objects.all().order_by("id").first()

        foodItem = obj.foodItem
        slug = obj.slug
        slugified_foodItem =slugify(foodItem)

        self.assertEqual(slug, slugified_foodItem)

    def test_papdichart_unique_slug(self):
        # qs = Donate.objects.exclude(slug__iexact = "aalu-paratha")
        qs = Donate.objects.exclude(slug__iexact = "papdichart")
        for obj in qs:
            foodItem = obj.foodItem
            slug = obj.slug
            slugified_foodItem =slugify(foodItem)

            self.assertNotEqual(slug, slugified_foodItem)

    def test_slugify_instance_foodItem(self):
        obj = Donate.objects.all().last()
        new_slugs= []
        for i in range(0,25):
            instance = slugify_instance_foodItem(obj, save =False)
            new_slugs.append(instance.slug)
        
        unique_slugs= list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_foodItem_redux(self):
        slug_list = Donate.objects.all().values_list('slug', flat =True)

        unique_slugs_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slugs_list))

    def test_meal_search_manager(self):
        qs = Donate.objects.search(query = "papdichart")
        self.assertEqual(qs.count(), self.Number_of_foodItem)
        qs = Donate.objects.search(query = "papdi")
        self.assertEqual(qs.count(), self.Number_of_foodItem)