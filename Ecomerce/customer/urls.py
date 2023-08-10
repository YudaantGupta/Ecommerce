from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.login,name = 'login'),
    path('signup' , views.signup , name='signup'),
    path('create_account' , views.create_account , name='create_account'),
    path('home_page' , views.home_page , name='home_page'),
    path('cart' , views.cart , name='cart'),
    path('profile' , views.profile , name = "profile"),
    path('search',views.search,name="search"),
    path('checkout',views.checkout,name="checkout")
]
