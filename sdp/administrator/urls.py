from django.conf.urls import url

from . import views


app_name = 'administrator'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit_user, name='edit_user'),
    url(r'^edit_category/(?P<category_id>\d+)$', views.edit_category, name='edit_category'),
    url(r'^create_category/$', views.create_category, name='create_category'),
    url(r'^category_list/$', views.category_list, name='category_list'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^logout/$', views.logout_view, name='logout'),
    
]
