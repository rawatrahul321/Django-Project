from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index')
    # url(r'^about$', views.about, name='abouturl'),
    # url(r'^details$', views.details, name='module_details'),
    # url(r'^contact$', views.contact, name='contact_me'),
    # url(r'^loginme/$', views.log_in, name='loginme'),
    # # url(r'^login/$', auth_views.login, {'template_name': 'homepage/log_in_employee.html'}, name='login'),
    # url(r'^signup$', views.sign_up, name='signupme'),
]
