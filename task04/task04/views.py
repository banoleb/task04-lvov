from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/registration_form.html',
                      {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect("/app")
        else:
            return render(request, 'registration/registration_form.html',
                          {'form': form})

def page_not_found(request, exception):
    return render(request, "pages/404.html", {})

def error_server(request, exception=None):
    return render(request, "pages/500.html", {})

def permission_denied(request, exception=None):
    return render(request, "pages/403.html", {})
