from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

from django.urls import  path


from airlines.views.viewsAirlineFleet import getAirlineFleet
from airlines.views.viewsAirlineRoutes import getAirlineRoutes
from airlines.views.viewsAirlineRoutesWayPoints import getRouteWayPoints

#from airlines.views.viewsAirlineCosts import getAirlineCosts, getAirlineCostsAsXlsx
#from airlines.views.viewsAirlineCostsOptimization import getAirlineCostsOptimization 
#from airlines.views.viewsAirlineCASM import getAirlineCASM , getAirlineCasmXlsx
#from airlines.views.viewsAirlineCasmOptimization import getAirlineCasmOptimization
#from airlines.views.viewsAirlineSeatMilesMaximization import getAirlineSeatsMilesMaxXlsx
#from airlines.views.viewsAirlineFuelEfficiency import getAirlineFuelEfficiencyXlsx 

from airlines.views.viewsUsers import viewUsers

app_name = "airlines"

''' 10th April 2023 - retrieve Airlines Costs as xlsx file to download  '''
urlpatterns = [
    
    path('airlineFleet/<slug:airlineName>' , getAirlineFleet , name='getAirlineFleet'),
    path('airlineRoutes/<slug:airlineName>' , getAirlineRoutes , name='getAirlineRoutes'),
    path('wayPointsRoute/<slug:Adep>/<slug:Ades>' , getRouteWayPoints , name='getRouteWayPoints'),
    #path('airlineCosts/<slug:airlineName>' , getAirlineCosts , name = 'getAirlineCosts'),
    #path('airlineCostsOptimization/<slug:airlineName>' , getAirlineCostsOptimization , name = 'getAirlineCostsOptimization'),
    #path('getAirlineCostsXlsx/<slug:airlineName>' , getAirlineCostsAsXlsx , name = 'getAirlineCostsAsXlsx'),
    #path('getAirlineCASM/<slug:airlineName>' , getAirlineCASM , name = 'getAirlineCASM'),
    #path('getAirlineCasmXlsx/<slug:airlineName>' , getAirlineCasmXlsx , name = 'getAirlineCasmXlsx'),
    #path('getAirlineCasmOptimization/<slug:airlineName>' , getAirlineCasmOptimization , name = 'getAirlineCasmOptimization'),
    #path('getAirlineSeatMilesXlsx/<slug:airlineName>' , getAirlineSeatsMilesMaxXlsx , name = 'getAirlineSeatsMilesMaxXlsx'),
    
    path('airlineFuelEfficiency/<slug:airlineName>', getAirlineFuelEfficiencyXlsx , name = 'getAirlineFuelEfficiencyXlsx'),
    path('users' , viewUsers , name = 'viewUsers')
    
]