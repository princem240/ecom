from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('logout',views.logout),
    path('register',views.register),
    path('view/<int:product_id>',views.view),
    path('filter',views.filter),
    path('search',views.search),
    path('cart',views.ac),
    path('cancel/<int:cart_id>',views.cancel),
    path('contact',views.contact),
    
]
