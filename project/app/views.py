from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import StudentRegistrationForm, AdmissionForm
from .models import Admission
from django.contrib.auth.models import User

def home(request):
    return render(request, 'app/home.html')

def signup(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            names = full_name.split()
            first_name = ' '.join(names[:-1]) if len(names) > 1 else ''
            last_name = names[-1] if names else ''
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def users(request):
    users = User.objects.all()
    return render(request, 'app/users.html', {'users': users})

def admission_form(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admission request submitted successfully!')
            return redirect('registrations')
    else:
        form = AdmissionForm()
    return render(request, 'app/form.html', {'form': form})

def registrations(request):
    admissions = Admission.objects.all().order_by('-submitted_at')
    return render(request, 'app/registrations.html', {'admissions': admissions})
