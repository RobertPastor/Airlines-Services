

## waypoints are managed in a specific way
## first all airports are loaded in the database
## then all routes (departure -> arrival airports) for each airline are loaded

## the system ensures the the airports used by each airline is effectively defined in the world wide CSV airport database

## the process to analyse all routes, this process ends in the creation of an EXCEL file with all the waypoints / fixes
## as waypoints / fix are not specific to an airline , this new database is shared among all airlines

## the newly created WayPoints.xlsx file needs to be moved 'manually' 
## from the "airlines" django application to the "trajectory" django application 
## to allow for loading of all waypoints in the Djngo applicative database (database based upon Django models)

## process order
## step one 

-> 1.0 run -> python manage.py AirlineRoutesWayPointsDatabaseLoad
-> 1.1 check the database and the "airlines_airlineroutewaypoints

-> 2.0 run -> python manage.py WayPointsXlsxFileCreate
-> 2.1 check the newly created file WayPoints.xlsx in the folling folder
C:\Users\rober\git\Airlines-Services\Airlines-Services\airlines\management\commands\AirlineRoutesWayPoints 

-> 2.2 move this newly created file (that should containing newly added waypoints) to the trajectory application here
C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\WayPoints

-> 3.0 run -> python manage.py WayPointsDatabaseLoad
-> 3.1 check the database and the following table -> trajectory_airlinewaypoint

## if a new airline route was added including the fix list then it should be possible to see the new fixes on the globe