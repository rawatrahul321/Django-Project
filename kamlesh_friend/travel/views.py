
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from passlib.hash import pbkdf2_sha256



def index(request):
    return render(request, 'index.html', {'price': 1000})
