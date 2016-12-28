from django.conf.urls import url
from . import views

urlpatterns=[
	#...../paintings/
	url(r'^$', views.index, name='index'),

	#...../paintings/<id>/
	url(r'^(?P<segment_id>[0-9]+)/$', views.nextseg, name='nextseg'),

	#...../paintings/<id>/like/
	url(r'^(?P<segment_id>[0-9]+)/like/$', views.like, name='like'),
]