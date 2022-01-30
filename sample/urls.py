"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.project,name="project"),
    path("viewusers/",views.viewusers,name="viewusers"),
    path("home/",views.home,name="home"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("signuppage/",views.signuppage,name="signuppage"),
    path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
    path("resetpassword/",views.resetpassword,name="resetpassword"),
    path("sam/",views.sam,name="sam"),
    path("tours/",views.tourspage,name="tourspage"),
    path("bookbus/",views.bookbuspage,name="bookbuspage"),
    path("busfilter/",views.busfilter,name="busfilter"),
    path("flightfilter/",views.flightfilter,name="flightfilter"),
    path("bookflight/",views.bookflightpage,name="bookflightpage"),
    path("tourinformation/<str:location>",views.tourinformation,name="tourinformation"),
    path("hospitality/",views.hospitalitypage,name="hospitalitypage"),
    path("viewseats/<str:travels>",views.viewseats,name="viewseats"),
    path("paymentpage/<str:travels>/<int:id>",views.paymentpage,name="paymentpage"),
    path("confirmpayment/",views.confirmpayment,name="confirmpayment"),
    path("aboutus/",views.aboutuspage,name="aboutuspage"),
    path("flightticketdetails/<str:flight>",views.flightticketdetails,name="flightticketdetails"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("flightticketconfirm/",views.flightticketconfirm,name="flightticketconfirm"),
    path("seasonsdashboard/",views.seasonsdashboard,name="seasonsdashboard"),
    path("profile/",views.profile,name="profile"),
    path("flightpaymentpage/",views.flightpaymentpage,name="flightpaymentpage"),
    path("tourconfirm/",views.tourconfirm,name="tourconfirm"),
    path("booked/",views.booked,name="booked"),
    path("date/",views.demodate,name="demodate"),
    path("logout/",views.logout,name="logout"),
    path("lr/",views.lr,name="lr"),
    path("shortpath/",views.shortpath,name="shortpath"),
    path("createtour/",views.createtour,name="createtour"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
