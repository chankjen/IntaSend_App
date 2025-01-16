from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


import requests
from django.http import JsonResponse

def make_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        api_key = 'ISPubKey_test_ee5f4860-80fb-4670-a8ef-3258658af886'
        url = 'https://sandbox.intasend.com/api/v1/payment/'

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        data = {
            'amount': amount,
            'currency': currency,
            'email': 'customer@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '254712345678'
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return JsonResponse(response.json(), status=200)
        else:
            return JsonResponse({'error': 'Payment failed'}, status=400)