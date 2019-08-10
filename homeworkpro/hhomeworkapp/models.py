from django.db import models

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    contactnumber=models.IntegerField()
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=100)
