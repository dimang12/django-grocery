from django.db import models

class Categories(models.Model):
    cateName = models.CharField(max_length=200)
    cateDetail = models.TextField()
    cateParent = models.IntegerField() 
    cateCreated = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    proName = models.CharField(max_length= 250)
    categoryId = models.ForeignKey(Categories, on_delete= models.CASCADE)
    proDetail = models.TextField()
    proPrice = models.FloatField()
    proWeight = models.CharField(max_length= 100)
    proDimension = models.CharField(max_length= 200)
    proIsPublish = models.BooleanField(default=True)
    proCreated = models.DateTimeField(auto_now_add=True)