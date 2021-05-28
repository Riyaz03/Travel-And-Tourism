from django.contrib import admin
from .models import User,UserLogin,DemoDate,Buses,Flights,Tours,VisitingData,TravelsData,SeasonsData,TouristPlaces,Distances

admin.site.register(User)
admin.site.register(UserLogin)
admin.site.register(DemoDate)
admin.site.register(Buses)
admin.site.register(Flights)
admin.site.register(Tours)
admin.site.register(VisitingData)
admin.site.register(TravelsData)
admin.site.register(SeasonsData)
admin.site.register(TouristPlaces)
admin.site.register(Distances)