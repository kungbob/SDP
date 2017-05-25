from django.db import models
from user.models import User


# Create your models here.
class Instructor(models.Model):
    user = models.ForeignKey(User)

