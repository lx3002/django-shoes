from django.db import models


# Create your models here.
class shoes(models.Model):
    shoes_name = models.CharField(max_length=30)
    shoes_price = models.CharField(max_length=300)
    shoes_image = models.CharField(max_length=250)

    class Meta:
        db_table = "shoe"


