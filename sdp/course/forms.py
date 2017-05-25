from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField

class EditForm(forms.Form):
    name = forms.CharField(max_length=50)
    content = forms.CharField(widget=CKEditorUploadingWidget())
#  #  your_name = forms.CharField(label='Your name', max_length=100)

    
    def clean(self,*arg,**kwargs):
    
        my_name = self.cleaned_data.get("name")
        
        if name.len() > 3:
            raise forms.ValidationError("too long!")
            
        return super(EditForm,self).clean(*args,**kwargs)
            