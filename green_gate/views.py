from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def HomePage(request):
    return render (request, 'index.html')

def AboutPage(request):
    return render (request, 'About.html')

def GuestPage(request):
    return render (request, 'Guest.html')


def ContactPage(request):
    if request.method =="POST":
        fname = request.POST.get('first-name')
        lname = request.POST.get('last-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'First name' :fname,
            'Last name' :lname,
            'email' :email,
            'subject' : subject,
            'message' : message
        }
        message = '''
        New message: {}

        From {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'], message, '',['fatgeeahminkis@gmail.com'])
        return HttpResponse('Your email has successfully been sent !')
    return render (request, 'Contact.html',)

def CartPage(request):
          context={}
          if request.user.is_authenticated:
           customer = request.user.customer
           order, created = Order.objects.get_or_create(customer=customer, complete=False)
           items = order.orderitem_set.all()
          else:
             items = []
             order = {'get_cart_total':0, 'get_cart_items':0}
             
             context = {'items': items, 'order':order}  
          return render(request,'cart.html',context)

def FAQsPage(request):
    return render (request, 'FAQs.html')

def FeedbackPage(request):
    return render (request, 'feedback.html')

def RegisterPage(request):
    if request.method=='POST':
     uname=request.POST.get('username')   
     email=request.POST.get('Email address') 
     pass1=request.POST.get('pass1') 
     pass2=request.POST.get('pass2')
     
     if pass1!=pass2:
         msg = "Please make sure that both passwords are the same !"
         messages.error(request, msg)
         return HttpResponseRedirect(request.path)
     else:
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
     print(uname,email,pass1) 
     
    return render (request, 'Signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('store')
        else:
            return HttpResponse("Username or Passsword is incorrect")
    return render (request, 'Login.html')

# @login_required(login_url='login')
def StorePage(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store.html', context)

def CheckoutPage(request):
    context={}
    if request.user.is_authenticated:
           customer = request.user.customer
           order, created = Order.objects.get_or_create(customer=customer, complete=False)
           items = order.orderitem_set.all()
    else:
             items = []
             order = {'get_cart_total':0, 'get_cart_items':0}
             
             context = {'items': items, 'order':order} 
    return render (request, 'checkout.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('home')

def PayPage(request):
    return render(request,'payment.html')