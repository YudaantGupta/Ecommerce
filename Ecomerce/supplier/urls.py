from django.urls import path 
from . import views

urlpatterns = [
    path('product' , views.product  , name='product'),
    path('add_orders' , views.add , name='add_orders'),
    path('idthing/<int:id>/' , views.idthing)
]