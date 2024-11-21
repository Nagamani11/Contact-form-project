from django.db import models
class ContactData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    contact = models.BigIntegerField()
    location = models.CharField(max_length=50)
