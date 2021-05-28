from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from . forms import userdataForm,UserLoginForm,DemoDateForm
from .models import User,UserLogin,DemoDate,Buses,Flights,Tours,VisitingData,TravelsData,SeasonsData,TouristPlaces,Distances
from django.db.models import Q
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

def project(request):
	return render(request,"home.html")

def home(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		email=request.session['email']
		return render(request,'userhome.html',{'email':email})
 
def viewusers(request):
	users=User.objects.all()
	return render(request,'display.html',{'users':users})

def loginpage(request):
	form = UserLoginForm()
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			email=form.data["email"]
			password=form.data["password"]
			data=User.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
			if data:
				request.session['email']=email
				if 'email' not in request.session:
					return HttpResponse("Session Expired")
				else:
					return render(request,'userhome.html',{'email':email})
			else:
				return render(request,"login.html",{'form':form})
		else:
			form = UserLoginForm() 
	return render(request,'login.html',{'form':form})
def viewseats(request,travels):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		bus=Buses.objects.filter(Q(travels__iexact=travels))
		if bus:
			return render(request,'viewseats.html',{'bus':bus})
		else:
			return HttpResponse("not found")
		#return render(request,'viewseats.html',{'bus':bus})

def profile(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		email=request.session['email']
		user=User.objects.filter(Q(email__iexact=email))
		return render(request,'profile.html',{'user':user})

def busfilter(request):
	if request.method=="POST":
		dep=request.POST["dep"]
		arr=request.POST["arr"]
		d=request.POST["d"]
		buses=Buses.objects.filter(Q(departure_palce__iexact=dep) & Q(arrival_place__iexact=arr) & Q(date__iexact=d)) 
		return render(request,'busfilter.html',{'buses':buses})
		
def flightfilter(request):
	if request.method=="POST":
		dep=request.POST["dep"]
		arr=request.POST["arr"]
		d=request.POST["d"]
		flights=Flights.objects.filter(Q(departure_palce__iexact=dep) & Q(arrival_place__iexact=arr) & Q(date__iexact=d)) 
		return render(request,'bookflightpage.html',{'flights':flights})


def dashboard(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		labels=[]
		data=[]

		queryset=VisitingData.objects.order_by('-population')[:9]
		for place in queryset:
			labels.append(place.place)
			data.append(place.population)

		return render(request,'dashboard.html',{'labels':labels,'data':data,})

def seasonsdashboard(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		labels=[]
		data=[]

		queryset=SeasonsData.objects.order_by('-population')[:6]
		for s in queryset:
			labels.append(s.season)
			data.append(s.population)

		return render(request,'seasonsdashbord.html',{'labels':labels,'data':data,})

def paymentpage(request,travels,id):
		if id==1:
			Buses.objects.filter(travels=travels).update(one="#1FACD4")
		elif id==2:
			Buses.objects.filter(travels=travels).update(two="#1FACD4")
		elif id==3:
			Buses.objects.filter(travels=travels).update(three="#1FACD4")
		elif id==4:
			Buses.objects.filter(travels=travels).update(four="#1FACD4")
		elif id==5:
			Buses.objects.filter(travels=travels).update(five="#1FACD4")
		elif id==6:
			Buses.objects.filter(travels=travels).update(six="#1FACD4")
		elif id==7:
			Buses.objects.filter(travels=travels).update(seven="#1FACD4")
		elif id==8:
			Buses.objects.filter(travels=travels).update(eight="#1FACD4")
		elif id==9:
			Buses.objects.filter(travels=travels).update(nine="#1FACD4")
		elif id==10:
			Buses.objects.filter(travels=travels).update(ten="#1FACD4")
		elif id==11:
			Buses.objects.filter(travels=travels).update(elven="#1FACD4")
		elif id==12:
			Buses.objects.filter(travels=travels).update(twelve="#1FACD4")
		elif id==13:
			Buses.objects.filter(travels=travels).update(thirtn="#1FACD4")
		elif id==14:
			Buses.objects.filter(travels=travels).update(fouthn="#1FACD4")
		elif id==15:
			Buses.objects.filter(travels=travels).update(fivethn="#1FACD4")
		elif id==16:
			Buses.objects.filter(travels=travels).update(sixthn="#1FACD4")
		email=request.session['email']
		request.session['travel']=travels
		buses=Buses.objects.filter(Q(travels__iexact=travels))
		return render(request,'buspaymentpage.html',{'buses':buses,'email':email,'id':id})

def forgotpassword(request):
	return render(request,'forgotpassword.html')
def confirmpayment(request):
	travels=request.session['travel']
	buses=Buses.objects.filter(Q(travels__iexact=travels))
	return render(request,'buscardpayment.html',{'v':buses,'travel':travels,})

def resetpassword(request):
	if request.method=="POST":
		email=request.POST["email"]
		opwd=request.POST["opwd"]
		npwd=request.POST["npwd"]
		r=User.objects.filter(Q(email__iexact=email) & Q(password__iexact=opwd)).update(password=npwd)
		if r:
			return render(request,'forgotpassword.html',{'msg':"password Udpated "})	
		else:
			return render(request,'forgotpassword.html',{'msg':"Password Not Udpated!"})
	else: 
		return HttpResponse("Not Successful")

"""def sam(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		m=request.session['email']
		del request.session['email']
		return HttpResponse("deleted")"""

"""def sam(request):
	distance_matrix = np.array([
    [0,  5, 4, 10],
    [5,  0, 8,  5],
    [4,  8, 0,  3],
    [10, 5, 3,  0]])
	permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
	return HttpResponse(distance)"""
def sam(request):
	#env = Buses.objects.filter(travels="Morning Star Travels").values_list('fare', flat=True)[0]
	#env=int(env)+2;
	#matrix=[[1,env],[2,env]]
	d=request.POST["num"]
	bu=request.POST["budget"]
	if d!="":
		days=int(d)
	if bu!="":
		budget=int(bu)
	dcount=0
	bcount=0
	places=TouristPlaces.objects.all()
	a=[]
	b=[]
	c=[]
	for i in places:
		name=i.place
		time=i.time
		cost=i.cost
		if bu!="":
			r=cost/time
		else:
			r=time/cost
		#print(name,cost)
		if name in request.POST:
			b.append([name,time,cost,r])
	
	b.sort(key=lambda b:b[3])
	if d=="" and bu!="":
		print(b)
		rows=len(b)
		print("rows",rows)
		for j in range(rows):
			#print(j)
			if bcount+b[j][2]<=budget:
				print("inside")
				c.append([b[j][0],b[j][1],b[j][2],b[j][3]])
				bcount=bcount+b[j][2]
				print(bcount)
	elif d!="" and bu=="":
		print(b)
		rows=len(b)
		print("rows",rows)
		for j in range(rows):
			#print(j)
			if dcount+b[j][1]<=days:
				c.append([b[j][0],b[j][1],b[j][2],b[j][3]])
				dcount=dcount+b[j][1]
				print(dcount)
	elif d!="" and bu!="":
		print("both not equals case")
		print(b)
		rows=len(b)
		print("rows",rows)
		for j in range(rows):
			#print(j)
			if dcount+b[j][1]<=days and bcount+b[j][2]<=budget:
				c.append([b[j][0],b[j][1],b[j][2],b[j][3]])
				dcount=dcount+b[j][1]
				bcount=bcount+b[j][2]
				print("b",bcount)
				print("d",dcount)
	elif d=="" and bu=="":
		return HttpResponse("You Did not fill any field")

	print(dcount)
	print(bcount)
	request.session['plan']=c
	return render(request,'planpage.html',{'plan':c,'days':dcount,'budget':bcount,})			
	return HttpResponse(b)
		


def logout(request):
	del request.session['email']
	form = UserLoginForm()
	return render(request,'home.html')

def signuppage(request):
	form = userdataForm()
	if request.method == 'POST':
		form = userdataForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'signup.html',{'msg':"Account Created",'form':form,})
		else:
			form = userdataForm() 
	return render(request,'signup.html',{'form':form})

def tourspage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		tours=Tours.objects.all()
		return render(request,'tourspage.html',{'tours':tours})

def booked(request):
	return render(request,'confirmpayment.html')

def tourinformation(request,location):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		tour=Tours.objects.filter(Q(location__iexact=location))
		return render(request,'tourinformation.html',{'tour':tour})
def tourconfirm(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		return render(request,'tourconfirm.html',)

def bookbuspage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		buses=Buses.objects.all()
		return render(request,'bookbuspage.html',{'buses':buses})

def bookflightpage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		flights=Flights.objects.all()
		return render(request,'bookflightpage.html',{'flights':flights})

def hospitalitypage(request):
	if 'email' not in request.session:
		return HttpResponse("<h1 align='center'>Session Expired</h1>")
	else:
		return render(request,'hospitalitypage.html')

def aboutuspage(request):
		return render(request,'aboutus.html')
def lr(request):
	return render(request,'linear_regression.html')
def demodate(request):
	form=DemoDateForm()
	return render(request,'demodatedisplay.html',{'form':form})
def flightticketdetails(request,flight):
	request.session['flight']=flight
	return render(request,'flightticket.html')
def flightpaymentpage(request):
	f=request.session['flight']
	flight=Flights.objects.filter(Q(flight__iexact=f))
	return render(request,'flightpaymentpage.html',{'f':f,'flight': flight})

def flightticketconfirm(request):
	f=request.POST['flight']
	c=request.POST['cl']
	n=request.POST['nt']
	fare=Flights.objects.filter(flight=f).values('fare')
	flight=Flights.objects.filter(Q(flight__iexact=f))
	email=request.session['email']
	return render(request,'flightticketconfirm.html',{'email':email,'fare':type(fare),})

def createtour(request):
	places=TouristPlaces.objects.all()
	return render(request,'createtour.html',{'places':places})

def shortpath(request):
	plan=request.session['plan']
	print(plan)
	rows=len(plan)
	print(rows)
	d=0
	matrix=[]
	temp=[]
	for p1 in range(rows):
		#for p3 in range(p1+1):
				#temp.append(0)
		for p2 in range(rows):
			#if p2<p1+1:
				#temp.append(matrix[p1+1][0])
			#else:
			#print(p1,p2)
			if p1==p2:
				temp.append(0)
			else:
				fp=plan[p1][0]
				tp=plan[p2][0]
			#print(p1,p2)
				i = Distances.objects.filter((Q(fromplace__iexact=fp) & Q(toplace__iexact=tp)) |(Q(fromplace__iexact=tp) & Q(toplace__iexact=fp))   ).values('distance')[0]
				env = i['distance']
				temp.append(env)
		#print(temp)
		matrix.append(temp)
		temp=[]
	#d=Distances.objects.filter(fromplace=plan[0][0]).values('distance')[0]
	
	#for p in range(rows):
		#d=Distances.objects.filter(fromplace=plan[p][0]).values('distance')
		#print(d)
	distance_matrix = np.array(matrix)
	permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
	#return HttpResponse(distance)
	print(permutation,distance)
	newplan=[]
	for t1 in range(rows):
		newplan.append(plan[permutation[t1]])
	return render(request,'shortpath.html',{'newplan':newplan})
