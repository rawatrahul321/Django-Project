from django.db import models

from homepage.models import Regis_db


# Create your models here.
class emp_account(models.Model):
    user_name = models.OneToOneField(Regis_db, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    DISPLAY_CHOICES = (
        ("male", "Male"),
        ("female", "Female")
    )

    gender = models.CharField(choices=DISPLAY_CHOICES, max_length=128)
    mobile = models.IntegerField()
    bday = models.DateField()
    add1 = models.CharField(max_length=120)
    email = models.EmailField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    filename = models.ImageField(blank=True, null=True)
    account = models.IntegerField()
    bank = models.CharField(max_length=40)
    pfaccount = models.IntegerField()
    joining_date = models.DateField()

    def __str__(self):
        return self.fullname
