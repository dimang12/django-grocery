from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length = 250)
    category = models.IntegerField()
    subCategory = models.IntegerField()
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
