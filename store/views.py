from django.shortcuts import render

# Create your views here.
from .models import Categories, Coupons, Roles, Profile, Products

def home_view(request):
    page_data = {
        'page_name': 'home',
        'test': "Siddiq",
    }

    return render(request, 'home.html', page_data)

def about_view(request):
    page_data = {
        'page_name': 'about',
    }
    
    return render(request, 'about.html', page_data)

def services_view(request):
    page_data = {
        'page_name': 'services',
    }
    
    return render(request, 'services.html', page_data)

def products_view(request):
    page_data = {
        'page_name': 'products',
    }
    
    return render(request, 'products.html', page_data)

def product_detail_view(request):
    page_data = {
        'page_name': 'product_detail',
    }
    
    return render(request, 'product_detail.html', page_data)

def contact_view(request):
    page_data = {
        'page_name': 'contact',
    }
    
    return render(request, 'contact.html', page_data)

def login_view(request):
    page_data = {
        'page_name': 'login',
    }
    
    return render(request, 'login.html', page_data)
