from django.conf.urls import url

from . import views

app_name = 'participant'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^enroll/(?P<course_id>[0-9]+)/real_enroll', views.real_enroll, name='real_enroll'),
    url(r'^enroll/(?P<course_id>[0-9]+)', views.enroll_detail, name='enroll_detail'),
    url(r'^enroll/$', views.enroll, name='enroll'),

    url(r'^enroll/(?P<category>[a-zA-Z]+)$', views.enroll_category, name='enroll_category'),
    url(r'^drop/(?P<course_id>[0-9]+)$', views.real_drop, name='real_drop'),

    url(r'^view/(?P<course_id>[0-9]+)/$', views.view_course, name='view_course'),
    url(r'^view/(?P<course_id>[0-9]+)/(?P<order_id>[0-9]+)/$', views.view_module, name='view_module'),


]
