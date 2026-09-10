
from xml.dom import minidom

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import xmltodict

from django.template import loader
from django.core import serializers
from django.http import HttpResponse , JsonResponse

from airlines.models import Airline, AirlineRoute
from trajectory.models import  AirlineAirport

from trajectory.views.utils import getAirlineRunWaysFromDB , getAirlineAircraftsFromDB, getAirlineRoutesFromDB
from trajectory.views.utils import getAircraftFromRequest, getRouteFromRequest, getAdepRunwayFromRequest, getAdesRunwayFromRequest 
from trajectory.views.utils import getMassFromRequest , getFlightLevelFromRequest , getReducedClimbPowerCoeffFromRequest, getDirectRouteFromRequest

from trajectory.models import BadaSynonymAircraft
from trajectory.BadaAircraftPerformance.BadaAircraftJsonPerformanceFile import AircraftJsonPerformance

from trajectory.Guidance.FlightPathFile import FlightPath

from trajectory.GuidanceOpenap.FlightPathOpenapFile import FlightPathOpenap
from trajectory.Openap.AircraftMainFile import OpenapAircraft
from trajectory.GuidanceOpenap.FlightPathOpenapFile import FlightPathOpenap

from trajectory.Environment.Earth.EarthFile import Earth
from trajectory.Environment.Atmosphere.AtmosphereFile import Atmosphere
from trajectory.Environment.Airports.AirportDatabaseFile import AirportsDatabase
from trajectory.Environment.Runways.RunWaysDatabaseFile import RunWaysDataBase
from trajectory.Environment.WayPoints.WayPointsDatabaseFile import WayPointsDatabase

# Create your views here.
def indexTrajectory(request):
    # return HttpResponse('Hello from Python!')
    template = loader.get_template('./index.html')

    siteMessages = []
    '''    for siteMessage in SiteMessage.objects.all().order_by("event_date"):
        if siteMessage.active == True:
            siteMessages.append(siteMessage)
    '''            
    siteMessages = serializers.serialize('json', siteMessages)
    context = {'siteMessages' : siteMessages}
    return HttpResponse(template.render(context, request))
    
def getPlaceMarks(XmlDocument):
    placeMarksList = []
    #print ( BASE_DIR )
    #filePath = os.path.join ( BASE_DIR , os.path.join ( "trajectory/static/kml"  , fileName ) )
    
    parseXml = minidom.parseString(XmlDocument)
    #use getElementsByTagName() to get tag
    placeMarks = parseXml.getElementsByTagName('Placemark')
    for placeMark in placeMarks:
            name = ""
            try:
                name = placeMark.getElementsByTagName("name")[0].childNodes[0].data
                #print ( name )
            except Exception:
                name = ""
            point = placeMark.getElementsByTagName("Point")[0]
            coordinates = point.getElementsByTagName("coordinates")[0].childNodes[0].data
            #print ( coordinates )
            placeMarksList.append({ 
                "name": name,
                "longitude": str(coordinates).split(",")[0],
                "latitude": str(coordinates).split(",")[1],
                "height": str(coordinates).split(",")[2]
            })
   
    #logger.info ( "length place marks = {0}".format(len ( placeMarksList )) )
    return placeMarksList
    
def launchFlightProfile(request , airlineName , BadaWrap ):
    logger.info  ("views Flight Profile - launch Flight Profile - with airline = {0}".format(airlineName))
    if (request.method == 'GET'):
        
        logger.info ( "views Flight Profile - Legacy or WRAP mode = {0}".format( BadaWrap ))
        airline = Airline.objects.filter(Name=airlineName).first()
        if (airline):
            airlineAircraftsList = getAirlineAircraftsFromDB(airline , BadaWrap) 
            airlineRoutesList    = getAirlineRoutesFromDB(airline)
            airlineRunWaysList   = getAirlineRunWaysFromDB()
            logger.info( "views Flight Profile - length of aircrafts list = {0}".format( len( airlineAircraftsList ) ) )
            if not airlineAircraftsList:
                return JsonResponse({'errors': "aircrafts list is empty for airline with name {0}".format(airlineName)})
            if not airlineRoutesList:
                return JsonResponse({'errors': "routes list is empty for airline with name {0}".format(airlineName)})
            if not airlineRunWaysList:
                return JsonResponse({'errors': "runways list is empty for airline with name {0}".format(airlineName)})

            response_data = {
                'airlineAircrafts': airlineAircraftsList,
                'airlineRoutes'   : airlineRoutesList,
                'airlineRunWays'  : airlineRunWaysList
                }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'errors': "airline with name {0} not found".format(airlineName)})
    else:
        return JsonResponse({'errors': "expecting GET method"})
    
def getAirport(airportICAOcode):
    for airport in AirlineAirport.objects.all():
        if (airport.AirportICAOcode == airportICAOcode ):
            return { "AirportICAOcode" : airport.AirportICAOcode ,
                     "AirportName"     : airport.AirportName,
                     "Longitude"       : airport.Longitude,
                     "Latitude"        : airport.Latitude         }
    return {}

