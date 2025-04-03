from django.http import HttpResponse
from django.shortcuts import render, redirect
from db.models import Employee, Register
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
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
            register = Register.objects.get(email=email)
        except Register.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        # Check the password
        if check_password(password, register.password):
            request.session['user_id'] = register.id  # Store user ID in session
            request.session['user_name'] = register.name  # Store user name
            messages.success(request, "Login successful!")  # Success message
            return redirect('/showall/')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')

def signupafter(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if Register.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        # Save the user with hashed password
        hashed_password = make_password(password)
        register = Register(name=name, email=email, password=hashed_password)
        register.save()

        return render(request, 'signup.html', {'success': 'User signed up successfully.'})

    return render(request, 'signup.html')


def profile(request,userid):
	showdata = Employee.objects.get(eid=userid)
	dd={
	'showdata':showdata
	}
	return render(request,'profile.html',dd)	

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


def showall(request):
    # Check if the user is logged in
    if 'user_id' in request.session:
        showdata = Employee.objects.all()  # Fetch all employee records
        return render(request, "showall.html", {
            'showdata': showdata,
            'user_name': request.session.get('user_name')
        })
    else:
        return redirect('/login/')  # Redirect to login if not logged in
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

def logout(request):
    request.session.flush()  # Clear session
    return redirect('/login/')  # Redirect to login after logout