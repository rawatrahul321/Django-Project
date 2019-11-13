from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [   url(' ', include('travel.urls',namespace='index')),
                  url(r'^admin/', admin.site.urls),

                  url(r'^', include('homepage.urls', namespace='homepageurl')),
                  url(r'^employee/', include('employee.urls', namespace='empurl')),
                  url(r'^payroll_admin/', include('payroll_admin.urls', namespace='payrollurl')),

                  url('^', include('django.contrib.auth.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
