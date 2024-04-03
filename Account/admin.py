from django.contrib import admin

# Register your models here.

from .models import Amount, Profile

admin.site.register(Amount)
admin.site.register(Profile)
