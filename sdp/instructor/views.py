from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Instructor
from user.models import User
from course.models import Course, Category,Module
from django.urls import reverse

from .forms import EditForm,CreateForm

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User as auth_user

from django.http import HttpResponse

@login_required(login_url='login:login')
def index(request):
    temp_name = request.user.get_username()
    
    my_user = User.objects.get(username = temp_name)
    
    me = Instructor.objects.get(user = my_user)

    courses = Course.objects.all().filter(instructor = me)

    context = {'courses': courses,
              }

    return render(request, 'instructor/index.html', context)


@login_required(login_url='login:login')
def view_course(request, course_id):
    
    my_course = Course.objects.get(pk=course_id)
    
    modules = Module.objects.all().filter(course = my_course).order_by('order')
    context = {'course': my_course, 'modules' : modules}
    
    return render(request, 'instructor/view_course.html', context)


def view_module(request,  course_id, order_id):

        
    my_course = Course.objects.get(pk=course_id)
    my_module = Module.objects.get(order = order_id,course = my_course,)

    context = {'course': my_course, 'module' : my_module,}
    return render(request, 'instructor/view_module.html', context)


#def create_course(request):
#    temp_name = request.user.get_username()
    
    #categories = Category.objects.all()
#    categories = [t for t in Category.objects.all()]
 #   context = {
#               'categories' : categories,
#              }
 #   return render(request, 'instructor/create_course.html', context)

def create_course(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            temp_name = request.user.get_username()
            new_code = request.POST['code']
            new_name = request.POST['name']
            new_description = request.POST['description']
            new_categories = request.POST.getlist('categories')
        
            my_user = User.objects.get(username = temp_name)
            me = get_object_or_404(Instructor, user = my_user)

            new_course = Course(code = new_code, instructor = me , name = new_name, description = new_description,status = 'close')

            new_course.save()

            for i in new_categories:
                temp = Category.objects.get(category = i)
                new_course.categories.add(temp)
            
            return HttpResponseRedirect(reverse('instructor:index'))
            
            
        else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
            return render(request, 'instructor/create_course.html',{'form': form})
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateForm()
        
    return render(request, 'instructor/create_course.html',{'form': form})


def real_create(request):
    temp_name = request.user.get_username()
    
    try:
        temp_name = request.user.get_username()
        new_course_code = request.POST['course_code']
        new_course_name = request.POST['course_name']
        new_course_description = request.POST['course_description']
        new_course_category = request.POST.getlist('course_categories')
        
        my_user = User.objects.get(username = temp_name)
        
        me = get_object_or_404(Instructor, user = my_user)

        new_course = Course(code = new_course_code, instructor = me , name = request.POST['course_name'], description = request.POST['course_description'],status = 'close')

        new_course.save()

        for i in new_course_category:
            temp = Category.objects.get(category = i)
            new_course.categories.add(temp)
            
    except (KeyError, Course.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'instructor/create_course.html')
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('instructor:index'))


def create_module(request,course_id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            new_name = request.POST['name']
            new_content = request.POST['content']
               
            my_course = Course.objects.get(pk=course_id)
    
            count = Module.objects.filter(course = my_course).count()
            count = count + 1
    
            new_module = Module(name = new_name, course = my_course,content = new_content, order = count)
    
            new_module.save()
    
            return HttpResponseRedirect(reverse('instructor:view_course', args=(course_id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        
        form = EditForm()
        
        return render(request, 'instructor/create_module.html', {'form': form, 'course_id': course_id, })




def edit_module(request,course_id,order_id):
    
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_content = request.POST['content']
            new_name = request.POST['name']
        
            my_course = Course.objects.get(pk=course_id)
            my_module = Module.objects.get(order = order_id,course = my_course,)
            
            my_module.content = new_content
            my_module.name = new_name
        
            my_module.save()
            # redirect to a new URL:
            
            return HttpResponseRedirect(reverse('instructor:view_course', args=(course_id,)))
        else:
            
            return render(request, 'instructor/edit_module.html', {'form': form, 'course_id': course_id, 'order_id': order_id,})
            

    # if a GET (or any other method) we'll create a blank form
    else:
        my_course = Course.objects.get(pk=course_id)
        my_module = Module.objects.get(order = order_id,course = my_course,)
       
        form = EditForm(initial={'content': my_module.content, 'name': my_module.name})
        context = {'module': my_module , 'form': form}

        return render(request, 'instructor/edit_module.html', {'form': form, 'course_id': course_id, 'order_id': order_id})

    
        
def open_close(request,course_id):
    my_course = Course.objects.get(pk=course_id)
    if my_course.status == 'close':
        my_course.status = 'open'
    else:
        my_course.status = 'close'
        
    my_course.save()
    
    return HttpResponseRedirect(reverse('instructor:index'))


def move_up(request,course_id,module_id):
    
    my_course = Course.objects.get(pk=course_id)
    
    if int(module_id) > 1:
        my_module1 = Module.objects.get(course = my_course, order = module_id)
        my_module2 = Module.objects.get(course = my_course, order = int(module_id)-1)
        
        
        temp = my_module2.order
        my_module2.order = my_module1.order
        my_module1.order = temp
        
        my_module1.save()
        my_module2.save()
        
    return HttpResponseRedirect(reverse('instructor:view_course',kwargs={'course_id': course_id}))


def move_down(request,course_id,module_id):
    
    my_course = Course.objects.get(pk=course_id)
                                   
    count = Module.objects.filter(course = my_course).count()
                                   
    if int(module_id) < count:
        my_module1 = Module.objects.get(course = my_course, order = module_id)
        my_module2 = Module.objects.get(course = my_course, order = int(module_id)+1)
        
                                   
        temp = my_module2.order
        my_module2.order = my_module1.order
        my_module1.order = temp
        
        my_module1.save()
        my_module2.save()
        
    
    return HttpResponseRedirect(reverse('instructor:view_course',kwargs={'course_id': course_id}))
        
        

def delete_course(request,course_id):
    
    my_course = Course.objects.get(pk=course_id)
    my_course.delete()
    
    return HttpResponseRedirect(reverse('instructor:index'))

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))
