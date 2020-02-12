from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

def login(request):
    _next = request.GET.get('next', '/index')

    if request.method == "POST":
        _next = request.POST.get('next')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(_next)
    else:
        form = AuthenticationForm(request)

    kwargs = {
        'form': form,
        'next': _next
    }

    return render(request, 'login.html', kwargs)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login-url'))

