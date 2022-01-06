from django.urls import path
from . import views
from authentication import views as authentication_views

urlpatterns = [
    path('', views.appointment, name='appointment'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('unbook_appointment/', views.unbook_appointment, name='unbook_appointment'),
    path('list_all_appointments/', views.list_all_appointments, name='list_all_appointments'),
    path('list_appointments/', views.list_appointments, name='list_appointments'),
    path('my_working_days/', views.my_working_days, name='my_working_days'),
    path('vaccinated_users/', views.vaccinated_users, name='vaccinated_users'),
    path('manage_working_days/', views.manage_working_days, name='manage_working_days'),
    path('manage_appointment/', views.manage_appointment, name='manage_appointment'),
    path('analytics/', views.analytics, name='analytics'),
]
