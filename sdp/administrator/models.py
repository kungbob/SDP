from django.db import models
from user.models import User
# Create your models here.

class Administrator(models.Model):
    user = models.ForeignKey(User)