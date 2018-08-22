from django.contrib import admin

# Register your models here.

from .models import Image , Temp_User

admin.site.register(Image)
admin.site.register(Temp_User)
