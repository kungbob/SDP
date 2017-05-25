from django.conf.urls import url

from . import views

app_name = 'login'
urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^$', views.login, name='login'),
]
