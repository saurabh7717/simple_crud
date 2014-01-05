from django.conf.urls import patterns,url

from cmanagement import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^(?P<c_id>\d+)/$',views.details,name='details'),
	url(r'^insert/$',views.insert,name='insert'),
	url(r'^sortcost/$',views.sortcost,name='sortcost'),
	url(r'^(?P<c_id>\d+)/updates/$',views.updates,name='updates'),
	) 
