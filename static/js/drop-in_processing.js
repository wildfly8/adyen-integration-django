// TODO Adyen doc is unclear on this for Python example
//  https://docs.adyen.com/checkout/drop-in-web?tab=%23codeBlocklimds_py#step-5-additional-payment-details

const request = {
    'details': JSON.parse(JSON.parse(document.getElementById('ady_details').textContent)),
    'paymentData': localStorage.getItem('paymentData')
}

console.log("Fetch the Payments details API")

fetch('/ady_API/payments_details/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(request)
})
    .then(response => response.json())
    .then(response => actionState(response))