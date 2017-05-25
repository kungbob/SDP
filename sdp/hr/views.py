from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User as auth_user
from django.contrib.auth import logout

from user.models import User, Acc
from instructor.models import Instructor
from participant.models import Participant, Record
from administrator.models import Administrator
from course.models import Category
from .models import Hr
# Create your views here.
def index(request):
    try:
        name = request.user.get_username()
        my_user = User.objects.get(username = name)
        acc_type  = my_user.acc_type
        if acc_type.acc_type == 'HR':
            temp = Acc.objects.get(acc_type = "Participant")
            users = User.objects.filter(acc_type = temp)
            return render(request, 'hr/index.html',{'users': users})
        else:
            logout(request)
            return HttpResponseRedirect(reverse('login:login'))
    except my_user.DoesNotExist:
        raise HttpResponseRedirect(reverse('login:login'))

def view_record(request,user_id):
    my_user = User.objects.get(pk = user_id)
    my_participant = Participant.objects.get(user = my_user)
    records = Record.objects.filter(participant = my_participant)

    return render(request,'hr/view_record.html',{'records':records})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))
