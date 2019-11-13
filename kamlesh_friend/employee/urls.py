from django.conf.urls import url
from django.contrib.auth import views as auth_views

from employee import views

urlpatterns = [
    url(r'^$', views.employee_details, name='employee'),
    url(r'^about$', views.about, name='abouturl'),
    url(r'^employee/details$', views.emp_details, name='emp_details'),
    url(r'^employee/salary/$', views.salary_detail, name='salary_details'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^view_details$', views.view_details, name='view_details'),
    url(r'^change_password$', views.change_password, name='change_password'),
    url(r'^view_salary/(?P<x>\d+)/$', views.view_salary, name='view_salary'),
    url(r'^delete_data/(?P<x>\d+)/$', views.delete_data, name='delete_data'),
]
