from django.http.response import Http404
from django.test import TestCase

# Create your tests here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.core.mail import send_mail


def register(request):

    # check if request is of type post (user register)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        # check if form received is valid
        if form.is_valid():
            form.save()     # Save the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Registered For {username}.') # Flash message usage with f_string
            return redirect('login')   # Redirect user to home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})  # Render register with form


@login_required    # Decorator to add restrictions to profile view
# @allowed_users(allowed_roles=['admin'])
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        print(request.FILES)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile.html', context)
    elif request.method == 'GET':

        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'users/profile.html', context)
    raise Http404()

