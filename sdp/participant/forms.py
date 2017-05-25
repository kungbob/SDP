from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField

class NameForm(forms.Form):
    your_name = forms.CharField(widget=CKEditorUploadingWidget())
 #    your_name = RichTextField()
#  #  your_name = forms.CharField(label='Your name', max_length=100)
