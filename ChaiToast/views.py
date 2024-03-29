from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def landing(request):
  return render(request, 'ChaiToast/landing.html')

def signup(request):
    if  request.method == 'GET':
        return render(request,'ChaiToast/signup.html',{'form': UserCreationForm()})
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')

        if b==c:
            #check whether user name is unique
            if (User.objects.filter(username = a)):
                return render(request, 'ChaiToast/signup.html',{'form': UserCreationForm(), 'error':'Username already exists Try again with different username'})
            else:
                user=User.objects.create_user(username = a, password =b)
                user.save()
                login(request,user)
                return redirect('/user/')

        else:
            #password 1 and 2 do not match
            return render(request, 'ChaiToast/signup.html',{'form': UserCreationForm(),'error':'Password Mismatch Try Again'})


def signin(request):
    if request.method == 'GET':
        return render(request, 'ChaiToast/signin.html', {'form': AuthenticationForm()})
    else:
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(request, username=a, password=b)
        if user is None:
            return render(request, 'ChaiToast/signin.html', {'form': AuthenticationForm(), 'error': 'Invalid credentials'})
        else:
            login(request, user)
            return redirect('/user/')  # Replace 'user_page' with the URL name of your user page

def signout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/signin/')