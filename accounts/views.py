
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import RegistrationForm, LoginForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy


# Create your views here.
success_url = reverse_lazy('index')


def register_view(request: HttpRequest) -> HttpResponse:
    "ENDPOIT para registro de usuario"
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(success_url)
        return render(request, 'accounts/register.html', {'form': form, 'title': 'Register'})
    return render(request, 'accounts/register.html', {'form': RegistrationForm(), 'title': 'Register'})

# login page
def login_view(request: HttpRequest) -> HttpResponse:
    "ENDPOIT para login de usuario"

    form = LoginForm(request, data=request.POST)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(success_url)
        return render(request, 'accounts/login.html', {'form': form, 'title': 'Login'})

    return render(request, 'accounts/login.html', {'form': form, 'title': 'Login'})

# logout page
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')