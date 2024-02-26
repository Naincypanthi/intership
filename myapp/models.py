from django.db import models
class web(models.Model):
    categories=models.CharField(max_length=20)
    date=models.IntegerField()
    amount=models.IntegerField()
class user(models.Model):
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
   
# Create your models here.
