from django.http import HttpResponse
from django.shortcuts import render, redirect
from db.models import Employee, Login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
import logging


# Set up a logger
logger = logging.getLogger(__name__)

def login(request):
	return render(request,"login.html")

def signup(request):
	return render(request,"signup.html")


def insert(request):
    if 'user_id' in request.session:
        return render(request, 'insert.html', {'user_name': request.session.get('user_name')})
    else:
        return redirect('/login/')  # Redirect to login if not logged in


def loginafter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Login.objects.get(email=email)
        except Login.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        # Check the password
        if check_password(password, user.password):
            request.session['user_id'] = user.id  # Store user ID in session
            request.session['user_name'] = user.name  # Store user name
            messages.success(request, "Login successful!")  # Success message
            return redirect('/insert/')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

def signupafter(request):
	name = (request.POST["name"])
	email = (request.POST["email"])
	password =  (request.POST["password"])
	res = Login(name = name, email = email, password = password)
	res.save()
	return redirect("insert") 


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