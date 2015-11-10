from django.contrib import admin

# Register your models here.
from .models import Company,Provider,Services

admin.site.register(Company)
admin.site.register(Provider)
admin.site.register(Services)
