# main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Payment


def process_payment(request, unique_id):
    payment = get_object_or_404(
        Payment, payment_link=f"http://yourdomain.com/payment/{unique_id}")
    if request.method == 'POST':
        # Process the payment here (integrate with a payment gateway)
        # For example, updating the payment status to 'completed' after successful payment
        payment.status = 'completed'
        payment.save()
        return HttpResponse("Payment successful")
    return render(request, 'main/payment_form.html', {'payment': payment})
