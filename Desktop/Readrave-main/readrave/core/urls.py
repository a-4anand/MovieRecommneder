from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('exchange-books/', views.exchange_books, name='exchange_books'),  # Exchange Books
    path('promote-books/', views.promote_books, name='promote_books'),  # Promote Books
    path('blogs/', views.blogs, name='blogs'),  # Blogs
    path('read-and-earn/', views.read_and_earn, name='read_and_earn'),  # Read & Earn
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard (logged-in users)
    path('promote-books/', views.promote_books, name='promote_books'),
    path('blogs/', views.blogs, name='blogs'),
    path('exchange-books/', views.exchange_books, name='exchange_books'),
    path('read-and-earn/', views.read_and_earn, name='read_and_earn'),
]
