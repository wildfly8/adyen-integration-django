// Handle action.state from Adyen API
// Is included in /payment/checkout and /payment/processing

const actionState = (response) => {
    console.log("API call done. Action: " + response.resultCode)
    if (response.action) {
        console.log("An action key is present.")

        // Save action.paymentData for future use in payment_processing
        if (response.resultCode === 'RedirectShopper') {
            localStorage.setItem('paymentData', response.action.paymentData);
        }

        // Drop-in handles the action object from the /payments response
        dropin.handleAction(response.action);

    } else {
        console.log("No more action needed. Status: " + response.resultCode)

        // The following can be tested with this list of Card holderNames
        // https://docs.adyen.com/development-resources/test-cards/result-code-testing/adyen-response-codes
        if (response.resultCode === "Authorised") {
            // dropin.setStatus('success', { message: 'Payment successful!' }); - If we wanted to use the drop-in confirmation instead
            window.location.href = "/payment/success/"

        } else if (response.resultCode === "Pending" || response.resultCode === "Received") {
            window.location.href = "/payment/pending/"

        /* For test purpose, we'll show the refusalError to the client in case of Refused
        } else if (response.resultCode === "Refused") {
            window.location.href = "/payment/error/" + "Refused"
         */

        } else if (response.resultCode === "Error" || response.resultCode === "Refused") {
            if (response['refusalReason']) {
                window.location.href = "/payment/error/" + response['refusalReason']
            } else {
                window.location.href = "/payment/error/" + "No refusalReason"
            }
        } else {
            // "PresentToShopper" is not handled in this example
            window.location.href = "/payment/error/" + "Unknown resultCode"

        }
    }
}