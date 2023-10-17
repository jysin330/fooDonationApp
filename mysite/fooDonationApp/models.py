from django.db import models


# Create your models here.
class Donate(models.Model):
    donar_id = models.AutoField
    donarName = models.CharField(max_length=20)
    phoneNum = models.IntegerField(max_length=14)
    foodItem = models.CharField(max_length=50)
    fooDescription = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fooDonation/images", default="")

    def __str__(self):
        return self.foodItem
