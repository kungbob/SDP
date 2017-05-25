from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.models import User as auth_user
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.urls import reverse

from .forms import LoginForm, RegisterForm
from user.models import User, Acc
from participant.models import Participant, Record
from instructor.models import Instructor
from hr.models import Hr

def login(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=name, password=pw)
            if user is not None:
                auth_login(request, user)
                try:
                    my_user = User.objects.get(username = name)
                    temp_key = my_user.pk
                    acc_type  = my_user.acc_type
                    if acc_type.acc_type == 'Participant':
                        return HttpResponseRedirect(reverse('participant:index'))
                    elif acc_type.acc_type == 'Instructor':
                        return HttpResponseRedirect(reverse('instructor:index'))
                    elif acc_type.acc_type == 'Administrator':
                        return HttpResponseRedirect(reverse('administrator:index'))
                    elif acc_type.acc_type == 'HR':
                        return HttpResponseRedirect(reverse('hr:index'))
                    else:
                        return HttpResponseRedirect(reverse('login:login'))
                except my_user.DoesNotExist:
                    raise HttpResponseRedirect(reverse('login:login'))

            else:
            # redirect to a new URL:
                return HttpResponseRedirect(reverse('login:login'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'login/index.html',{'form': form})


# Create your views here.
def create(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_user = request.POST['username']
            new_pw = request.POST['password']
            user = auth_user.objects.create_user(new_user, '', new_pw)
            user.save()

            type_of_user = Acc.objects.get(acc_type = 'Participant')
            new_user = User(username = new_user, password = new_pw , acc_type = type_of_user)
            new_user.save()

            new_participant = Participant(user = new_user)
            new_participant.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('login:login'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
    return render(request, 'login/create.html',{'form': form})

# Create your views here.
