
from django.core.management.base import BaseCommand
from airlines.management.commands.AirlineRoutes.AirlineRoutesAirportsReaderNew import AirlineRoutesDataBaseXlsx

class Command(BaseCommand):
    help = 'Fill the Airline routes table'
    def handle(self, *args, **options):
        # routes database -> all Departure and arrival pairs for the airline routes
        airlineRoutesDB = AirlineRoutesDataBaseXlsx()
        if (airlineRoutesDB.exists()):
            print("airline routes database exists")
            ret = airlineRoutesDB.createAirlineRoutes()
            print ("read airline routes database result = {0}".format(ret))
        else:
            print("airline routes database does not exists")
        return
    