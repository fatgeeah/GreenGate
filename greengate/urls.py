"""greengate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import  path
from green_gate import views
from django.conf.urls.static import static 
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='home'),
    path('Login/', views.LoginPage,name='login'),
    path('store/', views.StorePage, name='store'),
    path('Register/', views.RegisterPage, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
    path('about/', views.AboutPage, name='about'),
    path('guest/', views.GuestPage, name='guest'),
    path('contact/', views.ContactPage, name='contact'),
    path('help/', views.HelpPage, name='help'),
    path('cart/', views.CartPage, name='cart'),
    path('checkout/', views.CheckoutPage, name='checkout'),
    path('forgotpassword/', views.ForgotPasswordPage, name='forgotpassword'),
    path('changepassword/', views.ChangePasswordPage, name='changepassword'),
] 
urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)

