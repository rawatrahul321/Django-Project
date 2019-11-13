# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-23 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_admin_sal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('admin_name', models.CharField(max_length=30)),
                ('mp', models.CharField(max_length=15)),
                ('working_days', models.IntegerField()),
                ('bs', models.IntegerField()),
                ('house_rent', models.IntegerField()),
                ('mediclaim', models.IntegerField()),
                ('travel', models.IntegerField()),
                ('dearness', models.IntegerField()),
                ('reimburement', models.IntegerField()),
                ('conveyance', models.IntegerField()),
                ('other_salary', models.IntegerField()),
                ('year_salary', models.IntegerField()),
                ('provident_fund', models.IntegerField()),
                ('total_tax', models.IntegerField()),
                ('total_deduction', models.IntegerField()),
                ('total_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='add_department_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_department', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='add_designation_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_designation', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='admin_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=128)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('bday', models.DateField()),
                ('add1', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('filename', models.ImageField(blank=True, null=True, upload_to='')),
                ('account', models.IntegerField()),
                ('bank', models.CharField(max_length=40)),
                ('pfaccount', models.IntegerField()),
                ('joining_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='admin_destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('special_offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='admin_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_username', models.CharField(max_length=20)),
                ('admin_password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='salary_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('emp_name', models.CharField(max_length=30)),
                ('mp', models.CharField(max_length=15)),
                ('working_days', models.IntegerField()),
                ('bs', models.IntegerField()),
                ('house_rent', models.IntegerField()),
                ('mediclaim', models.IntegerField()),
                ('travel', models.IntegerField()),
                ('dearness', models.IntegerField()),
                ('reimburement', models.IntegerField()),
                ('conveyance', models.IntegerField()),
                ('other_salary', models.IntegerField()),
                ('year_salary', models.IntegerField()),
                ('provident_fund', models.IntegerField()),
                ('total_tax', models.IntegerField()),
                ('total_deduction', models.IntegerField()),
                ('total_salary', models.IntegerField()),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Regis_db')),
            ],
        ),
        migrations.AddField(
            model_name='admin_account',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll_admin.admin_model'),
        ),
        migrations.AddField(
            model_name='add_admin_sal',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll_admin.admin_model'),
        ),
    ]