''' legacy computation with enhanced BADA data available as a Json schema '''
def computeBadaFlightProfile(request , airlineName ):
        aircraftICAOcode = getAircraftFromRequest(request)
        badaAircraft = BadaSynonymAircraft.objects.all().filter(AircraftICAOcode=aircraftICAOcode).first()
        
        if not badaAircraft:
            logger.debug ("aircraft with ICAO code = {0} not found".format(aircraftICAOcode))
            response_data = { 'errors' : 'Aircraft with ICAO code {0} not found - please select another aircraft'.format(aircraftICAOcode)}
            return JsonResponse(response_data)
        
        if ( badaAircraft and badaAircraft.aircraftJsonPerformanceFileExists()):
            
            airlineRoute = getRouteFromRequest(request)
                                    
            departureAirportICAOcode = str(airlineRoute).split("-")[0]
            departureAirportRunWayName = getAdepRunwayFromRequest(request)
            
            arrivalAirportICAOcode = str(airlineRoute).split("-")[1]
            arrivalAirportRunWayName = getAdesRunwayFromRequest(request)
            
            takeOffMassKg = getMassFromRequest(request)
            cruiseFLfeet = getFlightLevelFromRequest(request)
            
            reducedClimbPowerCoeff = 0.0
            try:
                reducedClimbPowerCoeff = getReducedClimbPowerCoeffFromRequest(request)
                reducedClimbPowerCoeff = float(reducedClimbPowerCoeff)
            except:
                reducedClimbPowerCoeff = 0.0
                
            ''' 1st April 2024 - checkbox to fly direct route '''
            direct = getDirectRouteFromRequest(request)
            
            airline = Airline.objects.filter(Name=airlineName).first()
            if (airline):
                airlineRoute = AirlineRoute.objects.filter(airline = airline, DepartureAirportICAOCode = departureAirportICAOcode, ArrivalAirportICAOCode=arrivalAirportICAOcode).first()
                if (airlineRoute):
                    logger.debug( airlineRoute )
                    '''  use run-ways defined in the page '''
                    routeAsString = airlineRoute.getRouteAsString(AdepRunWayName = departureAirportRunWayName, AdesRunWayName = arrivalAirportRunWayName, direct=direct)
                    ''' compute direct route when requested '''
                    #routeAsString = airlineRoute.getDirectRouteAsString( AdepRunWayName = departureAirportRunWayName, AdesRunWayName = arrivalAirportRunWayName )
                    
                    acPerformance = AircraftJsonPerformance(aircraftICAOcode, badaAircraft.getAircraftPerformanceFile())
                    if acPerformance.read():
                        flightPath = FlightPath(
                                        route                  = routeAsString, 
                                        aircraftICAOcode       = aircraftICAOcode,
                                        RequestedFlightLevel   = float ( cruiseFLfeet ) / 100., 
                                        cruiseMach             = acPerformance.getMaxOpMachNumber(), 
                                        takeOffMassKilograms   = float(takeOffMassKg) ,
                                        reducedClimbPowerCoeff = float(reducedClimbPowerCoeff) )
                        
                        flightPath.computeFlight(deltaTimeSeconds = 1.0)
                        
                        logger.debug ( "=========== Flight Plan create output files  =========== " )
                        csvAltitudeMSLTimeGroundTrack = flightPath.createCsvAltitudeTimeProfile()
                        
                        kmlXmlDocument = flightPath.createKmlXmlPureDocument()
                        if ( kmlXmlDocument and csvAltitudeMSLTimeGroundTrack ):
                            logger.debug ( "=========== Flight Plan end  =========== "  )
                                                
                            response_data = {
                                        'kmlXMLjson'         : xmltodict.parse( kmlXmlDocument ),
                                        'placeMarks'         : getPlaceMarks(kmlXmlDocument) ,
                                        'csvAltitudeMSLtime' : csvAltitudeMSLTimeGroundTrack
                                        }
                            return JsonResponse(response_data)
                        else:
                            logger.debug ('Error while retrieving the KML document')
                            response_data = {'errors' : 'Error while retrieving the KML document'}
                            return JsonResponse(response_data)
                    else:
                        response_data = {'errors' : 'Error while reading aircraft performance file = {0}'.format(badaAircraft.getAircraftPerformanceFile())}
                        return JsonResponse(response_data)
                else:
                    logger.debug ('airline route not found = {0}'.format(airlineRoute))
                    response_data = { 'errors' : 'Airline route not found = {0}'.format(airlineRoute)}
                    return JsonResponse(response_data)
            else:
                response_data = {
                    'errors' : 'Airline not found = {0}'.format(airlineName)}
                return JsonResponse(response_data)
        else:
            logger.debug ("aircraft with ICAO code = {0} not found".format(aircraftICAOcode))
            logger.debug ("or aircraft performance file = {0} not found".format(badaAircraft))
            response_data = {
                'errors' : 'Aircraft performance file {0} not found - please select another aircraft'.format(aircraftICAOcode)}
            return JsonResponse(response_data)

