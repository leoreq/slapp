from django.contrib import admin

# Register your models here.
from .models import Company,Provider,Services

admin.site.register(Company)
admin.site.register(Provider)
admin.site.register(Services)


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name_plural = 'company'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (CompanyInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)