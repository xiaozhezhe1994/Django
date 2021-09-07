from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('name',max_length=50,default='')
    price = models.DecimalField('price',max_digits=7,decimal_places=2)
    info = models.CharField('描述',max_length=100,default='')

