from django.conf.urls import url

from . import views


app_name ='course'
urlpatterns = [
    
    url(r'^(?P<course_id>\d+)/(?P<order_id>\d+)/real_edit/$', views.real_edit, name='real_edit'),
    url(r'^(?P<course_id>\d+)/(?P<order_id>\d+)/$', views.edit, name='edit'),
    url(r'^(?P<course_id>\d+)/$', views.view, name='view'),
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<course_id>\d+)/(?P<order_id>\d+)$', views.view_module, name='view_module'),
    url(r'^view/(?P<course_id>\d+)$', views.participant_view_course, name='participant_view_course'),
]
