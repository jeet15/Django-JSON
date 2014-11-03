from django.contrib import admin

# Register your models here.
from models import Car

class CarAdmin(admin.ModelAdmin):
    fields = ('name', 'image')

admin.site.register(Car, CarAdmin)