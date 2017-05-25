from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField

from course.models import Category,Course

class EditForm(forms.Form):
    name = forms.CharField(max_length=50)
    content = forms.CharField(widget=CKEditorUploadingWidget())
    

    
    def clean_name(self):
        
        my_name = self.cleaned_data.get("name")
        
        if len(my_name) > 50:
            raise forms.ValidationError("module name too long!")
            
        return my_name
    
    def clean(self):
        cleaned_data = super(EditForm,self).clean()

class CreateForm(forms.Form):
    

    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    description = forms.CharField(widget = forms.Textarea)
    
    categories = forms.MultipleChoiceField(required = True)
    
    
    def __init__(self,*args,**kwargs):
        super(CreateForm,self).__init__(*args,**kwargs)
        self.fields['categories'].choices = [(x.category,x.category) for x in Category.objects.all()]
    
    
    
    def clean(self):
        cleaned_data = super(CreateForm,self).clean()
                
        my_code = self.cleaned_data.get("code")
        my_name = self.cleaned_data.get("name")
  
        
        
        courses = Course.objects.filter(code = my_code)
        
        if courses.exists():
            self.add_error('code','code being used!')
            
            
        courses = Course.objects.filter(name = my_name)
        
        if courses.exists():
            self.add_error('name','name being used!')