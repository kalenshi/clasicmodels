from django.contrib import admin

# Register your models here.
from api.models import Customers

app_name = "api"
admin.site.register(Customers)
