from django.db import models
from django.db import IntegrityError


# Create your models here.
class Donate(models.Model):
    donar_id = models.AutoField
    donarName = models.CharField(max_length=20)
    donarEmail = models.EmailField(max_length=70, default="")
    phoneNum = models.CharField(max_length=70, default="")
    foodItem = models.CharField(max_length=50)
    fooDescription = models.CharField(max_length=400)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fooDonation/images", default="")

    def __str__(self):
        return self.foodItem
