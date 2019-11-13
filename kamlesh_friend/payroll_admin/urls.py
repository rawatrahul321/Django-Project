from django.conf.urls import url

from payroll_admin import views

urlpatterns = [
    url(r'^$', views.admin_payroll, name='payroll_login'),
    url(r'^about_admin$', views.admin_about, name='admin_about'),
    url(r'^add_department$', views.add_department, name='add_depart'),
    url(r'^admin_destination$', views.admin_destination_data, name='admin_destination'),
    # url(r'^edit_depart/(?P<x>\d+)/$', views.edit_depart,name='edit_depart'),

    url(r'^add_designation$', views.add_designation, name='add_design'),
    url(r'^add_salary$', views.add_salary, name='add_salary'),
    url(r'^admin_report$', views.admin_report, name='admin_report'),
    url(r'^department_report$', views.department_report, name='department_report'),
    url(r'^designation_report$', views.designation_report, name='designation_report'),
    url(r'^employee_report$', views.employee_report, name='employee_report'),
    url(r'^salary_report$', views.salary_report, name='salary_report'),
    url(r'^salaryedit/(?P<x>\d+)/(?P<y>\d+)$', views.salaryedit, name='salaryedit'),

    url(r'^admin_account$', views.admin_account_info, name='admin_account'),
    url(r'^admin_salary$', views.admin_salary, name='admin_salary'),
    url(r'^admin_view_details$', views.admin_view_details, name='admin_view_details'),
    url(r'^admin_admin_salary$', views.admin_admin_salary, name='admin_admin_salary'),
    url(r'^delete/(?P<x>\d+)/$', views.delete, name='delete'),
    url(r'^view_salary_admin/(?P<x>\d+)/$', views.view_salary_admin, name='view_salary_admin'),
    url(r'^delete_admin/(?P<x>\d+)/$', views.delete_admin, name='delete_admin'),
    url(r'^salary_delete/(?P<x>\d+)/$', views.salary_delete, name='salary_delete'),
    url(r'^delete_salary_admin/(?P<x>\d+)/$', views.delete_salary_admin, name='delete_salary_admin'),
    url(r'^delete_department/(?P<x>\d+)/$', views.delete_department, name='delete_department'),
    url(r'^delete_designation/(?P<x>\d+)/$', views.delete_designation, name='delete_designation'),
    url(r'^delete_emp/(?P<x>\d+)/$', views.delete_emp, name='delete_emp'),
    # url(r'^edit_admin/(?P<x>\d+)/$', views.edit_admin,name='edit_admin'),

]
