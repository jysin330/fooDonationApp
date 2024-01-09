from django.db import models
from django.db import IntegrityError
from django.utils import timezone
from django.utils.text import slugify
CATEGORY = (
        ("Raw Food", "Raw Food"),
        ("Packed Food", "Packed Food"),
        ("Cooked Food", "Cooked Food"),
    )
# Create your models here.
class Donate(models.Model):
  
    donar_id = models.AutoField

    category = models.CharField(max_length=30, choices=CATEGORY, default="Raw Food")
    donarName = models.CharField(max_length=20, default="")
    donarEmail = models.EmailField(max_length=70, default="")
    phoneNum = models.CharField(max_length=70, default="")
    foodItem = models.CharField(max_length=50, default="")
    slug= models.SlugField(null =True, blank = True)
    fooDescription = models.CharField(max_length=400, default="")
    address = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    publish = models.DateField(auto_now_add = False, auto_now =False, default = timezone.now)
    def __str__(self):
        return self.foodItem

    def save(self,*args, **kwargs):

        if self.slug is None:
            self.slug = slugify(self.foodItem)

        super().save(*args, **kwargs)



class ReceiverUser(models.Model):
    # object_meal = Donate.objects.all()

    # meal = ()
    # temp = list(meal)
    # for x in object_meal:
    #     if x.foodItem:
    #         temp.append((f"{x.foodItem}", f"{x.foodItem}"))
    # meal = tuple(temp)
    category = models.CharField(max_length=30, choices=CATEGORY, default="Raw Food")
    receiver_id = models.AutoField
    receiver_meal = models.CharField(max_length=30, default="")
    receiver_name = models.CharField(max_length=30)
    receiver_num = models.CharField(max_length=10, default="")
    receiver_email = models.CharField(max_length=50, default="")
    receiver_address = models.CharField(max_length=70)
    des = models.TextField()
    timestamp = models.DateTimeField(auto_now_add =True)
    update = models.DateTimeField(auto_now =True)
    publish = models.DateField(auto_now_add = False, auto_now =False, default = timezone.now)

