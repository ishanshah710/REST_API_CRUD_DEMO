from django.contrib import admin
from .models import Language
# Register your models here.

class UpdateAdmin(admin.ModelAdmin):
    list_display = ['pk','__str__']

admin.site.register(Language , UpdateAdmin)
