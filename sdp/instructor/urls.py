from django.conf.urls import url

from . import views


app_name = 'instructor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    
    url(r'^view/(?P<course_id>\d+)/(?P<order_id>\d+)$', views.view_module, name='view_module'),
    url(r'^view/(?P<course_id>\d+)/$', views.view_course, name='view_course'),
    
    url(r'^move_up/(?P<course_id>\d+)/(?P<module_id>\d+)/$',views.move_up, name='move_up'),
    
    url(r'^move_down/(?P<course_id>\d+)/(?P<module_id>\d+)/$',views.move_down, name='move_down'),
    
    url(r'^open_close/(?P<course_id>\d+)/$', views.open_close, name='open_close'),
    
    url(r'^delete/(?P<course_id>\d+)/$', views.delete_course, name='delete_course'),
    
    url(r'^view/(?P<course_id>\d+)/$', views.view_course, name='view_course'),
    
    url(r'^create_module/(?P<course_id>\d+)/$', views.create_module, name='create_module'),
    
    url(r'^edit/(?P<course_id>\d+)/(?P<order_id>\d+)$', views.edit_module, name='edit_module'),
    
    url(r'^create_course/$', views.create_course, name='create_course'),
    url(r'^real_create/$', views.real_create, name='real_create'),
    
    
    
    
]
