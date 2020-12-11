from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """ Log the user out """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """ Register new user """
    if request.method != 'POST':
        #Show blank registration form
        form = UserCreationForm()
    else:
        #Form complatation process
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            #login, Redirect to Home Page
            pw = request.POST['password1']
            authenticated_user = authenticate(username= new_user.username, password=pw)

            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request, 'users/register.html', context)

