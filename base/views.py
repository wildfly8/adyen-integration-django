from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .ady_API import *
from .secrets import secrets
import json

# Fixed variables
value = 1500
currency = "EUR"

# Default views - Redirect to the next page
def index(request):
    return HttpResponseRedirect("/country/")


# Simple pre-checkout pages
def country(request):
    return render(request, 'base/country.html')

def cart(request):
    return render(request, 'base/cart.html')


## API

# /payments API implementation
def ady_api_payments(request):
    if request.method == 'POST':
        requestData = ady_payments(request, value, currency)
        return JsonResponse(requestData.message)
    else:
        return HttpResponseNotFound('<p>Incorrect data</p>')


# /payments API implementation
def ady_api_payments_details(request):
    if request.method == 'POST':
        requestData = ady_payments_details(request)
        return JsonResponse(requestData.message)
    else:
        return HttpResponseNotFound('<p>Incorrect data</p>')


## CHECKOUT EXPERIENCE

# Present Adyen Drop-in
def payment_checkout(request, country_code):
    return render(request, 'base/payment_checkout.html', context=
    {
        'paymentMethods': ady_paymentMethods(country_code, value, currency).message,
        'originKey': secrets()['originKey'],
    })


# Parse and process the return URL from Adyen
def payment_processing(request):
    if request.method == "GET":
        details = json.dumps(request.GET)
    elif request.method == "POST":
        details = json.dumps(request.POST)
    else:
        return 0  # neither a GET or a POST

    return render(request, 'base/payment_processing.html', context=
    {
        'ady_details': details,
    })


# Result pages
def payment_success(request):
    return render(request, 'base/payment_success.html')


def payment_pending(request):
    return render(request, 'base/payment_pending.html')


def payment_error(request, reason):
    return render(request, 'base/payment_error.html', context={
        'reason': reason,
    })

