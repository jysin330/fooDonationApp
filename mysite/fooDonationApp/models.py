from django.db import models
from django.db import IntegrityError


# Create your models here.
class Donate(models.Model):
    donar_id = models.AutoField
    category = models.CharField(max_length=140, null=True)
    donarName = models.CharField(max_length=20)
    donarEmail = models.EmailField(max_length=70, default="")
    phoneNum = models.CharField(max_length=70, default="")
    foodItem = models.CharField(max_length=50)
    fooDescription = models.CharField(max_length=400)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fooDonation/images", default="")

    def __str__(self):
        return self.foodItem


class ReceiverUser(models.Model):
    receiver_id = models.AutoField
    receiver_meal = models.CharField(max_length=30, null=True)
    receiver_name = models.CharField(max_length=30)
    receiver_num = models.CharField(max_length=10, default="")
    receiver_email = models.CharField(max_length=50, default="")
    receiver_address = models.CharField(max_length=70)
    des = models.TextField()
