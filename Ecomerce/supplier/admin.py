from django.contrib import admin
from .models import Product

class Name(admin.ModelAdmin):
    list_display = [
       "name","price","amount","disc","date","description","inStock"]
    # readonly_fields = ('customerid', "password")


admin.site.register(Product, Name)
# Register your models here.
