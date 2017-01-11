
from django.conf.urls import include, url
from . import views
from django.contrib import admin

admin.autodiscover()
# app urls.py

urlpatterns = [
	url(r'^home',views.home,name = 'home'),
	url(r'^restaurant/', views.restaurant,name = 'Food Map'),
	url(r'^add/', views.add_restaurant,name='add_restaurant'),
	url(r'^menu/(\d{1,5})/$',views.menu,name="menu"),
	url(r'^comment/(\d{1,5})/$',views.comment,name="comment"),
	#url(r'^bus/', views.bus,name = 'Bus Map'),
	#url(r'^bus_search/', views.bus_search,name = 'Bus_search Map'),
	url(r'^building/', views.building,name = 'Building Map'),
	url(r'^search/', include('haystack.urls')),
]