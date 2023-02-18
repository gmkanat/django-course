from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html', context={
        "items": [
            {
                "name": "Nike Air Max Sneakers",
                "price": 7990,
                "description": "Classic running shoes with visible air cushioning and stylish design."
            },
            {
                "name": "Adidas Ultra Boost Running Shoes",
                "price": 8990,
                "description": "Lightweight and responsive running shoes with advanced Boost technology."
            },
            {
                "name": "Under Armour Sports T-shirt",
                "price": 1890,
                "description": "Moisture-wicking and breathable t-shirt for maximum comfort during workouts."
            },
            {
                "name": "Puma Fenty Sweatshirt",
                "price": 4990,
                "description": "Cozy and stylish sweatshirt designed in collaboration with Rihanna's Fenty label."
            },
            {
                "name": "New Balance 990v5 Sneakers",
                "price": 9990,
                "description": "Premium quality sneakers with excellent support and cushioning for everyday wear."
            },
            {
                "name": "Reebok Classic Leather Shoes",
                "price": 6490,
                "description": "Iconic sneakers with a timeless design and durable leather construction."
            }
        ]
    })


def users_email_verification(request):
    return render(request, 'users/email_verification.html')


def users_login(request):
    return render(request, 'users/login.html')


def users_register(request):
    return render(request, 'users/register.html')


def users_profile(request):
    return render(request, 'users/profile.html')


def orders(request):
    return render(request, 'orders/orders.html')


def order(request):
    return render(request, 'orders/order.html')


def orders_create(request):
    return render(request, 'orders/order-create.html')


def orders_success(request):
    return render(request, 'orders/success.html')
