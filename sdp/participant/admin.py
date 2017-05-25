from django.contrib import admin


# Register your models here.
from .models import Participant
from .models import Record

admin.site.register(Record)
admin.site.register(Participant)
