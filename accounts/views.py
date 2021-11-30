from django.shortcuts import redirect, render
from django.contrib import messages , auth
from django.contrib.auth.models import User
from contacts.models import contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']

        user =  auth.authenticate(username=username, Password=Password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Now you are logged in') 
            return redirect ('dashboard')
        else: 
            messages.error(request, 'Invalid Log in credantails')
            return redirect ('login')
    return render(request,"accounts/login.html")

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exsits!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Exsits!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username, email=email,password=password)
                    auth.login(request, user)
                    messages.success(request, 'Now you are logged in')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'You are resgisterd successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect ('register')
    else:
        return render(request,"accounts/register.html")

@login_required(login_url = 'login')
def dashboard(request):
    user_inquiry = contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiry,
    }
    return render(request,"accounts/dashboard.html", data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success (request, 'Now you are successfully logout')
        return redirect('home')
    return redirect ('home')