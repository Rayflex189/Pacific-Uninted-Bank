from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .decorators import *

from .forms import *
from .models import *
# Create your views here.

@login_required
def home(request):
    amount = Amount.objects.all()
    random_number = Profile.objects.all()
    context = {
            'amount':amount, 'random_number':random_number
        }
    return render(request, 'Account/dashboard.html', context)


@login_required
def Account(request):
    return render(request, 'Account/account.html')

@login_required
def Add_cards(request):
    return render(request, 'Account/add_cards.html')

@login_required
def cards(request):
    return render(request, 'Account/cards.html')

def first_page(request):
    return render(request, 'Account/index.html')

@unaunthenticated_user
def Login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!")
    return render(request, 'Account/Login.html')

@unaunthenticated_user
def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        Email = request.POST['email']
        Age = request.POST['age']
        cell_number = request.POST['phone']
        country_name = request.POST['cname']
        password_1 = request.POST.get('pass1')
        password_2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, password_1, password_2)

        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.Email = Email
        myuser.Age = Age
        myuser.cell_number = cell_number
        myuser.country_name = country_name

        myuser.save()

        messages.success(request, 'Your account has been created successfully!')

        return redirect('Login')

    context = {}
    return render(request, 'Account/register.html', context)

def Logout(request):
    logout(request)
    return redirect('Login')

@login_required
def service(request):
    return render(request, 'Account/service.html')

@login_required
def deposit(request):
    return render(request, 'Account/deposit.html')

@login_required
def withdrawal(request):
    return render(request, 'Account/withdrawal.html')

@login_required
def payment_slip(request):
    amount = Amount.objects.all()
    context = {'amount':amount}
    return render(request, 'Account/payment_slip.html', context)

@login_required
def settings(request):
    return render(request, 'Account/settings.html')

def About(request):
    return render(request, 'Account/about.html')

def Contact_Us(request):
    return render(request, 'Account/contact-us.html')

def services(request):
    return render(request, 'Account/services.html')

@login_required
def transactions(request):
    return render(request, 'Account/transactions.html')

# def Account(request):
#     return render(request, 'Account/account.html')

# def Account(request):
#     return render(request, 'Account/account.html')
