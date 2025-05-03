"""
URL configuration for QR_Employee_Scanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from db.models import Employee, Register
from QR_Employee_Scanner import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from QR_Employee_Scanner.views import custom_404_view  



urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", include("QR_Employee_Scanner.urls")),  # Include your app's URLs
    path("",views.insert, name="insert"),
    path("showall/",views.showall, name="showall"),
    path("login/",views.login, name="login"),
    path('scan/', views.scan_qr_page, name='scan_qr_page'),
    path("signup/",views.signup, name="signup"),
    path("signupafter/",views.signupafter, name="signupafter"),
    path('loginafter/',views.loginafter, name="loginafter"),
    path('profile/<str:userid>/', views.profile, name='profile'),
    path("insertafter/",views.insertafter, name="insertafter"),
    path('delete/<str:userid>',views.delete),
    path('generate_qr_image/<str:eid>/', views.generate_qr_and_save, name='generate_qr_image'),  # <-- comma added
    path('logout/', views.logout, name='logout'),
    path('generate_qr/<str:eid>/', views.generate_qr_and_save, name='generate_qr'),
    path('update/', views.update_employee, name='update_employee'),

]

handler404 = 'QR_Employee_Scanner.views.custom_404_view'  # ✅ Use the actual app name


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
