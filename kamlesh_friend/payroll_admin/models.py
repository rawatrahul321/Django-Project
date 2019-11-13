from django.db import models

from homepage.models import Regis_db

class admin_destination(models.Model):

    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    special_offer = models.BooleanField(default=False)


    def __str__(self):
        return self.name






class admin_model(models.Model):
    admin_username = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=12)

    def __str__(self):
        return self.admin_username


class add_department_model(models.Model):
    add_department = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.add_department


class add_designation_model(models.Model):
    add_designation = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.add_designation


class salary_details(models.Model):
    user_name = models.ForeignKey(Regis_db, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    emp_name = models.CharField(max_length=30)
    mp = models.CharField(max_length=15)
    working_days = models.IntegerField()
    bs = models.IntegerField()
    house_rent = models.IntegerField()
    mediclaim = models.IntegerField()
    travel = models.IntegerField()
    dearness = models.IntegerField()
    reimburement = models.IntegerField()
    conveyance = models.IntegerField()
    other_salary = models.IntegerField()
    year_salary = models.IntegerField()
    provident_fund = models.IntegerField()
    total_tax = models.IntegerField()
    total_deduction = models.IntegerField()
    total_salary = models.IntegerField()

    def __str__(self):
        return self.emp_name


class admin_account(models.Model):
    user_name = models.ForeignKey(admin_model, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)
    DISPLAY_CHOICES = (
        ("male", "Male"),
        ("female", "Female")
    )

    gender = models.CharField(choices=DISPLAY_CHOICES, max_length=128)
    email = models.EmailField(max_length=30)
    mobile = models.IntegerField()
    bday = models.DateField()
    add1 = models.CharField(max_length=120)

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


class add_admin_sal(models.Model):
    user_name = models.ForeignKey(admin_model, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    admin_name = models.CharField(max_length=30)
    mp = models.CharField(max_length=15)
    working_days = models.IntegerField()
    bs = models.IntegerField()
    house_rent = models.IntegerField()
    mediclaim = models.IntegerField()
    travel = models.IntegerField()
    dearness = models.IntegerField()
    reimburement = models.IntegerField()
    conveyance = models.IntegerField()
    other_salary = models.IntegerField()
    year_salary = models.IntegerField()
    provident_fund = models.IntegerField()
    total_tax = models.IntegerField()
    total_deduction = models.IntegerField()
    total_salary = models.IntegerField()

    def __str__(self):
        return self.admin_name
