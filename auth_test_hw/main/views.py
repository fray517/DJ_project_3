from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm


def home_view(request):
    """Главная страница."""
    return render(request, "main/home.html")


def register_view(request):
    """Страница регистрации."""
    if request.user.is_authenticated:
        return redirect("main:profile")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("main:profile")
    else:
        form = CustomUserCreationForm()

    return render(request, "main/register.html", {"form": form})


def login_view(request):
    """Страница авторизации."""
    if request.user.is_authenticated:
        return redirect("main:profile")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Добро пожаловать, {username}!")
                return redirect("main:profile")
    else:
        form = AuthenticationForm()

    return render(request, "main/login.html", {"form": form})


@login_required
def profile_view(request):
    """Страница профиля пользователя."""
    return render(request, "main/profile.html")
