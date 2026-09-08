'''
Created on 4 juin 2023

@author: robert
'''

from django.core.management.base import BaseCommand
from trajectory.management.commands.SidStar.SidStarDatabaseLoader import SidStarLoaderOne

class Command(BaseCommand):
    help = 'Reads the SID STAR waypoints and write them a Django table'
    def handle(self, *args, **options):
        
        ''' clear database only on purpose '''
        #AirlineStandardDepartureArrivalRoute.objects.all().delete()
        # SID
        loaderOne = SidStarLoaderOne( isSID = True , 
                                    departureOrArrivalAirportICAO = "KLAX" , 
                                    FirstLastWayPointName = "SLI" , 
                                    RunWayStr = "24R" )
        if (loaderOne.exists()):
            ret = loaderOne.load()
            print ("SID STAR loading result = {0}".format(ret))
        else:
            print ("SID STAR does not exists")

        # STAR
        loaderTwo = SidStarLoaderOne( isSID = False , 
                                   departureOrArrivalAirportICAO = "KATL" , 
                                   FirstLastWayPointName = "MEM" , 
                                   RunWayStr = "26L" )
        if (loaderTwo.exists()):
            ret = loaderTwo.load()
            print ("SID STAR loading result = {0}".format(ret))
        else:
            print ("SID STAR does not exists")

        # SID - Departure LFPG - Charles de Gaulle
        loaderThree = SidStarLoaderOne( isSID = True , 
                                    departureOrArrivalAirportICAO = "LFPG" , 
                                    FirstLastWayPointName = "ERIXU" , 
                                    RunWayStr = "26L" )
        if (loaderThree.exists()):
            ret = loaderThree.load()
            print ("SID STAR loading result = {0}".format(ret))
        else:
            print ("SID STAR does not exists")
            
        ''' 6th August 2023 - STAR - JFK -> LUKIP - LFPG/08L '''
        loadFour = SidStarLoaderOne( isSID = False , 
                                    departureOrArrivalAirportICAO = "LFPG" , 
                                    FirstLastWayPointName = "LUKIP" , 
                                    RunWayStr = "08L" )
        if (loadFour.exists()):
            print ("acBD exists")
            ret = loadFour.load()
            print ("SID STAR loading result = {0}".format(ret))
        else:
            print ("SID STAR does not exists")
            
        ''' 8th September 2026 - SID - LIBD -> LUKIP - LFPG/08L '''
        loadFive = SidStarLoaderOne( isSID = True , 
                                    departureOrArrivalAirportICAO = "LIBD" , 
                                    FirstLastWayPointName = "PISIP" , 
                                    RunWayStr = "07" )
        if (loadFive.exists()):
            print ("acBD exists")
            ret = loadFive.load()
            print ("SID STAR loading result = {0}".format(ret))
        else:
            print ("SID STAR does not exists")