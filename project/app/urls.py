from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('users/', views.users, name='users'),
    path('form/', views.admission_form, name='form'),
    path('registrations/', views.registrations, name='registrations'),
]