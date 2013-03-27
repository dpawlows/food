from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from views import *


urlpatterns = patterns('',
	(r'^food/$',FoodView.as_view()),
	(r'^food/nations/(?P<nation_id>\d+)/?$', NationView.as_view()) , 	
	(r'^food/nations/(?P<nation_id>\d+)/recipes/(?P<recipe_id>\d+)/?$', RecipeView.as_view()) , 	
	(r'^food/add/',AddView.as_view()),
	(r'^food/new/',NewView.as_view()),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),	

)