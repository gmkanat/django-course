from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('users/email_verification', views.users_email_verification, name='users_email_verification'),
    path('users/login', views.users_login, name='users_login'),
    path('users/register', views.users_register, name='users_register'),
    path('users/profile', views.users_profile, name='users_profile'),
    path('orders/', views.orders, name='orders'),
    path('order/', views.order, name='order'),
    path('orders/create', views.orders_create, name='order-create'),
    path('orders/success', views.orders_success, name='orders_success'),

]
