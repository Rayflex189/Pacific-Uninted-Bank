from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('dashboard/', views.home, name='home'),
    path('account/', views.Account, name='account'),
    path('add_cards/', views.Add_cards, name='add_cards'),
    path('cards/', views.cards, name='cards'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('register/', views.register, name='register'),
    path('service/', views.service, name='service'),
    path('transactions/', views.transactions, name='transactions'),
    path('settings/', views.settings, name='settings'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('payment_slip/', views.payment_slip, name='payment_slip'),
    path('about/', views.About, name='about'),
    path('services/', views.services, name='services'),
    path('contact-us/', views.Contact_Us, name='contact_us'),
]