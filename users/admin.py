# Register your models here.
from django.contrib import admin
from users.models import CustomUser

admin.site.register(CustomUser)
