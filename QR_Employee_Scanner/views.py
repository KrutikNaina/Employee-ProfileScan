from django.http import HttpResponse
from django.shortcuts import render, redirect
from db.models import Employee, Register
from django.contrib import messages
from io import BytesIO
from django.core.files import File
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
import qrcode #QR 
import logging
from datetime import datetime



def generate_qr_and_save(request, eid):
    employee = get_object_or_404(Employee, eid=eid)
    qr_data = f"https://employee-profilescan.krutiknaina.com/profile/{employee.eid}/"

    # Generate QR Code
    qr_img = qrcode.make(qr_data)
    buffer = BytesIO()
    qr_img.save(buffer)
    filename = f'{employee.eid}_qr.png'

    # Save to employee
    employee.qr_code.save(filename, File(buffer), save=True)

    return render(request, 'profile.html', {'showdata': employee})

def scan_qr_page(request):
    if 'user_id' in request.session:
        return render(request, 'qr_scan.html', {'user_name': request.session.get('user_name')})
    else:
        return redirect('/login/')  # Redirect to login if not logged in



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

# def insertafter(request):
# 	eid = (request.POST["eid"])
# 	ename = (request.POST["ename"])
# 	eadd =  (request.POST["eadd"])
# 	esal = int (request.POST["esal"])
# 	ecity = (request.POST["ecity"])
# 	eimg = (request.FILES["eimg"])
# 	res = Employee( eid = eid, ename =ename, eadd = eadd, esal = esal, ecity = ecity, eimg=eimg)
# 	res.save()
# 	return redirect("insert") 

def insertafter(request):
    if request.method == "POST":
        eid = request.POST["eid"]
        ename = request.POST["ename"]
        eadd = request.POST["eadd"]
        esal = int(request.POST["esal"])
        ecity = request.POST["ecity"]
        eimg = request.FILES["eimg"]

        # Check if the employee ID already exists
        if Employee.objects.filter(eid=eid).exists():
            messages.error(request, f"Employee ID {eid} already exists. Please use a unique ID.")
            return redirect("insert")

        # Save employee
        res = Employee(eid=eid, ename=ename, eadd=eadd, esal=esal, ecity=ecity, eimg=eimg)
        res.save()

        # ✅ Generate QR Code
        qr_data = f"https://employee-profilescan.krutiknaina.com/profile/{res.eid}/"
        qr_img = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_img.save(buffer)
        filename = f"{res.eid}_qr.png"
        res.qr_code.save(filename, File(buffer), save=True)

        messages.success(request, "Employee added successfully with QR Code and attendance marked.")
        return redirect("insert")

    return render(request, "insert.html")


def delete(request,userid):
	empdata = Employee.objects.get(eid=userid)
	empdata.delete()
	return HttpResponseRedirect('/showall/')

def logout(request):
    request.session.flush()  # Clear session
    return redirect('/login/')  # Redirect to login after logout

def update_employee(request):
    if request.method == "POST":
        eid = request.POST["eid"]
        employee = get_object_or_404(Employee, eid=eid)

        employee.ename = request.POST["ename"]
        employee.eadd = request.POST["eadd"]
        employee.esal = request.POST["esal"]
        employee.ecity = request.POST["ecity"]

        if "eimg" in request.FILES:
            employee.eimg = request.FILES["eimg"]

        employee.save()
        return HttpResponseRedirect('/showall/')
    else:
        return HttpResponseRedirect('/showall/')
