from django.contrib import admin
from .models import IndieUser
# Register your models here.
admin.site.register(IndieUser)

# class IndieUserAdmin(admin.ModelAdmin):
#     readonly_fields = ('uid')