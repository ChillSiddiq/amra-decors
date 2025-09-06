from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Categories, Coupons, Roles, Profile, Products
from .serializers import CategoriesSerializer, CouponsSerializer, RolesSerializer, ProfileSerializer, ProductsSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CouponsViewSet(viewsets.ModelViewSet):
    queryset = Coupons.objects.all()
    serializer_class = CouponsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user', 'role').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Optionally, restrict profiles so users only see their own or admins see all
        user = self.request.user
        if user.is_staff:
            return Profile.objects.all()
        return Profile.objects.filter(user=user)

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def home_view(request):
    page_data = {
        'page_name': 'home',
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