def computeWrapFlightProfile( request , airlineName ):
    aircraftICAOcode = getAircraftFromRequest(request).lower()
    logging.info( aircraftICAOcode )
    
    earth = Earth()
    atmosphere = Atmosphere()

    airportsDatabase = AirportsDatabase()
    assert airportsDatabase.readAsDict()
        
    runwaysDataBase = RunWaysDataBase()
    assert runwaysDataBase.read()
        
    waypointsDataBase = WayPointsDatabase()
    assert waypointsDataBase.read()

    ac = OpenapAircraft( aircraftICAOcode , earth , atmosphere , initialMassKilograms = None)
    logging.info( ac.getAircraftName())
    
    airlineRoute = getRouteFromRequest(request)
    logging.info( airlineRoute )
                                    
    departureAirportICAOcode = str(airlineRoute).split("-")[0]
    departureAirportRunWayName = getAdepRunwayFromRequest(request)
            
    arrivalAirportICAOcode = str(airlineRoute).split("-")[1]
    arrivalAirportRunWayName = getAdesRunwayFromRequest(request)
            
    takeOffMassKg = getMassFromRequest(request)
    cruiseFlightLevel = float ( getFlightLevelFromRequest(request) ) / 100.0
    
    targetCruiseMach = ac.getMaximumSpeedMmoMach()
    logging.info( "target cruise mach = {0:.2f} ".format( targetCruiseMach ) )
    
    airline = Airline.objects.filter(Name=airlineName).first()
    if (airline):

        airlineRoute = AirlineRoute.objects.filter(airline = airline, DepartureAirportICAOCode = departureAirportICAOcode, ArrivalAirportICAOCode=arrivalAirportICAOcode).first()
        if (airlineRoute):
            logger.debug( airlineRoute )
            
            ''' 1st April 2024 - checkbox to fly direct route '''
            direct = getDirectRouteFromRequest(request)
 
            '''  use run-ways defined in the page '''
            routeAsString = airlineRoute.getRouteAsString(AdepRunWayName = departureAirportRunWayName, 
                                                          AdesRunWayName = arrivalAirportRunWayName, 
                                                          direct = direct)

            ''' try with direct route '''
            logging.info ( "Trajectory Compute Wrap - " + routeAsString )
            flightPath = FlightPathOpenap(
                        strRoute               = routeAsString , 
                        aircraftICAOcode       = aircraftICAOcode.lower() ,
                        RequestedFlightLevel   = float(cruiseFlightLevel) , 
                        cruiseMach             = float(targetCruiseMach) , 
                        takeOffMassKilograms   = float(takeOffMassKg) ,
                        reducedClimbPowerCoeff = 0.0 ,
                        earth                  = earth ,
                        atmosphere             = atmosphere ,
                        airportsDatabase       = airportsDatabase ,
                        runwaysDataBase        = runwaysDataBase ,
                        waypointsDatabase      = waypointsDataBase ,
                        directRoute            = False )
            try:
                flightPath.computeFlight(deltaTimeSeconds = 1.0)
                csvAltitudeMSLTimeGroundTrack = flightPath.createCsvAltitudeTimeProfile()
                kmlXmlDocument                = flightPath.createKmlXmlPureDocument()
                
                if ( kmlXmlDocument and csvAltitudeMSLTimeGroundTrack ):
                    logger.debug ( "=========== Flight Plan end  =========== "  )
                                                
                    response_data = {'kmlXMLjson'         : xmltodict.parse( kmlXmlDocument ),
                                     'placeMarks'         : getPlaceMarks(kmlXmlDocument) ,
                                     'csvAltitudeMSLtime' : csvAltitudeMSLTimeGroundTrack
                                        }
                    return JsonResponse(response_data)
                else:
                    response_data = {'errors' : 'Error while retrieving the KML document'}
                    return JsonResponse(response_data)
            except Exception as e:
                logging.error("Trajectory Compute Wrap - Exception = {0}".format( str(e ) ) )
                response_data = { 'errors' : 'Trajectory Compute Wrap - Exception = {0}'.format( str(e) ) }
                return JsonResponse(response_data)
        else:
            response_data = { 'errors' : 'Airline route not found = {0}'.format(airlineRoute)}
            return JsonResponse(response_data)
    else:
        response_data = { 'errors' : 'Airline not found = {0}'.format(airlineName)}
        return JsonResponse(response_data)

''' compute flight profile for LEGACY performance model and for WRAP OpenAp performance model '''
def computeFlightProfile( request, airlineName , BadaWrap ):

    logger.setLevel(logging.INFO)
    logging.info ("compute Flight Profile - for airline = {0}".format(airlineName))
    logging.info ("compute Flight Profile - Legacy - Wrap = {0}".format(BadaWrap))
    
    #routeWayPointsList = []
    if (request.method == 'GET'):
        airline = Airline.objects.filter(Name=airlineName).first()
        if (airline):
            if BadaWrap == "BADA": 
                return computeBadaFlightProfile(request , airlineName)
            else:
                return computeWrapFlightProfile(request, airlineName)
        else:
            response_data = { 'errors' : 'Airline not found = {0}'.format(airlineName)}
            return JsonResponse(response_data)
    else:
        response_data = { 'errors': "expecting GET method - received = {0}".format ( ) }
        return JsonResponse( response_data )
