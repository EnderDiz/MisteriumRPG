from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    login_form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "login":
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("main_menu")

        elif action == "register":
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect("main_menu")

    return render(request, "game/login.html", {
        "login_form": login_form,
        "register_form": register_form
    })

def index(request):
    return render(request, "game/index.html")

def main_menu(request):
    return render(request, "game/main_menu.html")

def observer(request):
    return render(request, "game/observer.html")

def guide(request):
    return render(request, "game/guide.html")

def patchnote(request):
    return render(request, "game/patchnote.html")