from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from cmanagement.models import cmanagement,cmanagementForm

def index(request):
	if request.method== 'POST':
		c_obj = get_object_or_404(cmanagement,pk=request.POST.get('delete'))
		c_obj.delete()
		return render(request,'cmanagement/index.html',{'cmanagement':cmanagement.objects.all()})	
	else:
		latest_list = cmanagement.objects.all()
		return render(request,'cmanagement/index.html',{'cmanagement':latest_list})

def sortcost(request):
	latest_list = cmanagement.objects.order_by('cost')
	return render(request,'cmanagement/index.html',{'cmanagement':latest_list})	

def details(request,c_id):
	c_detail = get_object_or_404(cmanagement,pk=c_id)
	return render(request,'cmanagement/details.html',{'c_detail':c_detail})

def insert(request):
	if request.method == 'POST':
		form = 	cmanagementForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			phone = form.cleaned_data['phone']
			address  = form.cleaned_data['address']	
			details = form.cleaned_data['details']
			cost = form.cleaned_data['cost']
			f = cmanagement.objects.create(name=name,phone=phone,details=details,address=address,cost=int(cost))
			return render(request,'cmanagement/insert.html',{'error_msg':'Success'})
		else:
			return render(request,'cmanagement/insert.html',{'error_msg':form})	
	else:
		return render(request,'cmanagement/insert.html')		

def updates(request,c_id):
	if request.method == 'POST':
		form = 	cmanagementForm(request.POST)
		if form.is_valid():
			c_obj = get_object_or_404(cmanagement,pk=c_id)
			c_obj.name = form.cleaned_data['name']
			c_obj.phone = form.cleaned_data['phone']
			c_obj.address  = form.cleaned_data['address']	
			c_obj.details = form.cleaned_data['details']
			c_obj.cost = form.cleaned_data['cost']
			c_obj.save()
			return render(request,'cmanagement/update.html',{'succ':'Success'})
	else:
		c = get_object_or_404(cmanagement, pk=c_id)
		return render(request,'cmanagement/update.html',{'cmanagement':c })