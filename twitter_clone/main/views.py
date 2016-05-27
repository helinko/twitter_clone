from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        # Show feed
        return redirect('feed')
    else:
        # Show the login form
        return redirect('/accounts/register/')
