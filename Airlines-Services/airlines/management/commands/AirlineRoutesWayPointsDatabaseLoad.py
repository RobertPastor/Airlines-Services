
from django.core.management.base import BaseCommand
from airlines.management.commands.AirlineRoutesWayPoints.AirlineRoutesWayPointsReaderNew import AirlineRoutesWayPointsDatabaseXlsx
from airlines.models import AirlineRouteWayPoints

class Command(BaseCommand):
    help = 'Reads the WayPoints of the Routes '
    ''' waypoints from the routes are next moved to an input file XLSX that is the truth for all fix / waypoints '''
    def handle(self, *args, **options):
        
        AirlineRouteWayPoints.objects.all().delete()
        
        airlineRoutesWayPointsDatabaseXlsx = AirlineRoutesWayPointsDatabaseXlsx()
        if (airlineRoutesWayPointsDatabaseXlsx.exists()):
            ret = airlineRoutesWayPointsDatabaseXlsx.read()
            if ret:
                airlineRoutesWayPointsDatabaseXlsx.insertWayPointsDatabase()
                
        #wayPointsDatabase.dropDuplicates()
        return
        
        
            
    
    