from django.shortcuts import render
from user.models import User, Acc
from instructor.models import Instructor
from participant.models import Participant
from administrator.models import Administrator
from course.models import Category
from hr.models import Hr
from .forms import EditForm,CategoryForm,UserForm,EditCategoryForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User as auth_user
from django.contrib.auth import logout
# Create your views here.


def index(request):
    
    try:
        name = request.user.get_username()
        my_user = User.objects.get(username = name)
        acc_type  = my_user.acc_type
        if acc_type.acc_type == 'Administrator':
            users = User.objects.all()
            return render(request, 'administrator/index.html',{'users': users})
        else:
            logout(request)
            return HttpResponseRedirect(reverse('login:login'))
    except my_user.DoesNotExist:
        raise HttpResponseRedirect(reverse('login:login'))
        
        
def category_list(request):

    categories = Category.objects.all()
    return render(request, 'administrator/category_list.html',{'categories':categories})

    



def create_category(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            my_category = request.POST['category']
            
            new_category = Category(category = my_category)
            new_category.save()
            
            return HttpResponseRedirect(reverse('administrator:category_list'))
            
        else:
            
            context = {'form': form}
            
            return render(request, 'administrator/create_category.html', context)


    else:
        
        form = CategoryForm()
        
        context = {'form': form}

        return render(request, 'administrator/create_category.html', context)
    
    
def edit_category(request,category_id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditCategoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            my_category_id = request.POST['category_id']
            my_category = request.POST['category']
            
            old = Category.objects.get(pk=my_category_id)
            
            if not old.category == my_category:
                old.category = my_category
                old.save()
                
            return HttpResponseRedirect(reverse('administrator:category_list'))
            
        else:
            
            context = {'form': form}
            
            return render(request, 'administrator/create_category.html', context)
    else:
        
        category = Category.objects.get(pk=category_id)
        
        form = EditCategoryForm(initial={"category":category,"category_id":category.pk})
        
        context = {'form': form}

        return render(request, 'administrator/create_category.html', context)
    
    

def create_user(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            my_username = request.POST['username']
            my_password = request.POST['password']
            
            #new_category = Category(category = my_category)
            #new_category.save()
            
            return HttpResponseRedirect(reverse('administrator:index'))
            
        else:
            
            context = {'form': form}
            
            return render(request, 'administrator/create_user.html', context)


    else:
        
        form = UserForm()
        
        context = {'form': form}

        return render(request, 'administrator/create_user.html', context)
        
        



def edit_user(request,user_id):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            new_username = request.POST['username']
            new_acc_type = request.POST['acc_type']

            my_user = User.objects.get(pk=user_id)

            user = auth_user.objects.get(username = my_user.username)

            if new_acc_type != my_user.acc_type.acc_type:

                if my_user.acc_type.acc_type == "Instructor":


                    old = Instructor.objects.get(user = my_user)

                else:
                    if my_user.acc_type.acc_type == "Participant":
                        old = Participant.objects.get(user = my_user)
                    else:
                        if my_user.acc_type.acc_type == "Administrator":
                            old = Administrator.objects.get(user = my_user)
                        else:
                            old = Hr.objects.get(user = my_user)
                    


                old.delete()


                if new_acc_type == "Participant":
                    new_participant = Participant(user = my_user)
                    new_participant.save()
                    
                if new_acc_type == "Instructor":
                        new_instructor = Instructor(user = my_user)
                        new_instructor.save()
                        
                if new_acc_type == "Administrator":
                        new_administrator = Administrator(user = my_user)
                        new_administrator.save()
                        
                if new_acc_type == "HR":
                        new_hr = Hr(user = my_user)
                        new_hr.save()
                


            if new_acc_type == "Instructor":
                user.is_staff = True
            else:
                user.is_staff = False

            user.username = new_username

            user.save()


            my_acc_type = Acc.objects.get(acc_type = new_acc_type)

            my_user.username = new_username
            my_user.acc_type = my_acc_type

            my_user.save()

            # redirect to a new URL:

            return HttpResponseRedirect(reverse('administrator:index'))
        else:
            
            
            context = {'user_id': user_id , 'form': form}
            
            return render(request, 'administrator/edit.html', context)
    
    # if a GET (or any other method) we'll create a blank form
    else:

        my_user = User.objects.get(pk=user_id)

        form = EditForm(initial={'username': my_user.username, 'acc_type': my_user.acc_type.acc_type, 'user_id':user_id})
        context = {'user_id': user_id , 'form': form}

        return render(request, 'administrator/edit.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))
