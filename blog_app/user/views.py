from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()           
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been successfully created. You can now login.')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

@login_required
def profile(request):
    return render(request, 'user/profile.html')