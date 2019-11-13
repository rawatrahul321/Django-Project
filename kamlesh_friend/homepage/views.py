from django.contrib import messages
from django.shortcuts import render, redirect
from passlib.hash import pbkdf2_sha256

from .models import contactus, Regis_db


def homepage(request):
    return render(request, 'homepage/home.html')


def about(request):
    return render(request, 'homepage/aboutme.html')


def details(request):
    return render(request, 'homepage/module_details.html')


# def contact(request):


# return render(request, 'homepage/contact.html')
def contact(request):
    if request.method == "POST":
        # print(1)
        # reg_form1 = contact_form(request.POST)
        # if reg_form1.is_valid():
        #     print(1)
        #     username = reg_form1.cleaned_data.get('name')
        #     email = reg_form1.cleaned_data.get('email')
        #     mobile = reg_form1.cleaned_data.get('mobile')
        #     subject= reg_form1.cleaned_data.get('subject')
        #     message= reg_form1.cleaned_data.get('message')
        username = request.POST['name']

        email = request.POST['email']
        mobile = request.POST['mobile']
        subject = request.POST['subject']
        message = request.POST['message']
        reg_db_obj = contactus()
        reg_db_obj.name = username
        reg_db_obj.email = email
        reg_db_obj.mobile = mobile
        reg_db_obj.subject = subject
        reg_db_obj.message = message
        reg_db_obj.save()
        return redirect('homepageurl:homepage')
    return render(request, 'homepage/contact.html')

def log_in(request):
    if 'u' in request.session:
        u = request.session['u']

        return redirect('empurl:employee')


    elif request.method == 'POST':

        u = request.POST["username"]
        p = request.POST["password"]
        obj = len(Regis_db.objects.filter(password=p))

        if (len(Regis_db.objects.filter(username=u)) and obj):
            request.session['u'] = u

            return render(request, 'employee/emp.html')
        else:
            messages.warning(request, 'username or password wrong')

    return render(request, 'homepage/log_in_employee.html')


def sign_up(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # enc_pass = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=32)
        password_confirm = request.POST['password_confirm']
        reg_db_obj = Regis_db()
        reg_db_obj.firstname = firstname
        reg_db_obj.lastname = lastname
        reg_db_obj.username = username
        reg_db_obj.email = email
        reg_db_obj.password = password
        reg_db_obj.password_confirm = password_confirm
        print(3)

        if (Regis_db.objects.filter(username=username).exists()):
            messages.warning(request, 'username or email already exist')
            return render(request, 'homepage/register.html')

        elif (Regis_db.objects.filter(email=email).exists()):
            print(2)
            messages.warning(request, 'username or email already exist')
            return render(request, 'homepage/register.html')
        else:

            reg_db_obj.save()

            return redirect('homepageurl:loginme')
    return render(request, 'homepage/register.html')
