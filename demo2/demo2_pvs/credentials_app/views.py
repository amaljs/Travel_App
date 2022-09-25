
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def logoutuser(request):
    auth.logout(request)
    return  redirect('/')
def loginuser(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid login')
            return redirect('login')
    return render(request,'login.html')
# Create your views here.
def register(request):

    if request.method == "POST":

        username=request.POST['username']
        first_name = request.POST['firstname']
        email = request.POST['email']
        last_name = request.POST['lastname']
        password_2 = request.POST['password1']
        password = request.POST['password2']

        if password_2==password :
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                print('username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email aleardy taken')
                print('Email aleardy taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save()
                messages.info(request,"user created")
                print('usercreated')
                return  redirect('login')



        else:
            messages.info(request,'password don"t match')
            return redirect('register')
        # return redirect('/')
    return  render(request,'register.html')