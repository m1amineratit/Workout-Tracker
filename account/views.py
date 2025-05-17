from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})


def logout_view(request):
    logout(request)
    return redirect(login)