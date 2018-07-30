from django.db import models

# Create your models here.

class Product(models.Model):
    Title = models.CharField(max_length=40)
    Event =  models.TextField(blank=True,null=True)
    Time =  models.DateTimeField(blank = True,null=True)
    Feature = models.BooleanField(default = True)
    Summary = models.TextField(default='This is the summary')
