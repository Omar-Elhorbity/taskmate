from django.shortcuts import render
from .forms import CustomRegisterForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('register')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return redirect('home')

