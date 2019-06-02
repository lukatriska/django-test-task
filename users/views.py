from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from django import forms


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # address_1 = forms.CharField(
        #     label='Address',
        #     widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
        # )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')