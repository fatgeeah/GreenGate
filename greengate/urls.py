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
    path('accounts/login/', views.LoginPage,name='login'),
    path('store/', views.StorePage, name='store'),
    path('Register/', views.RegisterPage, name='register'),
    path('logout/', views.LogoutPage, name='logout'),
    path('about/', views.AboutPage, name='about'),
    path('guest/', views.GuestPage, name='guest'), 
    path('contact/', views.ContactPage, name='contact'),
    path('help/', views.HelpPage, name='help'),
    path('cart/', views.CartPage, name='cart'),
    path('checkout/', views.CheckoutPage, name='checkout'),
    path('payment/', views.PayPage, name='payment'),

    path('password_reset/',
          auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),
            name="reset_password"),

    path('password_reset_sent/',
          auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
            name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
          name="password_reset_confirm"),
 
    path('password_complete/',\
          auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
          name="password_reset_complete"),

] 
urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)

