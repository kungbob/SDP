from django.conf.urls import url

from . import views


app_name = 'hr'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view_record/(?P<user_id>\d+)/$', views.view_record, name='view_record'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
