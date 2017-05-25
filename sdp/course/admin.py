from django.contrib import admin

# Register your models here.


from .models import Instructor
from .models import Category
from .models import Course
from .models import Module

admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Module)
