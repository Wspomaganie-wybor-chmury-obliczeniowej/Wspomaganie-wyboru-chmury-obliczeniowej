from django.contrib import admin

# Register your models here.
from .models import Cloud, Client

admin.site.register(Cloud)
admin.site.register(Client)