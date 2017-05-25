from django.shortcuts import render
from .models import Course
from .models import Module
from django.template import loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditForm

def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course/index.html', context)


def participant_view_course(request, course_id):
    
    my_course = Course.objects.get(pk=course_id)
    
    modules = Module.objects.all().filter(course = my_course)
    context = {'course': my_course, 'modules' : modules}
    
    return render(request, 'course/participant_view_course.html', context)

def view(request, course_id):
    
    my_course = Course.objects.get(pk=course_id)
    
    modules = Module.objects.all().filter(course = my_course)
    context = {'course': my_course, 'modules' : modules}
    
    return render(request, 'course/view.html', context)


def view_module(request, course_id, order_id):
    
    my_course = Course.objects.get(pk=course_id)
    my_module = Module.objects.get(order = order_id,course = my_course,)
    
    context = {'course': my_course, 'module' : my_module,}
    
    return render(request, 'course/view_module.html', context)


def edit(request,course_id,order_id):
    
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            my_course = Course.objects.get(pk=course_id)
            my_module = Module.objects.get(order = order_id,course = my_course,)
            
            my_module.content = form.content
            # redirect to a new URL:
            
            return render(request, 'course/edit.html', {'form': form, 'course_id': course_id, 'order_id': order_id})

    # if a GET (or any other method) we'll create a blank form
    else:
        my_course = Course.objects.get(pk=course_id)
        my_module = Module.objects.get(order = order_id,course = my_course,)
       
        form = EditForm(initial={'content': my_module.content, 'name': my_module.name})
        context = {'module': my_module , 'form': form}

        return render(request, 'course/edit.html', {'form': form, 'course_id': course_id, 'order_id': order_id})
    
def real_edit(request, course_id ,order_id):
    try:
        new_content = request.POST['content']
        new_name = request.POST['name']
        
        my_course = Course.objects.get(pk=course_id)
        my_module = Module.objects.get(order = order_id,course = my_course,)
            
        my_module.content = new_content
        my_module.name = new_name
        
        
        my_module.save()
        
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'course/edit.html')
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('course:view', args=(course_id,)))
       # return render(request, 'course/index.html')

# Create your views here.