from django.db import models

# Create your models here.


class Acc(models.Model):
    acc_type = models.CharField(max_length=20)
    def  __str__(self):
        return self.acc_type

class User(models.Model):
    username = models.CharField(unique=True,null=False,max_length=20)
    password = models.CharField(null=False,max_length=20)
    acc_type = models.ForeignKey(Acc)
    
    def  __str__(self):
        return self.username
