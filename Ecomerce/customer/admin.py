from django.contrib import admin
from .models import A_Customer,Item,Cart

class Customer_AL(admin.ModelAdmin):
    list_display = [
        "customer_name", "date", "email", "password", "contact", "building", "street", "landmark", "city", "state", "pincode", "wallet", "rewards"]
    readonly_fields = ('customerid', "password")


admin.site.register(A_Customer, Customer_AL)
admin.site.register(Item)
admin.site.register(Cart)


# Register your models here.