import Adyen
import json
import time
from .secrets import secrets


# Initialize Adyen client with common settings and return Adyen.Adyen object
def ady_clientInit():
    print("Adyen API is about to be initialized.")

    ady = Adyen.Adyen()
    ady.client.xapikey = secrets()['xapikey']
    ady.client.platform = secrets()['platform']

    # TODO Not in documentation, needed otherwise following error
    #  requests.exceptions.InvalidHeader: Invalid return character or leading space in header: User-Agent
    ady.client.app_name = secrets()['app_name']

    print("Adyen API is initialized.")
    return ady


# Retrieve /paymentMethods via Adyen API
def ady_paymentMethods(country_code, value, currency):
    request = {
        'merchantAccount': secrets()['merchantAccount'],
        'countryCode': country_code,
        'amount': {
            'value': value,
            'currency': currency,
        },
        'channel': 'Web'
    }

    print("/paymentMethods is about to be sent with: \n" + str(request))
    ady = ady_clientInit()
    response = ady.checkout.payment_methods(request)
    print("PaymentMethods collected from Adyen: \n" + str(response))

    return response


# POST /payments via Adyen API
def ady_payments(dropin_data, value, currency):
    # Data from drop_in is converted from string to JSON
    dropin_data = json.loads(dropin_data.body)

    request = {
        'amount': {
            'value': value,
            'currency': currency,
        },
        'reference': 'StoreDemo:' + time.strftime("%Y.%m.%d.%H:%M:%S"),  # no "-" as it's for multiples reference

        # TODO paymentMethod doesn't expect the full dropin_data. It's state.data.paymentMethod
        #  https://docs.adyen.com/checkout/drop-in-web?tab=%23codeBlockBPDnz_py#step-3-make-a-payment
        'paymentMethod': dropin_data['paymentMethod'],
        'returnUrl': secrets()['returnUrl'],
        'merchantAccount': secrets()['merchantAccount'],
    }

    # If shopper is too fast (?), riskData is not available -> try/catch to handle this case
    try:
        request['riskData'] = dropin_data['riskData']
    except:
        print("There's no riskData")

    print("/payments is about to be sent with: \n" + str(request))
    ady = ady_clientInit()
    response = ady.checkout.payments(request)
    print("Payment processed")

    return response


# POST /payments/details via Adyen API
def ady_payments_details(request):
    # request contain is already build in payment_processing page
    request = json.loads(request.body)

    print("/payments/details is about to be sent with: \n" + str(request))
    ady = ady_clientInit()
    response = ady.checkout.payments_details(request)
    print("/payments/details processed: \n" + str(response))

    return response
