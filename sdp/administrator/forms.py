from django import forms
from user.models import User
from course.models import Course,Category
from django.db.models import Q

class EditForm(forms.Form):
    list = (
        ("Instructor","Instructor"),
        ("Participant","Participant"),
        ("Administrator","Administrator"),
        ("HR","HR"),
        
    )
    username = forms.CharField(max_length=50)
    acc_type = forms.ChoiceField(choices=list)
    user_id = forms.IntegerField()
    
    def clean(self):
        cleaned_data = super(EditForm,self).clean()
        
        my_username = cleaned_data.get("username")
        my_user_id = cleaned_data.get("user_id")
        
        users = User.objects.filter(~Q(pk = my_user_id)).filter(username = my_username)
        
        if users.exists():
            self.add_error('username','username is used!')

            
class CategoryForm(forms.Form):

    category = forms.CharField(max_length=50)

    
    def clean(self):
        cleaned_data = super(CategoryForm,self).clean()
        
        my_category = cleaned_data.get("category")
        
        categories = Category.objects.filter(category = my_category)
        
        if categories.exists():
            self.add_error('category','Category name is used!')
            
                   
class EditCategoryForm(forms.Form):

    category = forms.CharField(max_length=50)
    category_id = forms.IntegerField()

    def clean(self):
        cleaned_data = super(EditCategoryForm,self).clean()
        
        my_category = cleaned_data.get("category")
        my_category_id = cleaned_data.get("category_id")
        
        categories = Category.objects.filter(~Q(pk = my_category_id)).filter(category = my_category)
        
        if categories.exists():
            self.add_error('category','Category name is used!')
            
            
            
class UserForm(forms.Form):
    
    list = (
        ("Instructor","Instructor"),
        ("Participant","Participant"),
        ("Administrator","Administrator"),
        ("HR","HR"),
        
    )
    
    
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    
    acc_type = forms.ChoiceField(choices=list)
    
    def clean(self):
        cleaned_data = super(RegisterForm,self).clean()
        
        my_username = cleaned_data.get("username")
        my_password = cleaned_data.get("password")
        my_password2 = cleaned_data.get("password2")
        
        
        users = User.objects.filter(username = my_username)
        
        if users.exists():
            self.add_error('username','username is used!')
            
            
        if len(my_password) < 6:
            self.add_error('password','password must be 6 character long!')
            
        if not my_password == my_password2:
            self.add_error('password2','password not the same !')

        
        
        
            
        
        
        
        
        
        
    
    
    
