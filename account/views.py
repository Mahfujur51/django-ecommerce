
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login


from account.forms import RegistrationForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return HttpResponse("You are Authenticate")
    else:
        form = RegistrationForm()
        if request.method=="POST" or request.method=="post":
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("You are Register now ")
    context={
        'form':form
    }
    return render(request,'register.html',context)

def CustomerLogin(request):
    if request.user.is_authenticated:
        return HttpResponse("You are login")
    else:
        if request.method=='post' or request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            customer=authenticate(request,username=username,password=password)
            if customer is not None:
                login(request,customer)
                return HttpResponse('You are Logged in Successfully!!')
            else:
                return HttpResponse("404")            
    return render(request,'login.html')       