from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from homepage.models import Regis_db
from payroll_admin.models import salary_details
from .models import emp_account


# Create your views here.


def employee_details(request):
    # u = None
    # if (request.method == "GET"):
    #
    #     if 'action' in request.GET:
    #         print(1)
    #         action = request.GET.get('action')
    #         if action == 'logout':
    #             if request.session.has_key('u'):
    #                 request.session.flush()
    #                 return render(request, 'homepage/log_in_employee.html')
    #                 # return HttpResponseRedirect('session')

    return render(request, 'employee/emp.html')


#

#
def change_password(request):
    if request.method == 'POST':
        print(1)
        password = request.POST['password']
        # enc_pass = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)

        s = Regis_db.objects.get(username=request.session['u'])

        s.password = password
        s.save()
        update_session_auth_hash(request, s)

        messages.success(request, 'Your password was successfully updated!')
        # return redirect('homepageurl:loginme')

    return render(request, 'employee/change_password.html')


def about(request):
    return render(request, 'employee/aboutme.html')


def emp_details(request):
    s = Regis_db.objects.filter(username=request.session['u'])

    if request.method == "POST":
        department = request.POST['department']
        designation = request.POST['designation']
        gender = request.POST['gender']
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        bday = request.POST['bday']
        add1 = request.POST['add1']
        email = request.POST['email']
        add2 = request.POST['add2']
        city = request.POST['city']
        state = request.POST["state"]
        country = request.POST['country']
        account = request.POST['account']
        bank = request.POST['bank']
        pfaccount = request.POST['pfaccount']
        joining_date = request.POST['joining_date']

        emp_obj = emp_account(filename=request.FILES['filename'])
        emp_obj.department = department
        emp_obj.designation = designation
        emp_obj.gender = gender
        emp_obj.mobile = mobile
        emp_obj.add1 = add1
        emp_obj.bday = bday
        emp_obj.add2 = add2
        emp_obj.city = city
        emp_obj.fullname = fullname
        emp_obj.state = state
        emp_obj.country = country
        emp_obj.email = email
        emp_obj.account = account
        emp_obj.bank = bank
        emp_obj.pfaccount = pfaccount
        emp_obj.joining_date = joining_date

        emp_obj.user_name_id = Regis_db.objects.filter(username=request.session['u'])[0].id

        emp_obj.save()

        messages.success(request, 'saved')
        return render(request, 'employee/emp_management.html')

    return render(request, 'employee/emp_management.html', {'data': s})


def salary_detail(request, x=-1):
    e = salary_details.objects.filter(user_name=Regis_db.objects.filter(username=request.session['u'])[0].id)
    print(e)
    return render(request, 'employee/salary_details.html', {'data': e})


#
# def logout(request):
#     auth.logout(request)
#     return render(request, 'employee/emp_logout.html')


def view_details(request):
    e = emp_account.objects.filter(user_name=Regis_db.objects.filter(username=request.session['u'])[0].id)

    s = Regis_db.objects.filter(username=request.session['u'])

    return render(request, 'employee/view_details.html', {'data': e, 'data1': s})


def view_salary(request, x):
    e = salary_details.objects.filter(id=x)
    obj = emp_account.objects.filter(user_name=Regis_db.objects.filter(username=request.session['u'])[0].id)

    return render(request, 'employee/view_salary.html', {"sal": e, 'emp': obj})


def delete_data(request, x):
    e = salary_details.objects.filter(id=x)
    e.delete()
    return redirect('empurl:salary_details')
