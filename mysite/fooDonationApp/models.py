from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from .utils import slugify_instance_foodItem
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.db.models import Q
from django.conf import settings
CATEGORY = (
        ("Raw Food", "Raw Food"),
        ("Packed Food", "Packed Food"),
        ("Cooked Food", "Cooked Food"),
    )

User = settings.AUTH_USER_MODEL
class DonateQuerySet(models.QuerySet):
     def search(self,query =None):
          if query is None or query == "":
               return self.none()
          
          lookups = Q(foodItem__icontains =query) | Q(fooDescription__icontains =query) | Q(category__icontains =query)
          return self.filter(lookups)
     

class DonateManager(models.Manager):
     def get_queryset(self):
         return DonateQuerySet(self.model , using =self.db)
     def search(self,query =None):
          return self.get_queryset().search(query=query)
     

class Donate(models.Model):
  
    donar_id = models.AutoField
    user = models.ForeignKey(User, blank = True, null= True , on_delete= models.SET_NULL)
    category = models.CharField(max_length=30, choices=CATEGORY, default="Raw Food")
    donarName = models.CharField(max_length=20, default="")
    donarEmail = models.EmailField(max_length=70, default="")
    phoneNum = models.CharField(max_length=70, default="")
    foodItem = models.CharField(max_length=50, default="")
    slug= models.SlugField(unique= True, null =True, blank = True)
    fooDescription = models.CharField(max_length=400, default="")
    address = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    publish = models.DateField(auto_now_add = False, auto_now =False, default = timezone.now)
    objects = DonateManager()

    def __str__(self):
        return self.foodItem

    def get_absolute_url(self):
         return reverse('meal-detail', kwargs={"slug" : self.slug})
         

    # Where ever the save method is called these signals(pre_save and post_save) be called, including over-riding the save method is called.
    def save(self,*args, **kwargs):
        # obj = Donate.objects.get(id=1)
        # set something
        # if self.slug is None:
        #     self.slug = slugify(self.foodItem)

        super().save(*args, **kwargs)
        # obj.save()
        # do another something
     

#  instance is the actual instance of whatever the model that's being sent and sender is the actual model class itself which we can test out by doing sender and instance.
def donate_pre_save(sender, instance, *args, **kwargs):
  
    if instance.slug is None:
            slugify_instance_foodItem(instance, save=False)

pre_save.connect(donate_pre_save, sender= Donate)

def donate_post_save(sender, instance, created,*args, **kwargs):
    
    if created:
        #  instance.slug = "This is the slug!!"
        slugify_instance_foodItem(instance, save=True)

post_save.connect(donate_post_save, sender= Donate)


class ReceiverUser(models.Model):
    # object_meal = Donate.objects.all()

    # meal = ()
    # temp = list(meal)
    # for x in object_meal:
    #     if x.foodItem:
    #         temp.append((f"{x.foodItem}", f"{x.foodItem}"))
    # meal = tuple(temp)
    receiver_meal = models.ForeignKey(Donate, blank = True, null= True , on_delete= models.SET_NULL)
    category = models.CharField(max_length=30, choices=CATEGORY, default="Raw Food")
    receiver_id = models.AutoField
    
    receiver_name = models.CharField(max_length=30)
    receiver_num = models.CharField(max_length=10, default="")
    receiver_email = models.CharField(max_length=50, default="")
    receiver_address = models.CharField(max_length=70)
    des = models.TextField()
    timestamp = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    publish = models.DateField(auto_now_add = False, auto_now =False, default = timezone.now)


# class DonateManager(models.Manager):
#      def search(self,query =None):
#           if query in None or "":
#                return self.get_queryset().none()
          
#           lookups = Q(foodItem__icontains =query) | Q(fooDescription__icontains =query) | Q(category__icontains =query)
#           return self.get_queryset().filter(lookups)
        #   return Donate.objects.filter(lookups)
# Create your models here.