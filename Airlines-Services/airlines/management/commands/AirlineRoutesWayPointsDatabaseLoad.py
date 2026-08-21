
from django.core.management.base import BaseCommand
from airlines.management.commands.AirlineRoutesWayPoints.AirlineRoutesWayPointsReaderNew import AirlineRoutesWayPointsDatabaseXlsx
from airlines.models import AirlineRouteWayPoints

class Command(BaseCommand):
    help = 'Reads the WayPoints of the Routes '

    def handle(self, *args, **options):
        
        AirlineRouteWayPoints.objects.all().delete()
        
        airlineRoutesWayPointsDatabaseXlsx = AirlineRoutesWayPointsDatabaseXlsx()
        if (airlineRoutesWayPointsDatabaseXlsx.exists()):
            pass
            ret = airlineRoutesWayPointsDatabaseXlsx.read()
            
            if ret:
                airlineRoutesWayPointsDatabaseXlsx.insertWayPointsDatabase()
                
        #wayPointsDatabase.dropDuplicates()
        return
        
        
            
    
    