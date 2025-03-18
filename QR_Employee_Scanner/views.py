from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def insert(request):
	return render(request,"insert.html")
    
def showall(request):
	return render(request,"showall.html")
