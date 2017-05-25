from django.db import models
from instructor.models import Instructor

from django.utils.encoding import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

    
class Category(models.Model):
    category = models.CharField(max_length=200)
    def  __str__(self):
        return self.category

class Course(models.Model):
    code = models.CharField(max_length=200,unique=True)
    instructor = models.ForeignKey(Instructor)
    name = models.CharField(max_length=200,unique = True)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length=50)
    
    def  __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()
    course = models.ForeignKey(Course)
    content = RichTextUploadingField('content')
        
    def  __str__(self):
        return self.name
