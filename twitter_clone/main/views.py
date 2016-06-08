from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# The index acts as the main feed, a login page and a registering page depending
# whether the user has signed in.

def index(request):
    if request.user.is_authenticated():
        # Show feed
        # Some get_tweets method here
        return render(request, 'feed.html')
    # Not authenticated, so show a login page
    if request.method == 'GET':
        # Show the form.
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})
    elif request.method == 'POST':
        # Logging in

        ### !!! IS THIS OK?
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('feed')
            else:
                context = { 'message': "Please activate your account \
                by clicking the activation link in your e-mail"}
                return render(request, 'general.html', context)
        else:
            # Auth failed, render the same page
            form = AuthenticationForm(request.POST)
            return render(request, 'index.html', {'form': form})
    else:
        # Another method, what to do?
        context = { 'message': "You seemed to use something else than GET or POST. \
        I wonder what you're trying to do."}
        return render(request, 'general.html', context)
def logout_view(request):
    if not request.user.is_authenticated():
        return redirect('index')
    else:
        logout(request)
        context = {'message': "You have been successfully logged out. "}
        return render(request, 'general.html', context)
def profile(request):
    context = {'message': "Profile page"}
    return render(request, 'general.html', context)
