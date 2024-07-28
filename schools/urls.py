# main/urls.py
from django.urls import path
from .views import process_payment

urlpatterns = [
    path('payment/<str:unique_id>/', process_payment, name='process_payment'),
]
