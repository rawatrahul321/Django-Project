from django.db import models
from passlib.hash import pbkdf2_sha256


class contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    mobile = models.IntegerField()
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# Create your models here.
class Regis_db(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
