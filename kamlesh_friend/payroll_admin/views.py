from django.contrib import messages
from django.shortcuts import render, redirect

from employee.models import emp_account
from .models import admin_destination
from homepage.models import Regis_db
from .models import admin_model,admin_destination, add_department_model, add_designation_model, salary_details, admin_account, \
    add_admin_sal






def admin_payroll(request):
    if 'admin_username' in request.session:
        admin_username = request.session['admin_username']
        return redirect('payrollurl:admin_about')
    elif request.method == 'POST':
        admin_username = request.POST["admin_username"]
        p = request.POST["admin_password"]

        if (len(admin_model.objects.filter(admin_username=admin_username)) and admin_model.objects.filter(admin_password=p)):
            request.session['admin_username'] = admin_username
            print("admin session start")
            return redirect('payrollurl:admin_about')
        else:
            messages.warning(request, 'Username Or Password Wrong')

    return render(request, 'payroll_admin/payroll_login.html')


def admin_about(request):
    return render(request, 'payroll_admin/admin_about.html')


def add_department(request):
    if request.method == "POST":
        add_department = request.POST['add_department']
        description = request.POST['description']

        reg_db_obj = add_department_model()
        reg_db_obj.add_department = add_department
        reg_db_obj.description = description

        reg_db_obj.save()
        messages.success(request, 'Department add successfully')

        return redirect('payrollurl:add_depart')
    return render(request, 'payroll_admin/admin_department.html')


def add_designation(request):
    if request.method == "POST":
        add_designation = request.POST['add_designation']
        description = request.POST['description']

        reg_db_obj = add_designation_model()
        reg_db_obj.add_designation = add_designation
        reg_db_obj.description = description
        reg_db_obj.save()
        messages.success(request, 'Designation add successfully')

        return redirect('payrollurl:add_design')
    return render(request, 'payroll_admin/add_designation.html')


# Create your views here.
def add_salary(request):
    e = emp_account.objects.all()
    r=Regis_db.objects.all()
    print(e)
    if request.method == "POST":
        emp_name = request.POST['emp_name']
        user_name=request.POST['user_name']
        mp = request.POST['mp']
        working_days = request.POST['working_days']
        bs = request.POST['bs']
        house_rent = request.POST['house_rent']
        mediclaim = request.POST['mediclaim']
        travel = request.POST['travel']
        dearness = request.POST['dearness']
        reimburement = request.POST['reimburement']
        conveyance = request.POST['conveyance']
        other_salary = request.POST['other_salary']
        year_salary = request.POST['year_salary']
        provident_fund = request.POST['provident_fund']
        total_tax = request.POST['total_tax']
        total_deduction = request.POST['total_deduction']
        total_salary = request.POST['total_salary']

        sal_obj = salary_details()
        sal_obj.emp_name = emp_name
        sal_obj.mp = mp
        sal_obj.working_days = working_days
        sal_obj.bs = bs
        sal_obj.house_rent = house_rent
        sal_obj.mediclaim = mediclaim
        sal_obj.travel = travel
        sal_obj.dearness = dearness
        sal_obj.reimburement = reimburement
        sal_obj.conveyance = conveyance
        sal_obj.other_salary = other_salary
        sal_obj.year_salary = year_salary
        sal_obj.provident_fund = provident_fund
        sal_obj.total_tax = total_tax
        sal_obj.total_deduction = total_deduction
        sal_obj.total_salary = total_salary

        sal_obj.user_name_id = user_name
        print(sal_obj.user_name_id)
        sal_obj.save()
        messages.success(request, 'saved')
        return redirect('payrollurl:add_salary')

    return render(request, 'payroll_admin/add_salary.html', {'data': e,'emp':r})


def admin_report(request):
    e = admin_account.objects.all()
    return render(request, 'payroll_admin/admin_report.html', {'data': e})


def delete_admin(request, x):
    e = admin_account.objects.filter(user_name_id=x)
    e.delete()
    return redirect('payrollurl:admin_report')


def department_report(request):
    obj = add_department_model.objects.all()
    return render(request, 'payroll_admin/department_report.html', {'data': obj})


def designation_report(request):
    obj = add_designation_model.objects.all()
    return render(request, 'payroll_admin/designation_report.html', {'data': obj})


def employee_report(request):
    obj = emp_account.objects.all()
    obj1 = Regis_db.objects.all()
    return render(request, 'payroll_admin/employee_report.html', {'data': obj, 'data1': obj1})


def salary_report(request):
    obj1 = salary_details.objects.all()
    obj2 = add_admin_sal.objects.all()

    return render(request, 'payroll_admin/salary_report.html', {'data1': obj1, 'data2': obj2})


def salaryedit(request, x, y):
    e = salary_details.objects.filter(id=x)
    a = emp_account.objects.filter(user_name_id=y)

    return render(request, 'payroll_admin/view_salary_admin.html', {'admin': e, 'sal': a})


