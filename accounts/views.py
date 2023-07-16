from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from .fetch_details import GetDetails

# Create your views here.
def register(request):
    if request.method=='POST':
        obj=GetDetails()
        first_name,last_name,username,email,password1,password2=obj.signin_info(request)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'A user with that ID already exists. Try another ID')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'A user with that email already exists. Try another email')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'The two password field\'s do not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"accounts/register.html")



def login(request):
    if request.method == "POST":
        obj1=GetDetails()
        username,password=obj1.login_info(request)
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')



def admin(request):
    if request.method == "POST":
        obj1=GetDetails()
        username,password=obj1.login_info(request)
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_superuser:
                auth.login(request,user)
                return redirect('admin-profile')
            else:
                messages.info(request,'You are not an admin')
                return redirect('login')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('admin')

    else:
        return render(request,'accounts/admin_login.html')


def logout(request):
    auth.logout(request)
    return redirect('services-page')


def profile(request):
    return render(request,'accounts/profile.html')


def new_admin(request):
    if request.method=='POST':
        obj=GetDetails()
        first_name,last_name,username,email,password1,password2=obj.signin_info(request)
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'A user with that ID already exists. Try another ID')
                return redirect('admin-creation')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'A user with that email already exists. Try another email')
                return redirect('admin-creation')
            else:
                user=User.objects.create_superuser(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('admin')
        else:
            messages.info(request,'The two password field\'s do not match')
            return redirect('admin-creation')
        return redirect('/')
    else:
        return render(request,"accounts/create_superuser.html")


def update_info(request):
    current_user=request.user
    if request.method=='POST':
        obj=GetDetails()
        first_name,last_name,username,email=obj.user_info(request)
        if first_name !="":
            current_user.first_name=first_name
        if last_name !="":
            current_user.last_name=last_name
        if username !="":
            current_user.username=username
        if email !="":
                current_user.email=email
        current_user.save()
        return redirect('admin-profile')

    return render(request,"accounts/update_info.html")

def delete(request):
    if request.method=='POST':
        current_user=request.user
        username=request.POST['username']
        del_user=User.objects.get(username=username)
        
        if current_user==del_user:
            del_user.delete()
            return redirect('services-page')
        else:
            del_user.delete()
            return redirect('admin-profile')

    return render(request,"accounts/delete.html")