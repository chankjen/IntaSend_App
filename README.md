# IntaSend_App
PLP Academy Practice 


# Integrating IntaSend API in a Django Project

This guide explains the importance of integrating the **IntaSend API** into a Django project and provides a step-by-step explanation of how to set it up. IntaSend is a payment gateway that allows businesses to accept payments seamlessly, making it an excellent choice for e-commerce platforms, subscription services, or any application requiring payment processing.

---

## **Why Integrate IntaSend API in a Django Project?**

1. **Seamless Payment Processing**:
   - IntaSend provides a simple and secure way to handle payments, including mobile money, card payments, and bank transfers.
   - It supports multiple currencies, making it ideal for businesses operating in global markets.

2. **Enhanced User Experience**:
   - By integrating IntaSend, you can offer a smooth and fast checkout experience for your users, reducing cart abandonment rates.

3. **Security and Compliance**:
   - IntaSend is PCI-DSS compliant, ensuring that sensitive payment data is handled securely.
   - It uses tokenization and encryption to protect user information.

4. **Real-Time Notifications**:
   - IntaSend provides webhooks for real-time payment notifications, allowing you to update your system immediately when a payment is completed or fails.

5. **Scalability**:
   - IntaSend is designed to handle high transaction volumes, making it suitable for growing businesses.

6. **Developer-Friendly**:
   - IntaSend offers a well-documented API and SDKs, making it easy to integrate into Django projects.

---

## **Requirements**

To integrate IntaSend API into your Django project, you need the following dependencies:

### **Dependencies**
Create a `requirements.txt` file with the following packages:

```plaintext
Django==4.2.7
requests==2.31.0
django-environ==0.11.2
python-dotenv==1.0.0
```

- **Django**: The web framework used to build the project.
- **requests**: A Python library for making HTTP requests to the IntaSend API.
- **django-environ**: A library for managing environment variables in Django.
- **python-dotenv**: A library to load environment variables from a `.env` file.

---

## **Steps to Integrate IntaSend API in Django**

### **1. Set Up Your Django Project**
If you haven't already, create a Django project and app:

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp payments
```

Add the `payments` app to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'payments',
]
```

### **2. Install Dependencies**
Install the required packages:

```bash
pip install -r requirements.txt
```

### **3. Configure Environment Variables**
Create a `.env` file in the root of your project to store sensitive information like your IntaSend API keys:

```plaintext
INTA_SEND_PUBLIC_KEY=ISPubKey_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
INTA_SEND_SECRET_KEY=ISSecretKey_test_xxxxxxxxxxxxxxxxxxxxxxxx
```

Load the environment variables in `settings.py`:

```python
import environ

env = environ.Env()
environ.Env.read_env()

INTA_SEND_PUBLIC_KEY = env('INTA_SEND_PUBLIC_KEY')
INTA_SEND_SECRET_KEY = env('INTA_SEND_SECRET_KEY')
```

### **4. Create a Payment View**
In `payments/views.py`, create a view to handle payments using the IntaSend API:

```python
import requests
from django.http import JsonResponse
from django.conf import settings

def initiate_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')

        url = 'https://sandbox.intasend.com/api/v1/payment/'
        headers = {
            'Authorization': f'Bearer {settings.INTA_SEND_SECRET_KEY}',
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
```

### **5. Configure URLs**
In `payments/urls.py`, add a URL pattern for the payment view:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
]
```

Include the `payments` app URLs in the main `urls.py`:

```python
from django.urls import include, path

urlpatterns = [
    ...
    path('payments/', include('payments.urls')),
]
```

### **6. Test the Integration**
Run the Django development server:

```bash
python manage.py runserver
```

Use a tool like Postman or a frontend form to send a POST request to `http://127.0.0.1:8000/payments/initiate-payment/` with the following payload:

```json
{
    "amount": "10",
    "currency": "KES"
}
```

---

## **Conclusion**

Integrating the IntaSend API into your Django project enables you to handle payments securely and efficiently. By following the steps above, you can set up a payment system that enhances user experience, ensures security, and scales with your business. With IntaSend, you can focus on growing your business while leaving the complexities of payment processing to a reliable platform.

For more details, refer to the [IntaSend API Documentation](https://developers.intasend.com/).
