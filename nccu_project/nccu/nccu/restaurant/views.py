from django.shortcuts import render,render_to_response,redirect
from restaurant.models import Restaurant,Comment,Food
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.utils import timezone
# Create your views here.
def home(request):

	return render_to_response('restaurant/home.html',locals())

def restaurant(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurant/restaurant.html',locals())

def add_restaurant(request):
	error = []
	if 'ok' in request.POST:
		name = request.POST['name']
		phone_number = request.POST['phone']
		address = request.POST['address']
		opentime  = request.POST['opentime']
	
		if not name:
			error.append('Please Enter Restaurant Name')
		if not phone_number:
			error.append('Please Enter Restaurant Phone_number')
		if not address:
			error.append('Please Enter Restaurant address')
		if not opentime:
			error.append('Please Enter Restaurant opentime')
		if not error:
			r = Restaurant(name = name,phone_number = phone_number,address = address,opentime = opentime)
			r.save()
			name = ''
			phone_number = ''
			address = ''
			opentime = ''
			return HttpResponseRedirect('/restaurant')
	return render_to_response('restaurant/add_restaurant.html',locals())

def menu(request):
	if 'id' in request.GET and request.GET['id'] !='':
		restaurant=Restaurant.objects.get(id=request.GET['id'])
		return render_to_response('restaurant/menu.html',locals())
	else:
		return HttpResponse("/restaurant/")

def comment(request,id):
	error = []
	if 	id:
		r=Restaurant.objects.get(id=id)
	else:
		return HttpResponseRedirect("/restaurant/")

	
	if 	'ok' in request.POST:
		user = request.POST['user']
		content = request.POST['content']
		date_time=timezone.localtime(timezone.now())
	
		if not user:
			error.append('Please Enter User Name')
		if not content:
			error.append('Please Enter Some Comments')
		if not error:
			Comment.objects.create(
				user=user,
				content=content,
				date_time=date_time,
				restaurant=r
				)
		
	return render_to_response('restaurant/comment.html',locals())



def bus_search(request):
	return render_to_response('restaurant/bus.html')
		
def bus(request):
	if  request.GET['q']:
		message = 'You search for: %s' %request.GET['q']
	else:
		message = 'You submmitted an empty form'
	return HttpResponse(message)

def building(request):
	return render(request,'restaurant/building.html')