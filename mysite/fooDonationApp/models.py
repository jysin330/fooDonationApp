from django.db import models
from django.db import IntegrityError


# Create your models here.
class Donate(models.Model):
    CATEGORY = (
        ("Raw Food", "Raw Food"),
        ("Packed Food", "Packed Food"),
        ("Cooked Food", "Cooked Food"),
    )
    donar_id = models.AutoField

    category = models.CharField(max_length=30, choices=CATEGORY, default="1")
    donarName = models.CharField(max_length=20, default="")
    donarEmail = models.EmailField(max_length=70, default="")
    phoneNum = models.CharField(max_length=70, default="")
    foodItem = models.CharField(max_length=50, default="")
    fooDescription = models.CharField(max_length=400, default="")
    address = models.CharField(max_length=100, default="")

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
