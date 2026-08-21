
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


$ python manage.py makemigrations
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
No changes detected
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$ python manage.py migrate
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
Operations to perform:
  Apply all migrations: admin, airlines, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying airlines.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$ 
