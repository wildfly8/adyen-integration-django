from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('country/', views.country, name="country"),
    path('cart/', views.cart, name="cart"),

    path('payment/checkout/<str:country_code>', views.payment_checkout, name="payment_checkout"),
    path('payment/processing/', views.payment_processing, name="payment_processing"),
    path('payment/success/', views.payment_success, name="payment_success"),
    path('payment/pending/', views.payment_pending, name="payment_pending"),
    path('payment/error/<str:reason>', views.payment_error, name="payment_error"),

    path('ady_API/payments/', views.ady_api_payments, name="ady_api_payments"),
    path('ady_API/payments_details/', views.ady_api_payments_details, name="ady_api_payments_details"),

]
