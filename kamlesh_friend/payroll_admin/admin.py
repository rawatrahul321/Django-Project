from django.contrib import admin

from .models import admin_model,admin_destination, add_department_model, add_designation_model, salary_details, admin_account, \
    add_admin_sal

admin.site.register(admin_model)
admin.site.register(add_department_model)
admin.site.register(add_designation_model)
admin.site.register(salary_details)
admin.site.register(admin_account)
admin.site.register(add_admin_sal)
admin.site.register(admin_destination)

# Register your models here.
