from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.cache import never_cache, cache_control
from django.http import HttpResponseRedirect


@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Parollar mos emas!")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan!")
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz va tizimga kirdingiz!")

            response = HttpResponseRedirect('/')
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            return response
        
        messages.error(request, "Autentifikatsiyada xatolik yuz berdi!")
        return redirect('register')

    return render(request, 'register.html')


@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Siz Tizimga muvaffaqiyatli kirdingiz!')

            response = HttpResponseRedirect('/')
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            return response
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
            return redirect('login')

    return render(request, 'login.html')


@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'profile.html')



@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    auth_logout(request)
    messages.success(request, "Siz Tizimdan muvaffaqiyatli chiqib ketdingiz!")
    return render(request, 'login.html')

