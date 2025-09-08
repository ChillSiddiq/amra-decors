from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from .models import Categories, Coupons, Roles, Profile, Products

def home_view(request):
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'home',
        'categories': categories,
    }

    return render(request, 'home.html', page_data)

def about_view(request):
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'about',
        'categories': categories,
    }
    
    return render(request, 'about.html', page_data)

def services_view(request):
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'services',
        'categories': categories,
    }
    
    return render(request, 'services.html', page_data)

def products_view(request, slug=''):
    if slug:
        category = Categories.objects.filter(slug=slug)
        products = Products.objects.filter(categories__in=category)
    else:
        products = Products.objects.filter(active=True)
    
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'products',
        'products': products,
        'categories': categories,
    }
    
    return render(request, 'products.html', page_data)

def product_detail_view(request, id=''):
    categories = Categories.objects.filter(active=True)

    if id:
        product = Products.objects.get(id=id)
        print(product.name)
    else:
        return redirect('home')

    page_data = {
        'page_name': 'product-detail',
        'product': product,
        'categories': categories,
    }
    
    return render(request, 'product-detail.html', page_data)

def contact_view(request):
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'contact',
        'categories': categories,
    }
    
    return render(request, 'contact.html', page_data)

def login_view(request):
    categories = Categories.objects.filter(active=True)

    page_data = {
        'page_name': 'login',
        'categories': categories,
    }
    
    return render(request, 'login.html', page_data)

def custom_404_view(request, exception):
    categories = Categories.objects.filter(active=True)
    
    page_data = {
        'page_name': '404',
        'categories': categories,
    }
    
    return render(request, '404.html', page_data, status=404)
