from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
# from website.forms import CreateUserForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Kainaat import settings

from datetime import date


######################## Login Views ##########################

def Login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            request.session['user'] = username
            # return redirect('/')
            if user.is_superuser:
                messages.info(request, 'Login Success')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('homepage')
                # return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                messages.info(request, 'Login Attempt Failed')
                # return redirect('show_client')
        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'website/login.html')


######################## Logout Views ##########################
@login_required
def Logout_view(request):
    logout(request)
    return redirect('login')

