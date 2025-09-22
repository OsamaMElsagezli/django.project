from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login,logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.views import View # type: ignore
from django.contrib.auth.models import User # type: ignore
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm # type: ignore

# Create your views here.
def register_view(request):
    error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after successful registration
        else:
            # This will catch errors like "passwords don't match"
            error = form.errors
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form, 'error': error})


def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Invalid username or password'

    return render(request, 'accounts/login.html', {'error': error}) 

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')

# Home Page.
# Using the decorator.
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')  

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' to redirect URL.
    redirect_field_name ='/redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')