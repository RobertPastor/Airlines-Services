

 cd "C:\Users\rober\Documents\04 - Workspace\flight-profile"
 
# list all available commands

python manage.py makemigrations -a airlines
python manage.py migrate -a airlines

python manage.py -a airlines --help

# run one command
python manage.py WayPointsDatabaseLoad -a flight-profile 

python manage.py AirportsDatabaseLoad -a flight-profile 
