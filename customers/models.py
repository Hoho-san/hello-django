from django.db import models

#try git if working

class Customer(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
