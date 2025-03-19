from django.http import HttpResponse
from django.shortcuts import render, redirect
from db.models import Employee
from django.http import HttpResponseRedirect

def insert(request):
	return render(request,"insert.html")

def profile(request,userid):
	showdata = Employee.objects.get(eid=userid)
	dd={
	'showdata':showdata
	}
	return render(request,'profile.html',dd)

def showall(request):
	showdata = Employee.objects.all()
	display={
	'showdata':showdata
	}
	return render(request,"showall.html",display)

def insertafter(request):
	eid = (request.POST["eid"])
	ename = (request.POST["ename"])
	eadd =  (request.POST["eadd"])
	esal = int (request.POST["esal"])
	ecity = (request.POST["ecity"])
	eimg = (request.FILES["eimg"])
	res = Employee( eid = eid, ename =ename, eadd = eadd, esal = esal, ecity = ecity, eimg=eimg)
	res.save()
	return redirect("insert") 

def delete(request,userid):
	empdata = Employee.objects.get(eid=userid)
	empdata.delete()
	return HttpResponseRedirect('/showall/')