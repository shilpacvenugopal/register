from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password, check_password
from .models import UserDetails

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        country = request.POST['country']
        nationality = request.POST['nationality']
        mobile = request.POST['mobile']
        password = request.POST['password']

        if not name or not email or not role or not country or not nationality or not mobile or not password:
            messages.error(request, 'All fields are required.')
            error_message='All fields are required.'
            return render(request, 'register.html', {'error_message': error_message})
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            error_message='Email is already registered.'
            return render(request, 'register.html', {'error_message': error_message})
        users = UserDetails(
            name=name,
            email=email,
            role=role,
            country=country,
            nationality=nationality,
            mobile=mobile,
            password=make_password(password)
        )
        users.save()
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not email or not password:
            error_message = 'Both email and password are required.'
            return render(request, 'login.html', {'error_message': error_message})

        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})

        if check_password(password, user.password):
            messages.success(request, 'Login successful.')
            user_role = user.role

            if user_role == 'student':
                return redirect('student_page')
            elif user_role == 'staff':
                return redirect('staff_page')
            elif user_role == 'admin':
                return redirect('admin_page')
            elif user_role == 'editor':
                return redirect('editor_page')
            else:
                return redirect('error_page')
        else:
            error_message = 'Invalid email or password.'

        return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')



def student_page(request):
    return render(request, 'student_page.html')

def staff_page(request):
    return render(request, 'staff_page.html')

def admin_page(request):
    return render(request, 'admin_page.html')

def editor_page(request):
    return render(request, 'editor_page.html')

def error_page(request):
    return render(request, 'error.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')
