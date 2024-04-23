from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterUserForm, LoginUserForm

def register_user_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request, f'User created for {name} successfully')
            return redirect('users:login_user')
        else:
            return render(request, 'users/register_user.html', {'form':form})
    else:
        form = RegisterUserForm()
        context = {
            'form':form
        }
    return render(request, 'users/register_user.html', context)

def login_user_view(request):
    
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.name}!')
                if request.user.is_authenticated:
                    return redirect('users:dashboard')
            else:
                messages.warning(request, 'Invalid email or password.')
    else:
        form = LoginUserForm()

    return render(request, 'users/login_user.html', {'form': form})


def logout_user_view(request):
    logout(request)
    return redirect('users:login_user')

def dashboard_view(request):
    return render(request,'users/dashboard.html')
