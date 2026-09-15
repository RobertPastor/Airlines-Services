'''
Created on 4 sept. 2022

@author: robert
'''

from django.http import  JsonResponse
from airlines.models import Airline
from trajectory.views.utils import getAirlineRoutesFromDB

import logging
logger = logging.getLogger(__name__)

def getAirlineRoutes(request , airlineName):
    
    if (request.method == 'GET'):
        
        airline = Airline.objects.filter(Name=airlineName).first()
        if airline:
            airlineRoutes = getAirlineRoutesFromDB(airline)
            if airlineRoutes:
                response_data = { 'airlineRoutes' : airlineRoutes }
            else:
                response_data = {'errors': "airline with name {0} - no routes found".format(airlineName)}
            return JsonResponse( response_data )
        else:
            response_data = {'errors': "airline with name {0} not found".format(airlineName)}
            return JsonResponse(response_data)

    else:
        response_data = {'errors': "expecting GET method - received = {0}".format(request.method)}
        return JsonResponse(response_data)