import requests

def send_payment_request(user_id, amount):
    api_url = "https://api.example.com/payment"
    data = {
        "user_id": user_id,
        "amount": amount,
        "description": "Parking fee"
    }
    response = requests.post(api_url, json=data)
    return response.json()

def confirm_payment(transaction_id):
    api_url = f"https://api.razorpay.com/payment/{transaction_id}/status"
    response = requests.get(api_url)
    return response.json()

# Send payment request
payment_response = send_payment_request('user_123', 50)
print(payment_response)

# Confirm payment
payment_confirmation = confirm_payment(payment_response['transaction_id'])
print(payment_confirmation)