def admin_account_info(request):
    s = admin_model.objects.filter(admin_username=request.session['admin_username'])
    e = admin_account.objects.filter(
        user_name=admin_model.objects.filter(admin_username=request.session['admin_username']))

    if request.method == "POST":
        department = request.POST['department']
        designation = request.POST['designation']
        gender = request.POST['gender']
        fullname = request.POST['fullname']
        mobile = request.POST['mobile']
        bday = request.POST['bday']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        city = request.POST['city']
        state = request.POST["state"]
        country = request.POST['country']
        account = request.POST['account']
        bank = request.POST['bank']
        email = request.POST['email']
        pfaccount = request.POST['pfaccount']
        joining_date = request.POST['joining_date']
        emp_obj = admin_account(filename=request.FILES['filename'])
        emp_obj.department = department
        emp_obj.designation = designation
        emp_obj.gender = gender
        emp_obj.mobile = mobile
        emp_obj.add1 = add1
        emp_obj.bday = bday
        emp_obj.add2 = add2
        emp_obj.city = city
        emp_obj.email = email
        emp_obj.fullname = fullname
        emp_obj.state = state
        emp_obj.country = country
        emp_obj.account = account
        emp_obj.bank = bank
        emp_obj.pfaccount = pfaccount
        emp_obj.joining_date = joining_date
        print(request.session['admin_username'])
        emp_obj.user_name = admin_model.objects.get(admin_username=request.session['admin_username'])
        emp_obj.save()

        messages.success(request, 'saved')
        return render(request, 'payroll_admin/admin_account.html')

    return render(request, 'payroll_admin/admin_account.html', {'data': s, 'data1': e})


# def edit_admin(request,x):
#
#     return redirect('payrollurl:admin_account',{'data':e})


def admin_salary(request):
    obj2 = add_admin_sal.objects.filter(
        user_name=admin_model.objects.filter(admin_username=request.session['admin_username']))
    return render(request, 'payroll_admin/admin_salary.html', {'data': obj2})


def admin_view_details(request):
    s = admin_model.objects.filter(admin_username=request.session['admin_username'])
    e = admin_account.objects.filter(
        user_name=admin_model.objects.filter(admin_username=request.session['admin_username']))
    print(e)

    return render(request, 'payroll_admin/admin_view_details.html', {'data': e, 'data1': s})


def admin_admin_salary(request):
    user_name_id = admin_model.objects.filter(admin_username=request.session['admin_username'])
    print(user_name_id)

    e = admin_account.objects.filter(
        user_name=admin_model.objects.filter(admin_username=request.session['admin_username']))
    if request.method == "POST":
        emp_name = request.POST['emp_name']
        mp = request.POST['mp']
        working_days = request.POST['working_days']
        bs = request.POST['bs']
        house_rent = request.POST['house_rent']
        mediclaim = request.POST['mediclaim']
        travel = request.POST['travel']
        dearness = request.POST['dearness']
        reimburement = request.POST['reimburement']
        conveyance = request.POST['conveyance']
        other_salary = request.POST['other_salary']
        year_salary = request.POST['year_salary']
        provident_fund = request.POST['provident_fund']
        total_tax = request.POST['total_tax']
        total_deduction = request.POST['total_deduction']
        total_salary = request.POST['total_salary']

        sal_obj = add_admin_sal()
        sal_obj.admin_name = emp_name
        sal_obj.mp = mp
        sal_obj.working_days = working_days
        sal_obj.bs = bs
        sal_obj.house_rent = house_rent
        sal_obj.mediclaim = mediclaim
        sal_obj.travel = travel
        sal_obj.dearness = dearness
        sal_obj.reimburement = reimburement
        sal_obj.conveyance = conveyance
        sal_obj.other_salary = other_salary
        sal_obj.year_salary = year_salary
        sal_obj.provident_fund = provident_fund
        sal_obj.total_tax = total_tax
        sal_obj.total_deduction = total_deduction
        sal_obj.total_salary = total_salary
        sal_obj.user_name_id = admin_model.objects.filter(admin_username=request.session['admin_username'])

        sal_obj.save()
        messages.success(request, 'saved')
        return redirect('payrollurl:admin_admin_salary')

    return render(request, 'payroll_admin/add_admin_salary.html', {'data': e})


def delete(request, x):
    e = add_admin_sal.objects.filter(id=x)
    e.delete()
    return redirect('payrollurl:admin_salary')


def salary_delete(request, x):
    e = salary_details.objects.filter(id=x)
    e.delete()

    return redirect('payrollurl:salary_report')


def delete_salary_admin(request, x):
    e = add_admin_sal.objects.filter(id=x)
    e.delete()
    return redirect('payrollurl:salary_report')


def delete_department(request, x):
    e = add_department_model.objects.filter(id=x)
    e.delete()
    return redirect('payrollurl:department_report')


def delete_designation(request, x):
    e = add_designation_model.objects.filter(id=x)
    e.delete()
    return redirect('payrollurl:designation_report')


def delete_emp(request, x):
    e = emp_account.objects.filter(user_name_id=x)
    e.delete()
    return redirect('payrollurl:employee_report')


def view_salary_admin(request, x):
    a = add_admin_sal.objects.filter(id=x)
    s = admin_account.objects.filter(
        user_name=admin_model.objects.filter(admin_username=request.session['admin_username']))

    return render(request, 'payroll_admin/view_salary_admin.html', {'admin': a, 'sal': s})


def admin_destination_data(request):
    dests = admin_destination.objects.all()
    


    return render(request, 'payroll_admin/admin_destination.html', {'dests':dests})
