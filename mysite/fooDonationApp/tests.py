from django.test import TestCase

# Create your tests here.
from .models import DonateRecipe
from .utils import slugify_instance_foodItem
from django.utils.text import slugify
class DonateRecipeTestCase(TestCase):
    def setUp(self):
        self.Number_of_foodItem= 500
        for i in range(0,self.Number_of_foodItem):
            DonateRecipe.objects.create(donarName= "jyoti singh" , foodItem= "papdichart")


    def test_queryset_exists(self):
        qs = DonateRecipe.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = DonateRecipe.objects.all()
        self.assertEqual(qs.count(),self.Number_of_foodItem)
    
    def test_papdichart_slug(self):
        obj = DonateRecipe.objects.all().order_by("id").first()

        foodItem = obj.foodItem
        slug = obj.slug
        slugified_foodItem =slugify(foodItem)

        self.assertEqual(slug, slugified_foodItem)

    def test_papdichart_unique_slug(self):
        # qs = Donate.objects.exclude(slug__iexact = "aalu-paratha")
        qs = DonateRecipe.objects.exclude(slug__iexact = "papdichart")
        for obj in qs:
            foodItem = obj.foodItem
            slug = obj.slug
            slugified_foodItem =slugify(foodItem)

            self.assertNotEqual(slug, slugified_foodItem)

    def test_slugify_instance_foodItem(self):
        obj = DonateRecipe.objects.all().last()
        new_slugs= []
        for i in range(0,25):
            instance = slugify_instance_foodItem(obj, save =False)
            new_slugs.append(instance.slug)
        
        unique_slugs= list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_foodItem_redux(self):
        slug_list = DonateRecipe.objects.all().values_list('slug', flat =True)

        unique_slugs_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slugs_list))

    def test_meal_search_manager(self):
        qs = DonateRecipe.objects.search(query = "papdichart")
        self.assertEqual(qs.count(), self.Number_of_foodItem)
        qs = DonateRecipe.objects.search(query = "papdi")
        self.assertEqual(qs.count(), self.Number_of_foodItem)