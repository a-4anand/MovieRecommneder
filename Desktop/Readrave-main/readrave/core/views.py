from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

def home(request):
    books = Book.objects.all()
    return render(request, 'core/home.html', {'books': books})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'core/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'core/signup.html')
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')
    
    return render(request, 'core/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login the user
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'core/login.html')


def exchange_books(request):
    return render(request, 'core/exchange_books.html')  # Create a template for this page

def promote_books(request):
    return render(request, 'core/promote_books.html')

def blogs(request):
    return render(request, 'core/blogs.html')

def read_and_earn(request):
    return render(request, 'core/read_and_earn.html')


@login_required  # Ensures the user is logged in to access this page
def dashboard(request):
    return render(request, 'core/dashboard.html')

def promote_books(request):
    return render(request, 'core/promote_books.html')

def blogs(request):
    return render(request, 'core/blogs.html')

def exchange_books(request):
    return render(request, 'core/exchange_books.html')

def read_and_earn(request):
    return render(request, 'core/read_and_earn.html')








