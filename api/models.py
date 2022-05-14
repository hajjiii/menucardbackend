from django.db import models

# Create your models here.
class Foods(models.Model):
    category = models.CharField(max_length=50)
    food_name = models.CharField(max_length=40)
    price = models.IntegerField()
