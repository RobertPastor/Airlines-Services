Each time a new route is added, there is the need to add the waypoints.xlsx database.

The route obtained from the http://rfinder.asalink.net/free/autoroute_rtx.php
can be easily pasted in this EXCEL file

## the WayPoints.xlsx file is created using the following commands
## that is available here
C:\Users\rober\git\Airlines-Services\Airlines-Services\airlines\management\commands


-> python manage.py WayPointsXlsxFileCreate
-> the WayPoints.xlsx file now contains all WayPoints / fixes as extracted from the routes
C:\Users\rober\git\Airlines-Services\Airlines-Services\airlines\management\commands\AirlineRoutesWayPoints

-> defined by a departure and an arrival airport

example  : AirlineRoute-LIBD-LFPO.xlsx