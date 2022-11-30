from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    