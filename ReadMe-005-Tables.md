
## migrate

$ python manage.py migrate
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
  Your models in app(s): 'airlines' have changes that are not yet reflected in a migration, and so won't be applied.
  Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## make migrations

$ python manage.py makemigrations
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
Migrations for 'airlines':
  airlines\migrations\0001_initial.py
    + Create model Airline
    + Create model User
    + Create model AirlineAircraft
    + Create model AirlineRoute
    + Create model AirlineCosts
    + Create model AirlineRouteWayPoints
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## migrate 

$ python manage.py migrate
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
Operations to perform:
  Apply all migrations: admin, airlines, auth, contenttypes, sessions
Running migrations:
  Applying airlines.0001_initial... OK
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$
