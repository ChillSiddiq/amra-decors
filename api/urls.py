"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from store.views import *
# from store.views import CategoriesViewSet, CouponsViewSet, RolesViewSet, ProfileViewSet, ProductsViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoriesViewSet)
# router.register(r'coupons', CouponsViewSet)
# router.register(r'roles', RolesViewSet)
# router.register(r'profiles', ProfileViewSet)
# router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('products/', products_view, name='products'),
    path('product-detail/', product_detail_view, name='product-detail'),
    path('contact/', contact_view, name='contact'),
    # path('api/', include(router.urls)),
    path('api/login/', obtain_auth_token, name='api_token_auth'),  # 🔐 Login route
    path('admin/', admin.site.urls),
]

