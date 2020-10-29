from django.contrib import admin
from .models import PrintOrder, CompletedOrder

# Register your models here.
admin.site.register(PrintOrder)
admin.site.register(CompletedOrder)