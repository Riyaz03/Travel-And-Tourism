from django.db import models

class User(models.Model):
	userid = models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=100,blank=False)
	lastname=models.CharField(max_length=100,blank=False)
	email=models.EmailField(blank=False)
	gender_choices=(('Male','Male'),('FeMale','FeMale'))
	gender=models.CharField(max_length=100,blank=False,choices=gender_choices)
	location=models.CharField(max_length=100,blank=False)
	age=models.IntegerField(blank=False)
	location=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table="userdata_table"

class UserLogin(models.Model):
	email=models.EmailField(blank=False)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table="userlogin_table"

class DemoDate(models.Model):
	name=models.CharField(max_length=10,blank=False)
	demodate=models.DateTimeField(blank=False)
	class Meta:
		db_table="demodata_table"

class Buses(models.Model):
	travels=models.CharField(max_length=50,blank=False)
	departure_timeHours=models.CharField(max_length=2,blank=False)
	departure_timeMinutes=models.CharField(max_length=2,blank=False)
	departure_palce=models.CharField(max_length=50,blank=False)
	arrival_timeHours=models.CharField(max_length=2,blank=False)
	arrival_timeMinutes=models.CharField(max_length=2,blank=False)
	arrival_place=models.CharField(max_length=50,blank=False)
	duration=models.CharField(max_length=25,blank=False)
	fare=models.CharField(max_length=20,blank=False)
	seats_available=models.IntegerField(blank=False)
	ac_sleeper=models.CharField(max_length=20,blank=False)
	bus_num=models.CharField(max_length=15,blank=False,default="AP04BN5444")
	date=models.CharField(max_length=10,blank=False,default="01/01/2021")
	day=models.CharField(max_length=10,blank=False,default="Friday")
	one=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	two=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	three=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	four=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	five=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	six=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	seven=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	eight=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	nine=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	ten=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	elven=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	twelve=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	thirtn=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	fouthn=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	fivethn=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	sixthn=models.CharField(max_length=10,blank=False,default="#DDF4EC")
	class Meta:
		db_table="buses_table"

class Flights(models.Model):
	flight=models.CharField(max_length=50,blank=False)
	departure_timeHours=models.CharField(max_length=2,blank=False)
	departure_timeMinutes=models.CharField(max_length=2,blank=False)
	departure_palce=models.CharField(max_length=50,blank=False)
	arrival_timeHours=models.CharField(max_length=2,blank=False)
	arrival_timeMinutes=models.CharField(max_length=2,blank=False)
	arrival_place=models.CharField(max_length=50,blank=False)
	duration=models.CharField(max_length=25,blank=False)
	fare=models.CharField(max_length=20,blank=False)
	seats_available=models.IntegerField(blank=False)
	date=models.CharField(max_length=10,blank=False,default="01/01/2021")
	day=models.CharField(max_length=10,blank=False,default="Wednesday")
	"""sclass_choices=(('Economy','Economy'),('Pre.Economy','Pre.Economy'),('Business','Business'))
	sclass=CharField(max_length=100,blank=False,choices=sclass_choices)"""
	class Meta:
		db_table="flights_table"

class Tours(models.Model):
	location=models.CharField(max_length=100,blank=False)
	touristplces_covered=models.CharField(max_length=500,blank=False)
	hotel=models.CharField(max_length=150,blank=False)
	cost=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table="Tours"

class VisitingData(models.Model):
	place=models.CharField(max_length=100,blank=False)
	population=models.PositiveIntegerField()
	class Meta:
		db_table="touristsData_table"

class TravelsData(models.Model):
	travels=models.CharField(max_length=100,blank=False)
	population=models.PositiveIntegerField()
	class Meta:
		db_table="TravelsData_table"

class SeasonsData(models.Model):
	season=models.CharField(max_length=100,blank=False)
	population=models.PositiveIntegerField()
	class Meta:
		db_table="SeasonalData"

class TouristPlaces(models.Model):
	place=models.CharField(max_length=100,blank=False)
	cost=models.PositiveIntegerField(blank=False)
	time=models.PositiveIntegerField(blank=False)
	state=models.CharField(max_length=100,blank=False,default="None")
	class Meta:
		db_table="touristplaces"

class Distances(models.Model):
	fromplace=models.CharField(max_length=100,blank=False)
	toplace=models.CharField(max_length=100,blank=False)
	distance=models.PositiveIntegerField(blank=False)
	#cost=models.PositiveIntegerField(blank=False)
	class Meta:
		db_table="distances"
		
