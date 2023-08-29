from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request,'Signup.html')

def store(request):
    return render(request, 'store.html')

def checkout(request):
    return render(request,'checkout.html')

def about(request):
    return render(request,'About.html')

def about2(request):
    return render(request,'About2.html')

def guest(request):
    return render(request,'Guest.html')

def cart(request):
     return render(request,'cart.html')

def FAQs(request):
    return render(request,'FAQs.html')

def feedback(request):
    return render(request,'feedback.html')

def comments(request):
    return render(request,'commemnts.html')

def contact(request):
    return render(request,'Contact.html')
