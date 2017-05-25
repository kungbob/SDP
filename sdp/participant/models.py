
from django.db import models
from course.models import Course
from user.models import User


from django.utils.encoding import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Participant(models.Model):
    #user_id = models.IntegerField(default=0)
    user = models.ForeignKey(User)


class Record(models.Model):
    participant = models.ForeignKey(Participant)
    course = models.ForeignKey(Course)
    status = models.CharField(max_length=50)
    module = models.IntegerField()
    finish_date = models.DateField(null=True, blank=True)
