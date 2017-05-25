from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User as auth_user
import datetime

from .models import Participant
from user.models import User
from .models import Record

from course.models import Course, Category ,Module
from django.urls import reverse

from .forms import NameForm


@login_required(login_url='login:login')
def index(request):
    try:
        temp_name = request.user.get_username()
        my_user = User.objects.get(username = temp_name)
        my_participant = Participant.objects.get(user = my_user)
        record = Record.objects.all().filter(participant = my_participant)
    except my_participant.DoesNotExist:

        raise Http404("404 error")
    return render(request, 'participant/index.html', {'record': record})


@login_required(login_url='login:login')
def view_course(request, course_id):
    temp_name = request.user.get_username()
    my_user = User.objects.get(username = temp_name)
    my_participant = Participant.objects.get(user = my_user)

    my_course = Course.objects.get(pk=course_id)
    modules = Module.objects.all().filter(course= my_course).order_by('order')
    count =  Module.objects.all().filter(course= my_course).count()
    
    
    if  Record.objects.filter(course = my_course, participant = my_participant, status = 'unfinish').exists():
        record_num = Record.objects.get(course = my_course, participant = my_participant, status = 'unfinish').module + 2
    else:
        
        record_num = count + 1

    return render(request, 'participant/view_course.html',{'course': my_course, 'modules':modules , 'record_num':record_num})


@login_required(login_url='login:login')
def view_module(request,  course_id, order_id):
    try:

        temp_name = request.user.get_username()
        my_user = User.objects.get(username = temp_name)
        my_participant = Participant.objects.get(user = my_user)

        my_course = Course.objects.get(pk=course_id)
        my_module = Module.objects.get(order = order_id,course = my_course,)
        
        check = Record.objects.filter(course = my_course, participant = my_participant , status = 'unfinish').exists()
        
        
        if check:
            
            my_record = Record.objects.get(course = my_course, participant = my_participant , status = 'unfinish')

            if my_record.module < int(order_id):
                my_record.module = int(order_id)
                my_record.save()

            my_record = Record.objects.get(course = my_course, participant = my_participant , status = 'unfinish')
            count = Module.objects.all().filter(course = my_course).count()

            if count == my_record.module:
                my_record.status = 'finish'
                my_record.finish_date = datetime.datetime.now().date()
                my_record.save()


    except(KeyError, User.DoesNotExist, Course.DoesNotExist, Participant.DoesNotExist):

        response = "<script>window.alert('hv some error checking finish!');document.location.replace('/participant/');</script>"
        return HttpResponse(response)

    else:
        context = {'course': my_course, 'module' : my_module,}
        return render(request, 'participant/view_module.html', context)



#-------------------------------------------------------------------
@login_required(login_url='login:login')
def enroll(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, 'participant/enroll.html', context)

@login_required(login_url='login:login')
def enroll_category(request, category):

    my_category = Category.objects.get(category=category)
    courses = Course.objects.filter(categories=my_category, status = 'open')
    context = {
        'courses': courses,
    }
    return render(request, 'participant/enroll_category.html', context)

@login_required(login_url='login:login')
def enroll_detail(request, course_id):

    course = Course.objects.get(pk=course_id)
    categories = [t.category for t in course.categories.all()]
    context = {'course': course, 'categories' : categories}

    return render(request, 'participant/enroll_detail.html', context)


@login_required(login_url='login:login')
def real_enroll(request,course_id):

    try:
        temp_name = request.user.get_username()
        my_user = User.objects.get(username = temp_name)
        my_course = Course.objects.get(pk=course_id)
        my_participant = Participant.objects.get(user = my_user)

        if Record.objects.filter(participant = my_participant, status='unfinish').exists():
            raise Exception('already enrolled a course!')

        else:
            new_record = Record(participant = my_participant, course = my_course, status='unfinish', module=0)
            new_record.save()



    except (KeyError, User.DoesNotExist, Course.DoesNotExist, Participant.DoesNotExist,Exception):
        # Redisplay the question voting form.

        context ={'course_id': course_id,}



        response = "<script>window.alert('You have already enrolled a course!');document.location.replace('/participant/');</script>"
        return HttpResponse(response)


    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('participant:index'))

@login_required(login_url='login:login')
def real_drop(request,course_id):
    try:
        temp_name = request.user.get_username()
        my_user = User.objects.get(username = temp_name)
        my_course = Course.objects.get(pk=course_id)
        my_participant = Participant.objects.get(user = my_user)

        my_record = Record.objects.filter(participant = my_participant,course=my_course,status='unfinish')
        if my_record.exists():
            my_record.delete()

        else:
            raise Exception("can't find record")
    except(KeyError, User.DoesNotExist, Course.DoesNotExist, Participant.DoesNotExist,Record.DoesNotExist):
        response = "<script>window.alert('error occur when deleting');document.location.replace('/participant/');</script>"
        return HttpResponse(response)
    else:
        return HttpResponseRedirect(reverse('participant:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))
    # Redirect to a success page.
