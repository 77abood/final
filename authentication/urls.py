from django.urls import path
from . import views
from authentication import views as authentication_views

urlpatterns = [
    path('', views.home, name='Web-Home'),
    path('about/', views.about, name='About-Page'),
    path('FAQ/', views.faq, name='FAQ-Page'),
    path('contact/', views.contact, name='Contact-Page'),
    path('contact/home', views.contact_home, name='Home-Vaccine'),
]

