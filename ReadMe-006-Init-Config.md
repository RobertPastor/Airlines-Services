
## after creating the tables , fill the site configuration

$ python manage.py AirlineDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
AmericanWings
EuropeanWings
IndianWings
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## check the tables in the PostGres SQL database


$ python manage.py AirlineDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
AmericanWings
EuropeanWings
IndianWings
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

## initialise the airports that are used in each Airline Route (departure and arrival)

$ python manage.py AirlineRoutesDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
airline routes database exists
Index is: 0
ID is: 0 - Airline is: AmericanWings - Departure Airport = KATL
ID is: 0 - Airline is: AmericanWings - Arrival AIrport = KLAX
route does not exist -> Atlanta-Hartsfield Jackson Intl - Los Angeles Intl
Index is: 1
ID is: 1 - Airline is: AmericanWings - Departure Airport = KJFK
ID is: 1 - Airline is: AmericanWings - Arrival AIrport = KSEA
route does not exist -> New York-John F Kennedy Intl - Seattle Tacoma Intl
Index is: 2
ID is: 2 - Airline is: AmericanWings - Departure Airport = MMMX
ID is: 2 - Airline is: AmericanWings - Arrival AIrport = KSEA
route does not exist -> Aeropuerto M▒xico Ciudad Intl - Seattle Tacoma Intl
Index is: 3
ID is: 3 - Airline is: AmericanWings - Departure Airport = KBOS
ID is: 3 - Airline is: AmericanWings - Arrival AIrport = KATL
route does not exist -> General Edward Lawrence Logan Intl - Atlanta-Hartsfield Jackson Intl
Index is: 4
ID is: 4 - Airline is: AmericanWings - Departure Airport = KIAH
ID is: 4 - Airline is: AmericanWings - Arrival AIrport = KORD
route does not exist -> Houston George Bush Intl - Chicago O'Hare Intl
Index is: 5
ID is: 5 - Airline is: AmericanWings - Departure Airport = KIAD
ID is: 5 - Airline is: AmericanWings - Arrival AIrport = KSFO
route does not exist -> Washington Dulles Airport Intl - San Francisco Intl
Index is: 6
ID is: 6 - Airline is: AmericanWings - Departure Airport = PANC
ID is: 6 - Airline is: AmericanWings - Arrival AIrport = KATL
route does not exist -> Alaska Anchorage-Ted Stevens Intl - Atlanta-Hartsfield Jackson Intl
Index is: 7
ID is: 7 - Airline is: AmericanWings - Departure Airport = KLAX
ID is: 7 - Airline is: AmericanWings - Arrival AIrport = KATL
route does not exist -> Los Angeles Intl - Atlanta-Hartsfield Jackson Intl
Index is: 8
ID is: 8 - Airline is: AmericanWings - Departure Airport = KSEA
ID is: 8 - Airline is: AmericanWings - Arrival AIrport = KJFK
route does not exist -> Seattle Tacoma Intl - New York-John F Kennedy Intl
Index is: 9
ID is: 9 - Airline is: AmericanWings - Departure Airport = KMSP
ID is: 9 - Airline is: AmericanWings - Arrival AIrport = KATL
route does not exist -> Minneapolis - Atlanta-Hartsfield Jackson Intl
Index is: 10
ID is: 10 - Airline is: AmericanWings - Departure Airport = KATL
ID is: 10 - Airline is: AmericanWings - Arrival AIrport = KBOS
route does not exist -> Atlanta-Hartsfield Jackson Intl - General Edward Lawrence Logan Intl
Index is: 11
ID is: 11 - Airline is: AmericanWings - Departure Airport = KORD
ID is: 11 - Airline is: AmericanWings - Arrival AIrport = KIAH
route does not exist -> Chicago O'Hare Intl - Houston George Bush Intl
Index is: 12
ID is: 12 - Airline is: AmericanWings - Departure Airport = KSFO
ID is: 12 - Airline is: AmericanWings - Arrival AIrport = KIAD
route does not exist -> San Francisco Intl - Washington Dulles Airport Intl
Index is: 13
ID is: 13 - Airline is: AmericanWings - Departure Airport = KATL
ID is: 13 - Airline is: AmericanWings - Arrival AIrport = PANC
route does not exist -> Atlanta-Hartsfield Jackson Intl - Alaska Anchorage-Ted Stevens Intl
Index is: 14
ID is: 14 - Airline is: AmericanWings - Departure Airport = KJFK
ID is: 14 - Airline is: AmericanWings - Arrival AIrport = LFPG
route does not exist -> New York-John F Kennedy Intl - Paris Charles-De-Gaulle France Intl
Index is: 15
ID is: 15 - Airline is: EuropeanWings - Departure Airport = LFPG
ID is: 15 - Airline is: EuropeanWings - Arrival AIrport = LPPT
route does not exist -> Charles-De-Gaulle-France - Lisbonne-Lisboa-Portugal
Index is: 16
ID is: 16 - Airline is: EuropeanWings - Departure Airport = LFPG
ID is: 16 - Airline is: EuropeanWings - Arrival AIrport = LFML
route does not exist -> Charles-De-Gaulle-France - Marseille-Provence-France
Index is: 17
ID is: 17 - Airline is: EuropeanWings - Departure Airport = LFOB
ID is: 17 - Airline is: EuropeanWings - Arrival AIrport = LHBP
route does not exist -> Paris-Beauvais-Tille - Hungary-Budapest-Listz
Index is: 18
ID is: 18 - Airline is: EuropeanWings - Departure Airport = LHBP
ID is: 18 - Airline is: EuropeanWings - Arrival AIrport = LFOB
route does not exist -> Hungary-Budapest-Listz - Paris-Beauvais-Tille
Index is: 19
ID is: 19 - Airline is: EuropeanWings - Departure Airport = LEMD
ID is: 19 - Airline is: EuropeanWings - Arrival AIrport = EDDB
route does not exist -> Madrid-Barajas - Berlin-Brandenburg
Index is: 20
ID is: 20 - Airline is: EuropeanWings - Departure Airport = LPFR
ID is: 20 - Airline is: EuropeanWings - Arrival AIrport = EBBR
route does not exist -> Faro-Portugal - Brussels-National
Index is: 21
ID is: 21 - Airline is: IndianWings - Departure Airport = VOBL
ID is: 21 - Airline is: IndianWings - Arrival AIrport = VIDP
route does not exist -> Bangalore-India - Indira Gandhi Intl New-Delhi-India
Index is: 22
ID is: 22 - Airline is: IndianWings - Departure Airport = VABB
ID is: 22 - Airline is: IndianWings - Arrival AIrport = VECC
route does not exist -> Mumbai-India - Calcutta-India
Index is: 23
ID is: 23 - Airline is: IndianWings - Departure Airport = VOMM
ID is: 23 - Airline is: IndianWings - Arrival AIrport = VIJP
route does not exist -> Chennai-India - Jaipur-India
read airline routes database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

$ python manage.py AirportsDatabaseLoad

{'Airport ID': '9412', 'Airport Name': 'Sabetha Municipal', 'City': 'Sabetha', 'Country': 'United States', 'IATA/FAA': 'K83', 'ICAO Code': 'KK83', 'LatitudeDegrees': '39.5425', 'LongitudeDegrees': '-95.4677', 'AltitudeFeet': '1330', 'TimeZone': '-6', 'DST': 'A'}
{'Airport ID': '9413', 'Airport Name': 'Mount Pleasant Regional-Faison Field', 'City': 'Mount Pleasant', 'Country': 'United States', 'IATA/FAA': 'LRO', 'ICAO Code': 'KLRO', 'LatitudeDegrees': '32.5387', 'LongitudeDegrees': '-79.4697', 'AltitudeFeet': '12', 'TimeZone': '-5', 'DST': 'A'}
{'Airport ID': '9414', 'Airport Name': 'Jimmy Carter Regional', 'City': 'Americus', 'Country': 'United States', 'IATA/FAA': 'ACJ', 'ICAO Code': 'KACJ', 'LatitudeDegrees': '32.0665', 'LongitudeDegrees': '-84.1133', 'AltitudeFeet': '468', 'TimeZone': '-5', 'DST': 'A'}
{'Airport ID': '9415', 'Airport Name': 'Weedon Field', 'City': 'Eufala', 'Country': 'United States', 'IATA/FAA': 'EUF', 'ICAO Code': 'KEUF', 'LatitudeDegrees': '31.5708', 'LongitudeDegrees': '-85.0774', 'AltitudeFeet': '285', 'TimeZone': '-6', 'DST': 'A'}
{'Airport ID': '9416', 'Airport Name': 'Saluda County', 'City': 'Saluda', 'Country': 'United States', 'IATA/FAA': '6J4', 'ICAO Code': 'K6J4', 'LatitudeDegrees': '33.5561', 'LongitudeDegrees': '-81.4768', 'AltitudeFeet': '539', 'TimeZone': '-5', 'DST': 'A'}
{'Airport ID': '9417', 'Airport Name': 'Dare County Regional', 'City': 'Manteo', 'Country': 'United States', 'IATA/FAA': 'MQI', 'ICAO Code': 'KMQI', 'LatitudeDegrees': '35.5514', 'LongitudeDegrees': '-75.4173', 'AltitudeFeet': '13', 'TimeZone': '-5', 'DST': 'A'}
{'Airport ID': '9418', 'Airport Name': 'Auburn University Regional', 'City': 'Auburn', 'Country': 'United States', 'IATA/FAA': 'AUO', 'ICAO Code': 'KAUO', 'LatitudeDegrees': '32.3691', 'LongitudeDegrees': '-85.2604', 'AltitudeFeet': '777', 'TimeZone': '-6', 'DST': 'A'}
{'Airport ID': '9419', 'Airport Name': 'Tri-Cities', 'City': 'Endicott', 'Country': 'United States', 'IATA/FAA': 'CZG', 'ICAO Code': 'KCZG', 'LatitudeDegrees': '42.0471', 'LongitudeDegrees': '-76.0578', 'AltitudeFeet': '833', 'TimeZone': '-5', 'DST': 'A'}
read airports database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

$ python manage.py 

$ python manage.py AirlineFleetDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
airline fleet database exists
Bada aircraft database read correctly = True
Index is: 0
--> row --> Airline                                AmericanWings
Aircraft ICAO                                   A320
Aircraft                                 Airbus A320
In service                                         5
Orders                                           NaN
Passengers Delta One                             NaN
Passengers First Class                          16.0
Passengers Premium Select                        NaN
Passengers Delta Confort Plus                   18.0
Passengers Main Cabin                          123.0
Passengers Total                                 157
Costs per flying hours dollars                  2840
Crew Costs per flying hours dollars             1657
TurnAround Time Minutes                           25
Refs                                            [35]
Notes                                            NaN
Name: 0, dtype: object
Airbus A320
aircraft = A320 - of airline = AmericanWings is new in the database
Airbus A320-A320
AmericanWings
Airbus A320
Index is: 1
--> row --> Airline                                                                   AmericanWings
Aircraft ICAO                                                                      A332
Aircraft                                                                Airbus A330-200
In service                                                                            5
Orders                                                                              NaN
Passengers Delta One                                                               34.0
Passengers First Class                                                              NaN
Passengers Premium Select                                                           NaN
Passengers Delta Confort Plus                                                      32.0
Passengers Main Cabin                                                             168.0
Passengers Total                                                                    234
Costs per flying hours dollars                                                     3300
Crew Costs per flying hours dollars                                                1857
TurnAround Time Minutes                                                              35
Refs                                                                               [40]
Notes                                  To be retrofitted with Premium Select seats.[41]
Name: 1, dtype: object
Airbus A330-200
aircraft = A332 - of airline = AmericanWings is new in the database
Airbus A330-200-A332
AmericanWings
Airbus A330-200
Index is: 2
--> row --> Airline                                 AmericanWings
Aircraft ICAO                                    B738
Aircraft                               Boeing 737-800
In service                                          5
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                           16.0
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                    36.0
Passengers Main Cabin                           108.0
Passengers Total                                  160
Costs per flying hours dollars                   3010
Crew Costs per flying hours dollars              1557
TurnAround Time Minutes                            25
Refs                                             [51]
Notes                                             NaN
Name: 2, dtype: object
Boeing 737-800
aircraft = B738 - of airline = AmericanWings is new in the database
Boeing 737-800-B738
AmericanWings
Boeing 737-800
Index is: 3
--> row --> Airline                                                                    AmericanWings
Aircraft ICAO                                                                       B739
Aircraft                                                                Boeing 737-900ER
In service                                                                             1
Orders                                                                              29.0
Passengers Delta One                                                                 NaN
Passengers First Class                                                              20.0
Passengers Premium Select                                                            NaN
Passengers Delta Confort Plus                                                       21.0
Passengers Main Cabin                                                              139.0
Passengers Total                                                                     180
Costs per flying hours dollars                                                      3050
Crew Costs per flying hours dollars                                                 1557
TurnAround Time Minutes                                                               25
Refs                                                                                [52]
Notes                                  29 used aircraft to enter service from 2022.[2...
Name: 3, dtype: object
Boeing 737-900ER
aircraft = B739 - of airline = AmericanWings is new in the database
Boeing 737-900ER-B739
AmericanWings
Boeing 737-900ER
Index is: 4
--> row --> Airline                                AmericanWings
Aircraft ICAO                                   A319
Aircraft                                 Airbus A319
In service                                         5
Orders                                           NaN
Passengers Delta One                             NaN
Passengers First Class                           NaN
Passengers Premium Select                        NaN
Passengers Delta Confort Plus                    NaN
Passengers Main Cabin                            NaN
Passengers Total                                 150
Costs per flying hours dollars                  2780
Crew Costs per flying hours dollars             1457
TurnAround Time Minutes                           25
Refs                                             NaN
Notes                                            NaN
Name: 4, dtype: object
Airbus A319
aircraft = A319 - of airline = AmericanWings is new in the database
Airbus A319-A319
AmericanWings
Airbus A319
Index is: 5
--> row --> Airline                                 AmericanWings
Aircraft ICAO                                    A20N
Aircraft                               Airbus A320neo
In service                                          5
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                            NaN
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                     NaN
Passengers Main Cabin                             NaN
Passengers Total                                  180
Costs per flying hours dollars                   2780
Crew Costs per flying hours dollars              1457
TurnAround Time Minutes                            25
Refs                                              NaN
Notes                                             NaN
Name: 5, dtype: object
Airbus A320neo
aircraft = A20N - of airline = AmericanWings is new in the database
Airbus A320neo-A20N
AmericanWings
Airbus A320neo
Index is: 6
--> row --> Airline                                EuropeanWings
Aircraft ICAO                                   A320
Aircraft                                 Airbus A320
In service                                         7
Orders                                           NaN
Passengers Delta One                             NaN
Passengers First Class                          16.0
Passengers Premium Select                        NaN
Passengers Delta Confort Plus                   18.0
Passengers Main Cabin                          123.0
Passengers Total                                 157
Costs per flying hours dollars                  2840
Crew Costs per flying hours dollars             1607
TurnAround Time Minutes                           25
Refs                                            [35]
Notes                                            NaN
Name: 6, dtype: object
Airbus A320
aircraft = A320 - of airline = EuropeanWings is new in the database
Airbus A320-A320
EuropeanWings
Airbus A320
Index is: 7
--> row --> Airline                                                                   EuropeanWings
Aircraft ICAO                                                                      A332
Aircraft                                                                Airbus A330-200
In service                                                                            8
Orders                                                                              NaN
Passengers Delta One                                                               34.0
Passengers First Class                                                              NaN
Passengers Premium Select                                                           NaN
Passengers Delta Confort Plus                                                      32.0
Passengers Main Cabin                                                             168.0
Passengers Total                                                                    234
Costs per flying hours dollars                                                     3300
Crew Costs per flying hours dollars                                                1807
TurnAround Time Minutes                                                              35
Refs                                                                               [40]
Notes                                  To be retrofitted with Premium Select seats.[41]
Name: 7, dtype: object
Airbus A330-200
aircraft = A332 - of airline = EuropeanWings is new in the database
Airbus A330-200-A332
EuropeanWings
Airbus A330-200
Index is: 8
--> row --> Airline                                 EuropeanWings
Aircraft ICAO                                    B738
Aircraft                               Boeing 737-800
In service                                          9
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                           16.0
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                    36.0
Passengers Main Cabin                           108.0
Passengers Total                                  160
Costs per flying hours dollars                   3010
Crew Costs per flying hours dollars              1507
TurnAround Time Minutes                            25
Refs                                             [51]
Notes                                             NaN
Name: 8, dtype: object
Boeing 737-800
aircraft = B738 - of airline = EuropeanWings is new in the database
Boeing 737-800-B738
EuropeanWings
Boeing 737-800
Index is: 9
--> row --> Airline                                                                    EuropeanWings
Aircraft ICAO                                                                       B739
Aircraft                                                                Boeing 737-900ER
In service                                                                            10
Orders                                                                              29.0
Passengers Delta One                                                                 NaN
Passengers First Class                                                              20.0
Passengers Premium Select                                                            NaN
Passengers Delta Confort Plus                                                       21.0
Passengers Main Cabin                                                              139.0
Passengers Total                                                                     180
Costs per flying hours dollars                                                      3050
Crew Costs per flying hours dollars                                                 1507
TurnAround Time Minutes                                                               25
Refs                                                                                [52]
Notes                                  29 used aircraft to enter service from 2022.[2...
Name: 9, dtype: object
Boeing 737-900ER
aircraft = B739 - of airline = EuropeanWings is new in the database
Boeing 737-900ER-B739
EuropeanWings
Boeing 737-900ER
Index is: 10
--> row --> Airline                                EuropeanWings
Aircraft ICAO                                   A319
Aircraft                                 Airbus A319
In service                                         5
Orders                                           NaN
Passengers Delta One                             NaN
Passengers First Class                           NaN
Passengers Premium Select                        NaN
Passengers Delta Confort Plus                    NaN
Passengers Main Cabin                            NaN
Passengers Total                                 150
Costs per flying hours dollars                  2780
Crew Costs per flying hours dollars             1457
TurnAround Time Minutes                           25
Refs                                             NaN
Notes                                            NaN
Name: 10, dtype: object
Airbus A319
aircraft = A319 - of airline = EuropeanWings is new in the database
Airbus A319-A319
EuropeanWings
Airbus A319
Index is: 11
--> row --> Airline                                 EuropeanWings
Aircraft ICAO                                    A20N
Aircraft                               Airbus A320neo
In service                                          5
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                            NaN
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                     NaN
Passengers Main Cabin                             NaN
Passengers Total                                  180
Costs per flying hours dollars                   2780
Crew Costs per flying hours dollars              1457
TurnAround Time Minutes                            25
Refs                                              NaN
Notes                                             NaN
Name: 11, dtype: object
Airbus A320neo
aircraft = A20N - of airline = EuropeanWings is new in the database
Airbus A320neo-A20N
EuropeanWings
Airbus A320neo
Index is: 12
--> row --> Airline                                IndianWings
Aircraft ICAO                                 A320
Aircraft                               Airbus A320
In service                                      12
Orders                                         NaN
Passengers Delta One                           NaN
Passengers First Class                        16.0
Passengers Premium Select                      NaN
Passengers Delta Confort Plus                 18.0
Passengers Main Cabin                        123.0
Passengers Total                               157
Costs per flying hours dollars                2840
Crew Costs per flying hours dollars           1517
TurnAround Time Minutes                         25
Refs                                          [35]
Notes                                          NaN
Name: 12, dtype: object
Airbus A320
aircraft = A320 - of airline = IndianWings is new in the database
Airbus A320-A320
IndianWings
Airbus A320
Index is: 13
--> row --> Airline                                                                     IndianWings
Aircraft ICAO                                                                      A332
Aircraft                                                                Airbus A330-200
In service                                                                           13
Orders                                                                              NaN
Passengers Delta One                                                               34.0
Passengers First Class                                                              NaN
Passengers Premium Select                                                           NaN
Passengers Delta Confort Plus                                                      32.0
Passengers Main Cabin                                                             168.0
Passengers Total                                                                    234
Costs per flying hours dollars                                                     3300
Crew Costs per flying hours dollars                                                1617
TurnAround Time Minutes                                                              35
Refs                                                                               [40]
Notes                                  To be retrofitted with Premium Select seats.[41]
Name: 13, dtype: object
Airbus A330-200
aircraft = A332 - of airline = IndianWings is new in the database
Airbus A330-200-A332
IndianWings
Airbus A330-200
Index is: 14
--> row --> Airline                                   IndianWings
Aircraft ICAO                                    B738
Aircraft                               Boeing 737-800
In service                                         14
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                           16.0
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                    36.0
Passengers Main Cabin                           108.0
Passengers Total                                  160
Costs per flying hours dollars                   3010
Crew Costs per flying hours dollars              1407
TurnAround Time Minutes                            25
Refs                                             [51]
Notes                                             NaN
Name: 14, dtype: object
Boeing 737-800
aircraft = B738 - of airline = IndianWings is new in the database
Boeing 737-800-B738
IndianWings
Boeing 737-800
Index is: 15
--> row --> Airline                                                                      IndianWings
Aircraft ICAO                                                                       B739
Aircraft                                                                Boeing 737-900ER
In service                                                                            15
Orders                                                                              29.0
Passengers Delta One                                                                 NaN
Passengers First Class                                                              20.0
Passengers Premium Select                                                            NaN
Passengers Delta Confort Plus                                                       21.0
Passengers Main Cabin                                                              139.0
Passengers Total                                                                     180
Costs per flying hours dollars                                                      3050
Crew Costs per flying hours dollars                                                 1407
TurnAround Time Minutes                                                               25
Refs                                                                                [52]
Notes                                  29 used aircraft to enter service from 2022.[2...
Name: 15, dtype: object
Boeing 737-900ER
aircraft = B739 - of airline = IndianWings is new in the database
Boeing 737-900ER-B739
IndianWings
Boeing 737-900ER
Index is: 16
--> row --> Airline                                IndianWings
Aircraft ICAO                                 A319
Aircraft                               Airbus A319
In service                                       5
Orders                                         NaN
Passengers Delta One                           NaN
Passengers First Class                         NaN
Passengers Premium Select                      NaN
Passengers Delta Confort Plus                  NaN
Passengers Main Cabin                          NaN
Passengers Total                               150
Costs per flying hours dollars                2780
Crew Costs per flying hours dollars           1457
TurnAround Time Minutes                         25
Refs                                           NaN
Notes                                          NaN
Name: 16, dtype: object
Airbus A319
aircraft = A319 - of airline = IndianWings is new in the database
Airbus A319-A319
IndianWings
Airbus A319
Index is: 17
--> row --> Airline                                   IndianWings
Aircraft ICAO                                    A20N
Aircraft                               Airbus A320neo
In service                                          5
Orders                                            NaN
Passengers Delta One                              NaN
Passengers First Class                            NaN
Passengers Premium Select                         NaN
Passengers Delta Confort Plus                     NaN
Passengers Main Cabin                             NaN
Passengers Total                                  180
Costs per flying hours dollars                   2780
Crew Costs per flying hours dollars              1457
TurnAround Time Minutes                            25
Refs                                              NaN
Notes                                             NaN
Name: 17, dtype: object
Airbus A320neo
aircraft = A20N - of airline = IndianWings is new in the database
Airbus A320neo-A20N
IndianWings
Airbus A320neo
read airline fleet database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


$ python manage.py NoaaWeatherStationsLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
 --- about to delete NOAA Weather Stations ---
 --- NOAA Weather Stations - delete done ---
NoaaWeatherStationsClass - final number of weather stations = 0
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

$ python manage.py RunWaysDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
RunWaysDatabase: file folder= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays
RunWaysDatabase: file path= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays\RunWays.xlsx
runwaysDB exists
C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays\RunWays.xlsx
EBBR
airport = EBBR
EBBR/01
EBBR
airport = EBBR
EBBR/07L
EBBR
airport = EBBR
EBBR/07R
EDDB
airport = EDDB
EDDB/07L
EDDB
airport = EDDB
EDDB/07R
KATL
airport = KATL
KATL/08L
KATL
airport = KATL
KATL/08R
KATL
airport = KATL
KATL/09L
KATL
airport = KATL
KATL/09R
KATL
airport = KATL
KATL/10
KBOS
airport = KBOS
KBOS/04L
KBOS
airport = KBOS
KBOS/04R
KBOS
airport = KBOS
KBOS/09
KBOS
airport = KBOS
KBOS/14
KBOS
airport = KBOS
KBOS/15L
KBOS
airport = KBOS
KBOS/15R
KIAD
airport = KIAD
KIAD/01C
KIAD
airport = KIAD
KIAD/01L
KIAD
airport = KIAD
KIAD/01R
KIAD
airport = KIAD
KIAD/12
KIAH
airport = KIAH
KIAH/08L
KIAH
airport = KIAH
KIAH/08R
KIAH
airport = KIAH
KIAH/09
KIAH
airport = KIAH
KIAH/15L
KIAH
airport = KIAH
KIAH/15R
KJFK
airport = KJFK
KJFK/04L
KJFK
airport = KJFK
KJFK/04R
KJFK
airport = KJFK
KJFK/13L
KJFK
airport = KJFK
KJFK/13R
KLAX
airport = KLAX
KLAX/06L
KLAX
airport = KLAX
KLAX/06R
KLAX
airport = KLAX
KLAX/07L
KLAX
airport = KLAX
KLAX/07R
KMSP
airport = KMSP
KMSP/04
KMSP
airport = KMSP
KMSP/12L
KMSP
airport = KMSP
KMSP/12R
KMSP
airport = KMSP
KMSP/17
KORD
airport = KORD
KORD/04L
KORD
airport = KORD
KORD/04R
KORD
airport = KORD
KORD/09L
KORD
airport = KORD
KORD/09R
KORD
airport = KORD
KORD/10C
KORD
airport = KORD
KORD/10L
KORD
airport = KORD
KORD/10R
KORD
airport = KORD
KORD/14L
KORD
airport = KORD
KORD/15
KORD
airport = KORD
KORD/18
KSEA
airport = KSEA
KSEA/16C
KSEA
airport = KSEA
KSEA/16L
KSEA
airport = KSEA
KSEA/16R
KSFO
airport = KSFO
KSFO/01L
KSFO
airport = KSFO
KSFO/01R
KSFO
airport = KSFO
KSFO/10L
KSFO
airport = KSFO
KSFO/10R
LEMD
airport = LEMD
LEMD/14L
LEMD
airport = LEMD
LEMD/14R
LEMD
airport = LEMD
LEMD/18L
LEMD
airport = LEMD
LEMD/18R
LFML
airport = LFML
LFML/13L
LFML
airport = LFML
LFML/13R
LFOB
airport = LFOB
LFOB/04
LFOB
airport = LFOB
LFOB/12
LFPG
airport = LFPG
LFPG/08L
LFPG
airport = LFPG
LFPG/08R
LFPG
airport = LFPG
LFPG/09L
LFPG
airport = LFPG
LFPG/09R
LHBP
airport = LHBP
LHBP/13L
LHBP
airport = LHBP
LHBP/13R
LPFR
airport = LPFR
LPFR/10
LPPT
airport = LPPT
LPPT/02
LPPT
airport = LPPT
LPPT/17
MMMX
airport = MMMX
MMMX/05L
MMMX
airport = MMMX
MMMX/05R
PANC
airport = PANC
PANC/07L
PANC
airport = PANC
PANC/07R
PANC
airport = PANC
PANC/15
VABB
airport = VABB
VABB/09
VABB
airport = VABB
VABB/14
VECC
airport = VECC
VECC/01L
VECC
airport = VECC
VECC/01R
VIDP
airport = VIDP
VIDP/09
VIDP
airport = VIDP
VIDP/10
VIDP
airport = VIDP
VIDP/11
VIJP
airport = VIJP
VIJP/09
VIJP
airport = VIJP
VIJP/15
VOBL
airport = VOBL
VOBL/09L
VOBL
airport = VOBL
VOBL/09R
VOMM
airport = VOMM
VOMM/07
VOMM
airport = VOMM
VOMM/12
read runways database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$

(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$ python manage.py RunWaysDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
RunWaysDatabase: file folder= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays
RunWaysDatabase: file path= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays\RunWays.xlsx
runwaysDB exists
C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\RunWays\RunWays.xlsx
EBBR
airport = EBBR
EBBR/01
EBBR
airport = EBBR
EBBR/07L
EBBR
airport = EBBR
EBBR/07R
EDDB
airport = EDDB
EDDB/07L
EDDB
airport = EDDB
EDDB/07R
KATL
airport = KATL
KATL/08L
KATL
airport = KATL
KATL/08R
KATL
airport = KATL
KATL/09L
KATL
airport = KATL
KATL/09R
KATL
airport = KATL
KATL/10
KBOS
airport = KBOS
KBOS/04L
KBOS
airport = KBOS
KBOS/04R
KBOS
airport = KBOS
KBOS/09
KBOS
airport = KBOS
KBOS/14
KBOS
airport = KBOS
KBOS/15L
KBOS
airport = KBOS
KBOS/15R
KIAD
airport = KIAD
KIAD/01C
KIAD
airport = KIAD
KIAD/01L
KIAD
airport = KIAD
KIAD/01R
KIAD
airport = KIAD
KIAD/12
KIAH
airport = KIAH
KIAH/08L
KIAH
airport = KIAH
KIAH/08R
KIAH
airport = KIAH
KIAH/09
KIAH
airport = KIAH
KIAH/15L
KIAH
airport = KIAH
KIAH/15R
KJFK
airport = KJFK
KJFK/04L
KJFK
airport = KJFK
KJFK/04R
KJFK
airport = KJFK
KJFK/13L
KJFK
airport = KJFK
KJFK/13R
KLAX
airport = KLAX
KLAX/06L
KLAX
airport = KLAX
KLAX/06R
KLAX
airport = KLAX
KLAX/07L
KLAX
airport = KLAX
KLAX/07R
KMSP
airport = KMSP
KMSP/04
KMSP
airport = KMSP
KMSP/12L
KMSP
airport = KMSP
KMSP/12R
KMSP
airport = KMSP
KMSP/17
KORD
airport = KORD
KORD/04L
KORD
airport = KORD
KORD/04R
KORD
airport = KORD
KORD/09L
KORD
airport = KORD
KORD/09R
KORD
airport = KORD
KORD/10C
KORD
airport = KORD
KORD/10L
KORD
airport = KORD
KORD/10R
KORD
airport = KORD
KORD/14L
KORD
airport = KORD
KORD/15
KORD
airport = KORD
KORD/18
KSEA
airport = KSEA
KSEA/16C
KSEA
airport = KSEA
KSEA/16L
KSEA
airport = KSEA
KSEA/16R
KSFO
airport = KSFO
KSFO/01L
KSFO
airport = KSFO
KSFO/01R
KSFO
airport = KSFO
KSFO/10L
KSFO
airport = KSFO
KSFO/10R
LEMD
airport = LEMD
LEMD/14L
LEMD
airport = LEMD
LEMD/14R
LEMD
airport = LEMD
LEMD/18L
LEMD
airport = LEMD
LEMD/18R
LFML
airport = LFML
LFML/13L
LFML
airport = LFML
LFML/13R
LFOB
airport = LFOB
LFOB/04
LFOB
airport = LFOB
LFOB/12
LFPG
airport = LFPG
LFPG/08L
LFPG
airport = LFPG
LFPG/08R
LFPG
airport = LFPG
LFPG/09L
LFPG
airport = LFPG
LFPG/09R
LHBP
airport = LHBP
LHBP/13L
LHBP
airport = LHBP
LHBP/13R
LPFR
airport = LPFR
LPFR/10
LPPT
airport = LPPT
LPPT/02
LPPT
airport = LPPT
LPPT/17
MMMX
airport = MMMX
MMMX/05L
MMMX
airport = MMMX
MMMX/05R
PANC
airport = PANC
PANC/07L
PANC
airport = PANC
PANC/07R
PANC
airport = PANC
PANC/15
VABB
airport = VABB
VABB/09
VABB
airport = VABB
VABB/14
VECC
airport = VECC
VECC/01L
VECC
airport = VECC
VECC/01R
VIDP
airport = VIDP
VIDP/09
VIDP
airport = VIDP
VIDP/10
VIDP
airport = VIDP
VIDP/11
VIJP
airport = VIJP
VIJP/09
VIJP
airport = VIJP
VIJP/15
VOBL
airport = VOBL
VOBL/09L
VOBL
airport = VOBL
VOBL/09R
VOMM
airport = VOMM
VOMM/07
VOMM
airport = VOMM
VOMM/12
read runways database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


$ python manage.py WayPointsDatabaseLoad
 openap/prop : ==================== read data/aircraft/_synonym.csv =====================
 --- about to delete ---
 delete done
WayPointsDatabaseXlsx: file folder= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\WayPoints
WayPointsDatabaseXlsx: file path= C:\Users\rober\git\Airlines-Services\Airlines-Services\trajectory\management\commands\WayPoints\WayPoints.xlsx
acBD exists
Index is: 0
ID is: 0 - WayPoint is: VUZ - Latitude = N33▒40'12.47" - Longitude = W086▒53'59.41"
wayPoint name = VUZ - Latitude 33.67 - Longitude = -86.90
Index is: 1
ID is: 1 - WayPoint is: YAALL - Latitude = N33▒47'36.30" - Longitude = W087▒28'51.23"
wayPoint name = YAALL - Latitude 33.79 - Longitude = -87.48
Index is: 2
ID is: 2 - WayPoint is: XESSS - Latitude = N34▒18'50.62" - Longitude = W090▒07'02.78"
wayPoint name = XESSS - Latitude 34.31 - Longitude = -90.12
Index is: 3
ID is: 3 - WayPoint is: CARIN - Latitude = N34▒27'14.98" - Longitude = W090▒53'13.05"
wayPoint name = CARIN - Latitude 34.45 - Longitude = -90.89
Index is: 4
ID is: 4 - WayPoint is: ARIGY - Latitude = N34▒32'07.71" - Longitude = W091▒20'49.90"
wayPoint name = ARIGY - Latitude 34.54 - Longitude = -91.35
Index is: 5
ID is: 5 - WayPoint is: LIT - Latitude = N34▒40'39.62" - Longitude = W092▒10'49.90"
wayPoint name = LIT - Latitude 34.68 - Longitude = -92.18
Index is: 6
ID is: 6 - WayPoint is: KOMMA - Latitude = N35▒00'52.67" - Longitude = W094▒40'39.39"
wayPoint name = KOMMA - Latitude 35.01 - Longitude = -94.68
Index is: 7
ID is: 7 - WayPoint is: KLUBB - Latitude = N35▒07'13.30" - Longitude = W095▒28'00.29"
wayPoint name = KLUBB - Latitude 35.12 - Longitude = -95.47
Index is: 8
ID is: 8 - WayPoint is: DWINE - Latitude = N35▒12'29.02" - Longitude = W096▒12'58.54"
wayPoint name = DWINE - Latitude 35.21 - Longitude = -96.22
Index is: 9
ID is: 9 - WayPoint is: IRW - Latitude = N35▒21'30.94" - Longitude = W097▒36'33.21"
wayPoint name = IRW - Latitude 35.36 - Longitude = -97.61
Index is: 10
ID is: 10 - WayPoint is: CRUSR - Latitude = N35▒20'07.49" - Longitude = W098▒51'58.39"
wayPoint name = CRUSR - Latitude 35.34 - Longitude = -98.87
Index is: 11
ID is: 11 - WayPoint is: PNH - Latitude = N35▒14'06.22" - Longitude = W101▒41'56.51"
wayPoint name = PNH - Latitude 35.24 - Longitude = -101.70
Index is: 12
ID is: 12 - WayPoint is: TCC - Latitude = N35▒10'55.94" - Longitude = W103▒35'54.89"
wayPoint name = TCC - Latitude 35.18 - Longitude = -103.60
Index is: 13
ID is: 13 - WayPoint is: ABQ - Latitude = N35▒02'37.66" - Longitude = W106▒48'58.72"
wayPoint name = ABQ - Latitude 35.04 - Longitude = -106.82
Index is: 14
ID is: 14 - WayPoint is: ZUN - Latitude = N34▒57'56.71" - Longitude = W109▒09'16.23"
wayPoint name = ZUN - Latitude 34.97 - Longitude = -109.15
Index is: 15
ID is: 15 - WayPoint is: PYRIT - Latitude = N34▒52'10.39" - Longitude = W110▒30'41.16"
wayPoint name = PYRIT - Latitude 34.87 - Longitude = -110.51
Index is: 16
ID is: 16 - WayPoint is: DRK - Latitude = N34▒42'09.19" - Longitude = W112▒28'49.24"
wayPoint name = DRK - Latitude 34.70 - Longitude = -112.48
Index is: 17
ID is: 17 - WayPoint is: HIPPI - Latitude = N34▒33'44.24" - Longitude = W113▒38'21.73"
wayPoint name = HIPPI - Latitude 34.56 - Longitude = -113.64
Index is: 18
ID is: 18 - WayPoint is: CADEZ - Latitude = N34▒12'23.63" - Longitude = W115▒20'34.34"
wayPoint name = CADEZ - Latitude 34.21 - Longitude = -115.34
Index is: 19
ID is: 19 - WayPoint is: TNP - Latitude = N34▒06'44.04" - Longitude = W115▒46'11.65"
wayPoint name = TNP - Latitude 34.11 - Longitude = -115.77
Index is: 20
ID is: 20 - WayPoint is: SAX - Latitude = N41▒04'03.15" - Longitude = W074▒32'17.92"
wayPoint name = SAX - Latitude 41.07 - Longitude = -74.54
Index is: 21
ID is: 21 - WayPoint is: COATE - Latitude = N41▒08'10.42" - Longitude = W074▒41'42.60"
wayPoint name = COATE - Latitude 41.14 - Longitude = -74.70
Index is: 22
ID is: 22 - WayPoint is: LAAYK - Latitude = N41▒28'32.64" - Longitude = W075▒28'57.31"
wayPoint name = LAAYK - Latitude 41.48 - Longitude = -75.48
Index is: 23
ID is: 23 - WayPoint is: YYOST - Latitude = N41▒34'57.78" - Longitude = W075▒51'21.05"
wayPoint name = YYOST - Latitude 41.58 - Longitude = -75.86
Index is: 24
ID is: 24 - WayPoint is: DGRAF - Latitude = N41▒41'10.52" - Longitude = W076▒13'21.15"
wayPoint name = DGRAF - Latitude 41.69 - Longitude = -76.22
Index is: 25
ID is: 25 - WayPoint is: MTCAF - Latitude = N41▒46'11.34" - Longitude = W076▒31'20.58"
wayPoint name = MTCAF - Latitude 41.77 - Longitude = -76.52
Index is: 26
ID is: 26 - WayPoint is: REBBL - Latitude = N41▒52'57.63" - Longitude = W076▒55'58.06"
wayPoint name = REBBL - Latitude 41.88 - Longitude = -76.93
Index is: 27
ID is: 27 - WayPoint is: REXXY - Latitude = N42▒00'39.83" - Longitude = W077▒24'34.97"
wayPoint name = REXXY - Latitude 42.01 - Longitude = -77.41
Index is: 28
ID is: 28 - WayPoint is: HERBA - Latitude = N42▒14'35.29" - Longitude = W078▒16'27.84"
wayPoint name = HERBA - Latitude 42.24 - Longitude = -78.27
Index is: 29
ID is: 29 - WayPoint is: RAAKK - Latitude = N42▒23'59.00" - Longitude = W078▒54'39.00"
wayPoint name = RAAKK - Latitude 42.40 - Longitude = -78.91
Index is: 30
ID is: 30 - WayPoint is: FARGN - Latitude = N42▒36'42.19" - Longitude = W079▒47'18.42"
wayPoint name = FARGN - Latitude 42.61 - Longitude = -79.79
Index is: 31
ID is: 31 - WayPoint is: ICHOL - Latitude = N42▒38'31.46" - Longitude = W080▒30'13.99"
wayPoint name = ICHOL - Latitude 42.64 - Longitude = -80.50
Index is: 32
ID is: 32 - WayPoint is: JAAJA - Latitude = N42▒40'00.00" - Longitude = W081▒16'00.00"
wayPoint name = JAAJA - Latitude 42.67 - Longitude = -81.27
Index is: 33
ID is: 33 - WayPoint is: TWIGS - Latitude = N42▒48'34.10" - Longitude = W082▒33'10.30"
wayPoint name = TWIGS - Latitude 42.81 - Longitude = -82.55
Index is: 34
ID is: 34 - WayPoint is: BERYS - Latitude = N42▒54'33.97" - Longitude = W083▒17'59.75"
wayPoint name = BERYS - Latitude 42.91 - Longitude = -83.30
Index is: 35
ID is: 35 - WayPoint is: FNT - Latitude = N42▒58'00.38" - Longitude = W083▒44'49.08"
wayPoint name = FNT - Latitude 42.97 - Longitude = -83.75
Index is: 36
ID is: 36 - WayPoint is: MONEE - Latitude = N43▒14'25.80" - Longitude = W084▒27'50.95"
wayPoint name = MONEE - Latitude 43.24 - Longitude = -84.46
Index is: 37
ID is: 37 - WayPoint is: GRB - Latitude = N44▒33'18.57" - Longitude = W088▒11'41.48"
wayPoint name = GRB - Latitude 44.56 - Longitude = -88.19
Index is: 38
ID is: 38 - WayPoint is: TWINZ - Latitude = N45▒02'55.67" - Longitude = W092▒17'21.64"
wayPoint name = TWINZ - Latitude 45.05 - Longitude = -92.29
Index is: 39
ID is: 39 - WayPoint is: GEP - Latitude = N45▒08'44.46" - Longitude = W093▒22'23.45"
wayPoint name = GEP - Latitude 45.15 - Longitude = -93.37
Index is: 40
ID is: 40 - WayPoint is: ABR - Latitude = N45▒25'02.47" - Longitude = W098▒22'07.39"
wayPoint name = ABR - Latitude 45.42 - Longitude = -98.37
Index is: 41
ID is: 41 - WayPoint is: MLS - Latitude = N46▒22'56.00" - Longitude = W105▒57'12.72"
wayPoint name = MLS - Latitude 46.38 - Longitude = -105.95
Index is: 42
ID is: 42 - WayPoint is: ISAME - Latitude = N46▒25'43.25" - Longitude = W106▒11'05.39"
wayPoint name = ISAME - Latitude 46.43 - Longitude = -106.18
Index is: 43
ID is: 43 - WayPoint is: ESTRO - Latitude = N46▒57'09.42" - Longitude = W109▒00'37.65"
wayPoint name = ESTRO - Latitude 46.95 - Longitude = -109.01
Index is: 44
ID is: 44 - WayPoint is: LWT - Latitude = N47▒03'10.69" - Longitude = W109▒36'22.20"
wayPoint name = LWT - Latitude 47.05 - Longitude = -109.61
Index is: 45
ID is: 45 - WayPoint is: MLP - Latitude = N47▒27'24.85" - Longitude = W115▒38'45.76"
wayPoint name = MLP - Latitude 47.46 - Longitude = -115.65
Index is: 46
ID is: 46 - WayPoint is: AXIRI - Latitude = N20▒26'24.00" - Longitude = W099▒04'21.99"
wayPoint name = AXIRI - Latitude 20.44 - Longitude = -99.07
Index is: 47
ID is: 47 - WayPoint is: UDMAN - Latitude = N21▒17'20.99" - Longitude = W099▒32'36.99"
wayPoint name = UDMAN - Latitude 21.29 - Longitude = -99.54
Index is: 48
ID is: 48 - WayPoint is: TAKSO - Latitude = N21▒35'19.99" - Longitude = W099▒42'39.99"
wayPoint name = TAKSO - Latitude 21.59 - Longitude = -99.71
Index is: 49
ID is: 49 - WayPoint is: ULUAS - Latitude = N21▒50'02.00" - Longitude = W100▒09'19.99"
wayPoint name = ULUAS - Latitude 21.83 - Longitude = -100.16
Index is: 50
ID is: 50 - WayPoint is: AVPUS - Latitude = N22▒02'44.00" - Longitude = W100▒32'33.00"
wayPoint name = AVPUS - Latitude 22.05 - Longitude = -100.54
Index is: 51
ID is: 51 - WayPoint is: SLP - Latitude = N22▒15'23.00" - Longitude = W100▒55'49.52"
wayPoint name = SLP - Latitude 22.26 - Longitude = -100.93
Index is: 52
ID is: 52 - WayPoint is: KEPLU - Latitude = N22▒36'07.00" - Longitude = W101▒10'56.00"
wayPoint name = KEPLU - Latitude 22.60 - Longitude = -101.18
Index is: 53
ID is: 53 - WayPoint is: IDEAL - Latitude = N23▒22'50.99" - Longitude = W101▒45'20.00"
wayPoint name = IDEAL - Latitude 23.38 - Longitude = -101.76
Index is: 54
ID is: 54 - WayPoint is: EMIRA - Latitude = N23▒35'41.00" - Longitude = W101▒54'51.99"
wayPoint name = EMIRA - Latitude 23.59 - Longitude = -101.91
Index is: 55
ID is: 55 - WayPoint is: KATLA - Latitude = N24▒48'50.00" - Longitude = W102▒49'56.99"
wayPoint name = KATLA - Latitude 24.81 - Longitude = -102.83
Index is: 56
ID is: 56 - WayPoint is: URTIG - Latitude = N25▒13'18.99" - Longitude = W103▒08'41.00"
wayPoint name = URTIG - Latitude 25.22 - Longitude = -103.14
Index is: 57
ID is: 57 - WayPoint is: TRC - Latitude = N25▒33'50.27" - Longitude = W103▒24'30.26"
wayPoint name = TRC - Latitude 25.56 - Longitude = -103.41
Index is: 58
ID is: 58 - WayPoint is: KITON - Latitude = N25▒54'17.00" - Longitude = W103▒40'32.00"
wayPoint name = KITON - Latitude 25.90 - Longitude = -103.68
Index is: 59
ID is: 59 - WayPoint is: ETLEP - Latitude = N26▒44'19.00" - Longitude = W104▒20'15.99"
wayPoint name = ETLEP - Latitude 26.74 - Longitude = -104.34
Index is: 60
ID is: 60 - WayPoint is: LENEM - Latitude = N27▒46'25.00" - Longitude = W105▒10'35.99"
wayPoint name = LENEM - Latitude 27.77 - Longitude = -105.18
Index is: 61
ID is: 61 - WayPoint is: CUU - Latitude = N28▒42'58.97" - Longitude = W105▒57'31.43"
wayPoint name = CUU - Latitude 28.72 - Longitude = -105.96
Index is: 62
ID is: 62 - WayPoint is: SETMA - Latitude = N29▒07'31.00" - Longitude = W106▒03'23.00"
wayPoint name = SETMA - Latitude 29.13 - Longitude = -106.06
Index is: 63
ID is: 63 - WayPoint is: BECON - Latitude = N31▒47'17.58" - Longitude = W106▒42'45.17"
wayPoint name = BECON - Latitude 31.79 - Longitude = -106.71
Index is: 64
ID is: 64 - WayPoint is: RUTER - Latitude = N32▒17'01.43" - Longitude = W106▒53'55.21"
wayPoint name = RUTER - Latitude 32.28 - Longitude = -106.90
Index is: 65
ID is: 65 - WayPoint is: TCS - Latitude = N33▒16'57.00" - Longitude = W107▒16'49.96"
wayPoint name = TCS - Latitude 33.28 - Longitude = -107.28
Index is: 66
ID is: 66 - WayPoint is: CURLY - Latitude = N35▒25'04.75" - Longitude = W107▒05'32.33"
wayPoint name = CURLY - Latitude 35.42 - Longitude = -107.09
Index is: 67
ID is: 67 - WayPoint is: TANER - Latitude = N35▒52'05.76" - Longitude = W107▒25'42.57"
wayPoint name = TANER - Latitude 35.87 - Longitude = -107.43
Index is: 68
ID is: 68 - WayPoint is: PUMPS - Latitude = N36▒13'06.73" - Longitude = W107▒41'35.64"
wayPoint name = PUMPS - Latitude 36.22 - Longitude = -107.69
Index is: 69
ID is: 69 - WayPoint is: RSK - Latitude = N36▒44'54.21" - Longitude = W108▒05'56.03"
wayPoint name = RSK - Latitude 36.75 - Longitude = -108.10
Index is: 70
ID is: 70 - WayPoint is: BDROC - Latitude = N38▒27'03.27" - Longitude = W108▒36'19.86"
wayPoint name = BDROC - Latitude 38.45 - Longitude = -108.61
Index is: 71
ID is: 71 - WayPoint is: SINSY - Latitude = N38▒47'01.93" - Longitude = W108▒42'26.75"
wayPoint name = SINSY - Latitude 38.78 - Longitude = -108.71
Index is: 72
ID is: 72 - WayPoint is: JNC - Latitude = N39▒03'34.43" - Longitude = W108▒47'33.26"
wayPoint name = JNC - Latitude 39.06 - Longitude = -108.79
Index is: 73
ID is: 73 - WayPoint is: TCH - Latitude = N40▒51'00.93" - Longitude = W111▒58'54.86"
wayPoint name = TCH - Latitude 40.85 - Longitude = -111.98
Index is: 74
ID is: 74 - WayPoint is: TWF - Latitude = N42▒28'47.46" - Longitude = W114▒29'22.04"
wayPoint name = TWF - Latitude 42.48 - Longitude = -114.49
Index is: 75
ID is: 75 - WayPoint is: DNJ - Latitude = N44▒46'01.60" - Longitude = W116▒12'22.55"
wayPoint name = DNJ - Latitude 44.77 - Longitude = -116.21
Index is: 76
ID is: 76 - WayPoint is: BEAMO - Latitude = N45▒18'51.91" - Longitude = W117▒46'39.59"
wayPoint name = BEAMO - Latitude 45.31 - Longitude = -117.78
Index is: 77
ID is: 77 - WayPoint is: PDT - Latitude = N45▒41'54.31" - Longitude = W118▒56'19.35"
wayPoint name = PDT - Latitude 45.70 - Longitude = -118.94
Index is: 78
ID is: 78 - WayPoint is: BOSOX - Latitude = N42▒12'06.79" - Longitude = W071▒37'39.64"
wayPoint name = BOSOX - Latitude 42.20 - Longitude = -71.63
Index is: 79
ID is: 79 - WayPoint is: GRIPE - Latitude = N42▒08'08.87" - Longitude = W071▒54'32.47"
wayPoint name = GRIPE - Latitude 42.14 - Longitude = -71.91
Index is: 80
ID is: 80 - WayPoint is: GRAYM - Latitude = N42▒06'04.27" - Longitude = W072▒01'53.49"
wayPoint name = GRAYM - Latitude 42.10 - Longitude = -72.03
Index is: 81
ID is: 81 - WayPoint is: WITNY - Latitude = N42▒02'57.82" - Longitude = W072▒14'11.96"
wayPoint name = WITNY - Latitude 42.05 - Longitude = -72.24
Index is: 82
ID is: 82 - WayPoint is: BDL - Latitude = N41▒56'27.63" - Longitude = W072▒41'18.88"
wayPoint name = BDL - Latitude 41.94 - Longitude = -72.69
Index is: 83
ID is: 83 - WayPoint is: BRISS - Latitude = N41▒42'09.36" - Longitude = W073▒01'00.15"
wayPoint name = BRISS - Latitude 41.70 - Longitude = -73.02
Index is: 84
ID is: 84 - WayPoint is: JUDDS - Latitude = N41▒38'04.82" - Longitude = W073▒06'29.68"
wayPoint name = JUDDS - Latitude 41.63 - Longitude = -73.11
Index is: 85
ID is: 85 - WayPoint is: SOARS - Latitude = N41▒30'42.07" - Longitude = W073▒16'17.77"
wayPoint name = SOARS - Latitude 41.51 - Longitude = -73.27
Index is: 86
ID is: 86 - WayPoint is: GREKI - Latitude = N41▒28'48.03" - Longitude = W073▒18'50.98"
wayPoint name = GREKI - Latitude 41.48 - Longitude = -73.31
Index is: 87
ID is: 87 - WayPoint is: CMK - Latitude = N41▒16'48.33" - Longitude = W073▒34'52.78"
wayPoint name = CMK - Latitude 41.28 - Longitude = -73.58
Index is: 88
ID is: 88 - WayPoint is: DUEYS - Latitude = N41▒09'09.46" - Longitude = W073▒47'48.52"
wayPoint name = DUEYS - Latitude 41.15 - Longitude = -73.80
Index is: 89
ID is: 89 - WayPoint is: JERSY - Latitude = N40▒47'28.99" - Longitude = W074▒23'58.00"
wayPoint name = JERSY - Latitude 40.79 - Longitude = -74.40
Index is: 90
ID is: 90 - WayPoint is: SBJ - Latitude = N40▒34'58.96" - Longitude = W074▒44'30.45"
wayPoint name = SBJ - Latitude 40.58 - Longitude = -74.74
Index is: 91
ID is: 91 - WayPoint is: DIRPE - Latitude = N40▒28'22.94" - Longitude = W074▒59'37.03"
wayPoint name = DIRPE - Latitude 40.47 - Longitude = -74.99
Index is: 92
ID is: 92 - WayPoint is: PTW - Latitude = N40▒13'20.05" - Longitude = W075▒33'36.93"
wayPoint name = PTW - Latitude 40.22 - Longitude = -75.56
Index is: 93
ID is: 93 - WayPoint is: BYRDD - Latitude = N40▒05'31.93" - Longitude = W075▒49'07.29"
wayPoint name = BYRDD - Latitude 40.09 - Longitude = -75.82
Index is: 94
ID is: 94 - WayPoint is: HAAGN - Latitude = N39▒57'41.39" - Longitude = W076▒04'34.32"
wayPoint name = HAAGN - Latitude 39.96 - Longitude = -76.08
Index is: 95
ID is: 95 - WayPoint is: PENSY - Latitude = N39▒54'25.96" - Longitude = W076▒10'57.13"
wayPoint name = PENSY - Latitude 39.91 - Longitude = -76.18
Index is: 96
ID is: 96 - WayPoint is: EMI - Latitude = N39▒29'42.02" - Longitude = W076▒58'42.85"
wayPoint name = EMI - Latitude 39.50 - Longitude = -76.98
Index is: 97
ID is: 97 - WayPoint is: CSN - Latitude = N38▒38'28.32" - Longitude = W077▒51'55.79"
wayPoint name = CSN - Latitude 38.64 - Longitude = -77.87
Index is: 98
ID is: 98 - WayPoint is: MOL - Latitude = N37▒54'01.88" - Longitude = W079▒06'24.80"
wayPoint name = MOL - Latitude 37.90 - Longitude = -79.11
Index is: 99
ID is: 99 - WayPoint is: FLASK - Latitude = N37▒01'03.92" - Longitude = W080▒18'58.62"
wayPoint name = FLASK - Latitude 37.02 - Longitude = -80.32
Index is: 100
ID is: 100 - WayPoint is: REAVS - Latitude = N36▒42'10.99" - Longitude = W080▒44'12.03"
wayPoint name = REAVS - Latitude 36.70 - Longitude = -80.74
Index is: 101
ID is: 101 - WayPoint is: ODF - Latitude = N34▒41'45.14" - Longitude = W083▒17'51.58"
wayPoint name = ODF - Latitude 34.70 - Longitude = -83.30
Index is: 102
ID is: 102 - WayPoint is: CORCE - Latitude = N34▒27'34.99" - Longitude = W083▒33'10.59"
wayPoint name = CORCE - Latitude 34.46 - Longitude = -83.55
Index is: 103
ID is: 103 - WayPoint is: MACEY - Latitude = N34▒20'00.25" - Longitude = W083▒41'19.08"
wayPoint name = MACEY - Latitude 34.33 - Longitude = -83.69
Index is: 104
ID is: 104 - WayPoint is: WOMAC - Latitude = N34▒07'48.86" - Longitude = W083▒54'20.77"
wayPoint name = WOMAC - Latitude 34.13 - Longitude = -83.91
Index is: 105
ID is: 105 - WayPoint is: LOGEN - Latitude = N33▒59'16.98" - Longitude = W084▒03'24.43"
wayPoint name = LOGEN - Latitude 33.99 - Longitude = -84.06
Index is: 106
ID is: 106 - WayPoint is: LFK - Latitude = N31▒09'44.79" - Longitude = W094▒43'00.59"
wayPoint name = LFK - Latitude 31.16 - Longitude = -94.72
Index is: 107
ID is: 107 - WayPoint is: SKKIP - Latitude = N31▒14'54.86" - Longitude = W094▒39'27.00"
wayPoint name = SKKIP - Latitude 31.25 - Longitude = -94.66
Index is: 108
ID is: 108 - WayPoint is: ADUKE - Latitude = N31▒52'56.75" - Longitude = W094▒12'59.28"
wayPoint name = ADUKE - Latitude 31.88 - Longitude = -94.22
Index is: 109
ID is: 109 - WayPoint is: BERKE - Latitude = N32▒45'18.20" - Longitude = W093▒35'50.03"
wayPoint name = BERKE - Latitude 32.76 - Longitude = -93.60
Index is: 110
ID is: 110 - WayPoint is: CISAR - Latitude = N33▒30'42.79" - Longitude = W093▒02'54.64"
wayPoint name = CISAR - Latitude 33.51 - Longitude = -93.05
Index is: 111
ID is: 111 - WayPoint is: WASKO - Latitude = N34▒03'36.47" - Longitude = W092▒38'38.02"
wayPoint name = WASKO - Latitude 34.06 - Longitude = -92.64
Index is: 112
ID is: 112 - WayPoint is: IGLOO - Latitude = N35▒49'06.52" - Longitude = W091▒44'11.55"
wayPoint name = IGLOO - Latitude 35.82 - Longitude = -91.74
Index is: 113
ID is: 113 - WayPoint is: PLIED - Latitude = N36▒07'59.54" - Longitude = W091▒36'41.40"
wayPoint name = PLIED - Latitude 36.13 - Longitude = -91.61
Index is: 114
ID is: 114 - WayPoint is: TWRAY - Latitude = N37▒36'05.06" - Longitude = W091▒00'52.53"
wayPoint name = TWRAY - Latitude 37.60 - Longitude = -91.01
Index is: 115
ID is: 115 - WayPoint is: STL - Latitude = N38▒51'38.48" - Longitude = W090▒28'56.52"
wayPoint name = STL - Latitude 38.86 - Longitude = -90.48
Index is: 116
ID is: 116 - WayPoint is: FARGO - Latitude = N39▒43'17.26" - Longitude = W089▒46'35.07"
wayPoint name = FARGO - Latitude 39.72 - Longitude = -89.78
Index is: 117
ID is: 117 - WayPoint is: SPI - Latitude = N39▒50'23.03" - Longitude = W089▒40'39.84"
wayPoint name = SPI - Latitude 39.84 - Longitude = -89.68
Index is: 118
ID is: 118 - WayPoint is: PNT - Latitude = N40▒49'16.32" - Longitude = W088▒44'00.63"
wayPoint name = PNT - Latitude 40.82 - Longitude = -88.73
Index is: 119
ID is: 119 - WayPoint is: JOT - Latitude = N41▒32'47.09" - Longitude = W088▒19'06.28"
wayPoint name = JOT - Latitude 41.55 - Longitude = -88.32
Index is: 120
ID is: 120 - WayPoint is: GILBY - Latitude = N38▒58'23.61" - Longitude = W077▒35'20.64"
wayPoint name = GILBY - Latitude 38.97 - Longitude = -77.59
Index is: 121
ID is: 121 - WayPoint is: MANNE - Latitude = N39▒00'14.40" - Longitude = W077▒41'13.17"
wayPoint name = MANNE - Latitude 39.00 - Longitude = -77.69
Index is: 122
ID is: 122 - WayPoint is: JASEN - Latitude = N39▒03'38.50" - Longitude = W077▒52'05.19"
wayPoint name = JASEN - Latitude 39.06 - Longitude = -77.87
Index is: 123
ID is: 123 - WayPoint is: HOAGE - Latitude = N39▒07'42.96" - Longitude = W078▒05'12.41"
wayPoint name = HOAGE - Latitude 39.13 - Longitude = -78.09
Index is: 124
ID is: 124 - WayPoint is: TRIXY - Latitude = N39▒08'21.20" - Longitude = W078▒07'16.00"
wayPoint name = TRIXY - Latitude 39.14 - Longitude = -78.12
Index is: 125
ID is: 125 - WayPoint is: DRUZZ - Latitude = N39▒09'48.28" - Longitude = W078▒21'28.71"
wayPoint name = DRUZZ - Latitude 39.16 - Longitude = -78.36
Index is: 126
ID is: 126 - WayPoint is: ESL - Latitude = N39▒13'31.77" - Longitude = W078▒59'22.20"
wayPoint name = ESL - Latitude 39.23 - Longitude = -78.99
Index is: 127
ID is: 127 - WayPoint is: MOTME - Latitude = N39▒27'26.47" - Longitude = W079▒35'47.23"
wayPoint name = MOTME - Latitude 39.46 - Longitude = -79.60
Index is: 128
ID is: 128 - WayPoint is: MGW - Latitude = N39▒33'24.10" - Longitude = W079▒51'37.41"
wayPoint name = MGW - Latitude 39.56 - Longitude = -79.86
Index is: 129
ID is: 129 - WayPoint is: TEDDS - Latitude = N39▒38'18.76" - Longitude = W080▒16'34.08"
wayPoint name = TEDDS - Latitude 39.64 - Longitude = -80.28
Index is: 130
ID is: 130 - WayPoint is: BURGS - Latitude = N39▒41'54.66" - Longitude = W080▒35'10.99"
wayPoint name = BURGS - Latitude 39.70 - Longitude = -80.59
Index is: 131
ID is: 131 - WayPoint is: BEALL - Latitude = N39▒47'06.55" - Longitude = W081▒02'35.51"
wayPoint name = BEALL - Latitude 39.79 - Longitude = -81.04
Index is: 132
ID is: 132 - WayPoint is: HISOM - Latitude = N39▒52'35.48" - Longitude = W081▒32'13.19"
wayPoint name = HISOM - Latitude 39.88 - Longitude = -81.54
Index is: 133
ID is: 133 - WayPoint is: MUNOE - Latitude = N39▒53'42.66" - Longitude = W081▒38'22.27"
wayPoint name = MUNOE - Latitude 39.90 - Longitude = -81.64
Index is: 134
ID is: 134 - WayPoint is: ZZV - Latitude = N39▒56'27.10" - Longitude = W081▒53'33.36"
wayPoint name = ZZV - Latitude 39.94 - Longitude = -81.89
Index is: 135
ID is: 135 - WayPoint is: CINAB - Latitude = N40▒00'52.49" - Longitude = W082▒08'04.13"
wayPoint name = CINAB - Latitude 40.01 - Longitude = -82.13
Index is: 136
ID is: 136 - WayPoint is: APE - Latitude = N40▒09'03.82" - Longitude = W082▒35'17.88"
wayPoint name = APE - Latitude 40.15 - Longitude = -82.59
Index is: 137
ID is: 137 - WayPoint is: TRAKK - Latitude = N40▒18'32.35" - Longitude = W083▒10'17.75"
wayPoint name = TRAKK - Latitude 40.31 - Longitude = -83.17
Index is: 138
ID is: 138 - WayPoint is: WHETT - Latitude = N41▒09'36.64" - Longitude = W086▒35'02.93"
wayPoint name = WHETT - Latitude 41.16 - Longitude = -86.58
Index is: 139
ID is: 139 - WayPoint is: MOPER - Latitude = N41▒25'52.54" - Longitude = W087▒47'12.40"
wayPoint name = MOPER - Latitude 41.43 - Longitude = -87.79
Index is: 140
ID is: 140 - WayPoint is: VORIN - Latitude = N41▒32'52.81" - Longitude = W089▒20'10.95"
wayPoint name = VORIN - Latitude 41.55 - Longitude = -89.34
Index is: 141
ID is: 141 - WayPoint is: IOW - Latitude = N41▒31'08.26" - Longitude = W091▒36'47.69"
wayPoint name = IOW - Latitude 41.52 - Longitude = -91.61
Index is: 142
ID is: 142 - WayPoint is: DSM - Latitude = N41▒26'15.44" - Longitude = W093▒38'54.80"
wayPoint name = DSM - Latitude 41.44 - Longitude = -93.65
Index is: 143
ID is: 143 - WayPoint is: OBH - Latitude = N41▒22'32.64" - Longitude = W098▒21'12.94"
wayPoint name = OBH - Latitude 41.38 - Longitude = -98.35
Index is: 144
ID is: 144 - WayPoint is: ELJAY - Latitude = N41▒13'30.37" - Longitude = W101▒13'17.26"
wayPoint name = ELJAY - Latitude 41.23 - Longitude = -101.22
Index is: 145
ID is: 145 - WayPoint is: SNY - Latitude = N41▒05'48.00" - Longitude = W102▒58'58.80"
wayPoint name = SNY - Latitude 41.10 - Longitude = -102.98
Index is: 146
ID is: 146 - WayPoint is: FROGS - Latitude = N40▒31'12.12" - Longitude = W105▒53'41.21"
wayPoint name = FROGS - Latitude 40.52 - Longitude = -105.89
Index is: 147
ID is: 147 - WayPoint is: EKR - Latitude = N40▒04'02.79" - Longitude = W107▒55'29.81"
wayPoint name = EKR - Latitude 40.07 - Longitude = -107.92
Index is: 148
ID is: 148 - WayPoint is: DTA - Latitude = N39▒18'07.96" - Longitude = W112▒30'20.00"
wayPoint name = DTA - Latitude 39.30 - Longitude = -112.51
Index is: 149
ID is: 149 - WayPoint is: PAWLY - Latitude = N39▒11'49.70" - Longitude = W113▒26'23.38"
wayPoint name = PAWLY - Latitude 39.20 - Longitude = -113.44
Index is: 150
ID is: 150 - WayPoint is: MVA - Latitude = N38▒33'55.07" - Longitude = W118▒01'58.27"
wayPoint name = MVA - Latitude 38.57 - Longitude = -118.03
Index is: 151
ID is: 151 - WayPoint is: YESKA - Latitude = N61▒00'00.78" - Longitude = W149▒20'01.84"
wayPoint name = YESKA - Latitude 61.00 - Longitude = -149.33
Index is: 152
ID is: 152 - WayPoint is: REMBY - Latitude = N60▒40'00.00" - Longitude = W146▒00'00.00"
wayPoint name = REMBY - Latitude 60.67 - Longitude = -146.00
Index is: 153
ID is: 153 - WayPoint is: COHIL - Latitude = N60▒06'31.00" - Longitude = W139▒00'00.00"
wayPoint name = COHIL - Latitude 60.11 - Longitude = -139.00
Index is: 154
ID is: 154 - WayPoint is: GOROV - Latitude = N59▒18'21.10" - Longitude = W133▒00'02.80"
wayPoint name = GOROV - Latitude 59.31 - Longitude = -133.00
Index is: 155
ID is: 155 - WayPoint is: OMLOK - Latitude = N58▒46'45.59" - Longitude = W130▒00'00.00"
wayPoint name = OMLOK - Latitude 58.78 - Longitude = -130.00
Index is: 156
ID is: 156 - WayPoint is: BINGA - Latitude = N57▒42'07.09" - Longitude = W125▒00'00.00"
wayPoint name = BINGA - Latitude 57.70 - Longitude = -125.00
Index is: 157
ID is: 157 - WayPoint is: LEPET - Latitude = N56▒25'35.90" - Longitude = W120▒16'15.72"
wayPoint name = LEPET - Latitude 56.43 - Longitude = -120.27
Index is: 158
ID is: 158 - WayPoint is: NUBEG - Latitude = N54▒16'51.69" - Longitude = W113▒59'03.32"
wayPoint name = NUBEG - Latitude 54.28 - Longitude = -113.98
Index is: 159
ID is: 159 - WayPoint is: YWV - Latitude = N52▒58'53.00" - Longitude = W110▒49'59.79"
wayPoint name = YWV - Latitude 52.98 - Longitude = -110.83
Index is: 160
ID is: 160 - WayPoint is: VLN - Latitude = N50▒40'01.22" - Longitude = W104▒53'22.96"
wayPoint name = VLN - Latitude 50.67 - Longitude = -104.89
Index is: 161
ID is: 161 - WayPoint is: MOT - Latitude = N48▒15'37.20" - Longitude = W101▒17'13.44"
wayPoint name = MOT - Latitude 48.26 - Longitude = -101.29
Index is: 162
ID is: 162 - WayPoint is: PABIC - Latitude = N48▒03'07.54" - Longitude = W101▒11'54.34"
wayPoint name = PABIC - Latitude 48.05 - Longitude = -101.20
Index is: 163
ID is: 163 - WayPoint is: HIDEL - Latitude = N48▒01'45.05" - Longitude = W101▒11'19.40"
wayPoint name = HIDEL - Latitude 48.03 - Longitude = -101.19
Index is: 164
ID is: 164 - WayPoint is: TERTL - Latitude = N47▒34'16.39" - Longitude = W100▒59'47.62"
wayPoint name = TERTL - Latitude 47.57 - Longitude = -101.00
Index is: 165
ID is: 165 - WayPoint is: WASHR - Latitude = N47▒18'26.68" - Longitude = W100▒53'15.50"
wayPoint name = WASHR - Latitude 47.31 - Longitude = -100.89
Index is: 166
ID is: 166 - WayPoint is: WILTN - Latitude = N47▒04'58.09" - Longitude = W100▒47'43.84"
wayPoint name = WILTN - Latitude 47.08 - Longitude = -100.80
Index is: 167
ID is: 167 - WayPoint is: FIKAG - Latitude = N46▒55'20.20" - Longitude = W100▒43'48.91"
wayPoint name = FIKAG - Latitude 46.92 - Longitude = -100.73
Index is: 168
ID is: 168 - WayPoint is: BIS - Latitude = N46▒45'42.34" - Longitude = W100▒39'55.46"
wayPoint name = BIS - Latitude 46.76 - Longitude = -100.67
Index is: 169
ID is: 169 - WayPoint is: MOFIT - Latitude = N46▒33'01.37" - Longitude = W100▒17'28.81"
wayPoint name = MOFIT - Latitude 46.55 - Longitude = -100.29
Index is: 170
ID is: 170 - WayPoint is: WISEK - Latitude = N46▒22'49.35" - Longitude = W099▒59'38.99"
wayPoint name = WISEK - Latitude 46.38 - Longitude = -99.99
Index is: 171
ID is: 171 - WayPoint is: IRIWY - Latitude = N46▒03'11.72" - Longitude = W099▒25'52.63"
wayPoint name = IRIWY - Latitude 46.05 - Longitude = -99.43
Index is: 172
ID is: 172 - WayPoint is: MUNEF - Latitude = N45▒41'21.22" - Longitude = W098▒49'04.75"
wayPoint name = MUNEF - Latitude 45.69 - Longitude = -98.82
Index is: 173
ID is: 173 - WayPoint is: FSD - Latitude = N43▒38'58.16" - Longitude = W096▒46'52.05"
wayPoint name = FSD - Latitude 43.65 - Longitude = -96.78
Index is: 174
ID is: 174 - WayPoint is: EYHUX - Latitude = N42▒26'08.02" - Longitude = W095▒01'09.77"
wayPoint name = EYHUX - Latitude 42.44 - Longitude = -95.02
Index is: 175
ID is: 175 - WayPoint is: JAVAS - Latitude = N40▒45'56.25" - Longitude = W092▒47'19.80"
wayPoint name = JAVAS - Latitude 40.77 - Longitude = -92.79
Index is: 176
ID is: 176 - WayPoint is: CHASY - Latitude = N40▒41'38.25" - Longitude = W092▒41'55.11"
wayPoint name = CHASY - Latitude 40.69 - Longitude = -92.70
Index is: 177
ID is: 177 - WayPoint is: SKBOZ - Latitude = N40▒34'52.20" - Longitude = W092▒33'26.15"
wayPoint name = SKBOZ - Latitude 40.58 - Longitude = -92.56
Index is: 178
ID is: 178 - WayPoint is: COLIE - Latitude = N40▒16'50.12" - Longitude = W092▒11'01.93"
wayPoint name = COLIE - Latitude 40.28 - Longitude = -92.18
Index is: 179
ID is: 179 - WayPoint is: TWAIN - Latitude = N39▒40'20.55" - Longitude = W091▒26'35.13"
wayPoint name = TWAIN - Latitude 39.67 - Longitude = -91.44
Index is: 180
ID is: 180 - WayPoint is: PLESS - Latitude = N37▒48'34.48" - Longitude = W088▒57'47.48"
wayPoint name = PLESS - Latitude 37.81 - Longitude = -88.96
Index is: 181
ID is: 181 - WayPoint is: BNA - Latitude = N36▒08'13.05" - Longitude = W086▒41'05.17"
wayPoint name = BNA - Latitude 36.14 - Longitude = -86.68
Index is: 182
ID is: 182 - WayPoint is: SLI - Latitude = N33▒46'59.87" - Longitude = W118▒03'17.11"
wayPoint name = SLI - Latitude 33.78 - Longitude = -118.05
Index is: 183
ID is: 183 - WayPoint is: AHEIM - Latitude = N33▒49'13.13" - Longitude = W117▒54'43.01"
wayPoint name = AHEIM - Latitude 33.82 - Longitude = -117.91
Index is: 184
ID is: 184 - WayPoint is: OLLIE - Latitude = N33▒50'46.55" - Longitude = W117▒48'41.00"
wayPoint name = OLLIE - Latitude 33.85 - Longitude = -117.81
Index is: 185
ID is: 185 - WayPoint is: POXKU - Latitude = N33▒51'13.47" - Longitude = W117▒46'56.49"
wayPoint name = POXKU - Latitude 33.85 - Longitude = -117.78
Index is: 186
ID is: 186 - WayPoint is: EBITE - Latitude = N33▒51'40.73" - Longitude = W117▒45'03.23"
wayPoint name = EBITE - Latitude 33.86 - Longitude = -117.75
Index is: 187
ID is: 187 - WayPoint is: PDZ - Latitude = N33▒55'06.01" - Longitude = W117▒31'47.99"
wayPoint name = PDZ - Latitude 33.92 - Longitude = -117.53
Index is: 188
ID is: 188 - WayPoint is: CIVET - Latitude = N34▒02'03.93" - Longitude = W117▒23'27.17"
wayPoint name = CIVET - Latitude 34.03 - Longitude = -117.39
Index is: 189
ID is: 189 - WayPoint is: RUSTT - Latitude = N34▒02'53.62" - Longitude = W117▒14'32.83"
wayPoint name = RUSTT - Latitude 34.05 - Longitude = -117.24
Index is: 190
ID is: 190 - WayPoint is: PIONE - Latitude = N34▒05'40.10" - Longitude = W116▒44'19.64"
wayPoint name = PIONE - Latitude 34.09 - Longitude = -116.74
Index is: 191
ID is: 191 - WayPoint is: GEEYY - Latitude = N34▒50'11.79" - Longitude = W091▒10'47.67"
wayPoint name = GEEYY - Latitude 34.84 - Longitude = -91.18
Index is: 192
ID is: 192 - WayPoint is: MEM - Latitude = N35▒00'54.42" - Longitude = W089▒58'59.55"
wayPoint name = MEM - Latitude 35.02 - Longitude = -89.98
Index is: 193
ID is: 193 - WayPoint is: BLUIT - Latitude = N47▒24'21.36" - Longitude = W120▒25'05.51"
wayPoint name = BLUIT - Latitude 47.41 - Longitude = -120.42
Index is: 194
ID is: 194 - WayPoint is: EPH - Latitude = N47▒22'40.50" - Longitude = W119▒25'26.41"
wayPoint name = EPH - Latitude 47.38 - Longitude = -119.42
Index is: 195
ID is: 195 - WayPoint is: PECOK - Latitude = N44▒00'27.67" - Longitude = W085▒43'14.71"
wayPoint name = PECOK - Latitude 44.01 - Longitude = -85.72
Index is: 196
ID is: 196 - WayPoint is: LEATO - Latitude = N43▒43'16.90" - Longitude = W084▒31'49.35"
wayPoint name = LEATO - Latitude 43.72 - Longitude = -84.53
Index is: 197
ID is: 197 - WayPoint is: DIRKS - Latitude = N43▒29'57.42" - Longitude = W083▒38'52.95"
wayPoint name = DIRKS - Latitude 43.50 - Longitude = -83.65
Index is: 198
ID is: 198 - WayPoint is: ECK - Latitude = N43▒15'21.18" - Longitude = W082▒43'04.54"
wayPoint name = ECK - Latitude 43.26 - Longitude = -82.72
Index is: 199
ID is: 199 - WayPoint is: YXU - Latitude = N43▒02'16.47" - Longitude = W081▒08'56.14"
wayPoint name = YXU - Latitude 43.04 - Longitude = -81.15
Index is: 200
ID is: 200 - WayPoint is: LESUB - Latitude = N43▒01'00.29" - Longitude = W080▒32'58.76"
wayPoint name = LESUB - Latitude 43.02 - Longitude = -80.55
Index is: 201
ID is: 201 - WayPoint is: BUF - Latitude = N42▒55'44.38" - Longitude = W078▒38'46.82"
wayPoint name = BUF - Latitude 42.93 - Longitude = -78.65
Index is: 202
ID is: 202 - WayPoint is: DALEE - Latitude = N42▒45'22.73" - Longitude = W078▒18'12.85"
wayPoint name = DALEE - Latitude 42.76 - Longitude = -78.30
Index is: 203
ID is: 203 - WayPoint is: BURST - Latitude = N42▒31'20.40" - Longitude = W077▒50'43.29"
wayPoint name = BURST - Latitude 42.52 - Longitude = -77.85
Index is: 204
ID is: 204 - WayPoint is: HORNE - Latitude = N42▒23'21.25" - Longitude = W077▒35'16.19"
wayPoint name = HORNE - Latitude 42.39 - Longitude = -77.59
Index is: 205
ID is: 205 - WayPoint is: THINK - Latitude = N42▒13'43.44" - Longitude = W077▒16'49.20"
wayPoint name = THINK - Latitude 42.23 - Longitude = -77.28
Index is: 206
ID is: 206 - WayPoint is: ULW - Latitude = N42▒05'38.95" - Longitude = W077▒01'29.30"
wayPoint name = ULW - Latitude 42.09 - Longitude = -77.02
Index is: 207
ID is: 207 - WayPoint is: BIPOD - Latitude = N41▒52'41.57" - Longitude = W076▒40'04.22"
wayPoint name = BIPOD - Latitude 41.88 - Longitude = -76.67
Index is: 208
ID is: 208 - WayPoint is: TWIIN - Latitude = N41▒44'57.85" - Longitude = W076▒27'25.15"
wayPoint name = TWIIN - Latitude 41.75 - Longitude = -76.46
Index is: 209
ID is: 209 - WayPoint is: LACIE - Latitude = N41▒33'14.95" - Longitude = W076▒08'24.38"
wayPoint name = LACIE - Latitude 41.55 - Longitude = -76.14
Index is: 210
ID is: 210 - WayPoint is: LOPEZ - Latitude = N41▒26'35.68" - Longitude = W075▒57'42.12"
wayPoint name = LOPEZ - Latitude 41.44 - Longitude = -75.96
Index is: 211
ID is: 211 - WayPoint is: LVZ - Latitude = N41▒16'22.08" - Longitude = W075▒41'22.08"
wayPoint name = LVZ - Latitude 41.27 - Longitude = -75.69
Index is: 212
ID is: 212 - WayPoint is: DBQ - Latitude = N42▒24'05.30" - Longitude = W090▒42'32.66"
wayPoint name = DBQ - Latitude 42.40 - Longitude = -90.71
Index is: 213
ID is: 213 - WayPoint is: LOTTE - Latitude = N41▒56'07.89" - Longitude = W090▒33'24.79"
wayPoint name = LOTTE - Latitude 41.94 - Longitude = -90.56
Index is: 214
ID is: 214 - WayPoint is: CVA - Latitude = N41▒42'30.77" - Longitude = W090▒28'59.92"
wayPoint name = CVA - Latitude 41.71 - Longitude = -90.48
Index is: 215
ID is: 215 - WayPoint is: NOWSO - Latitude = N41▒31'19.43" - Longitude = W090▒21'22.56"
wayPoint name = NOWSO - Latitude 41.52 - Longitude = -90.36
Index is: 216
ID is: 216 - WayPoint is: GENSO - Latitude = N41▒21'44.35" - Longitude = W090▒14'53.18"
wayPoint name = GENSO - Latitude 41.36 - Longitude = -90.25
Index is: 217
ID is: 217 - WayPoint is: JPAUL - Latitude = N41▒15'03.15" - Longitude = W090▒10'22.74"
wayPoint name = JPAUL - Latitude 41.25 - Longitude = -90.17
Index is: 218
ID is: 218 - WayPoint is: PIA - Latitude = N40▒40'48.26" - Longitude = W089▒47'33.90"
wayPoint name = PIA - Latitude 40.68 - Longitude = -89.79
Index is: 219
ID is: 219 - WayPoint is: MACIN - Latitude = N40▒32'27.36" - Longitude = W089▒27'33.88"
wayPoint name = MACIN - Latitude 40.54 - Longitude = -89.46
Index is: 220
ID is: 220 - WayPoint is: NINIC - Latitude = N40▒26'02.03" - Longitude = W089▒12'19.69"
wayPoint name = NINIC - Latitude 40.43 - Longitude = -89.21
Index is: 221
ID is: 221 - WayPoint is: MCLEN - Latitude = N40▒24'18.98" - Longitude = W089▒08'16.55"
wayPoint name = MCLEN - Latitude 40.41 - Longitude = -89.14
Index is: 222
ID is: 222 - WayPoint is: LODGE - Latitude = N40▒08'35.76" - Longitude = W088▒31'34.60"
wayPoint name = LODGE - Latitude 40.14 - Longitude = -88.53
Index is: 223
ID is: 223 - WayPoint is: CMI - Latitude = N40▒02'04.30" - Longitude = W088▒16'33.81"
wayPoint name = CMI - Latitude 40.03 - Longitude = -88.28
Index is: 224
ID is: 224 - WayPoint is: NEWMY - Latitude = N39▒51'26.22" - Longitude = W087▒56'19.21"
wayPoint name = NEWMY - Latitude 39.86 - Longitude = -87.94
Index is: 225
ID is: 225 - WayPoint is: BLANO - Latitude = N39▒36'45.74" - Longitude = W087▒28'44.55"
wayPoint name = BLANO - Latitude 39.61 - Longitude = -87.48
Index is: 226
ID is: 226 - WayPoint is: TTH - Latitude = N39▒29'20.19" - Longitude = W087▒14'56.44"
wayPoint name = TTH - Latitude 39.49 - Longitude = -87.25
Index is: 227
ID is: 227 - WayPoint is: BUNKA - Latitude = N39▒04'57.32" - Longitude = W087▒09'06.58"
wayPoint name = BUNKA - Latitude 39.08 - Longitude = -87.15
Index is: 228
ID is: 228 - WayPoint is: HNB - Latitude = N38▒15'01.75" - Longitude = W086▒57'22.30"
wayPoint name = HNB - Latitude 38.25 - Longitude = -86.96
Index is: 229
ID is: 229 - WayPoint is: APALO - Latitude = N38▒00'20.59" - Longitude = W086▒51'35.27"
wayPoint name = APALO - Latitude 38.01 - Longitude = -86.86
Index is: 230
ID is: 230 - WayPoint is: LOONE - Latitude = N37▒44'14.43" - Longitude = W086▒45'18.02"
wayPoint name = LOONE - Latitude 37.74 - Longitude = -86.76
Index is: 231
ID is: 231 - WayPoint is: RENRO - Latitude = N37▒28'50.53" - Longitude = W086▒39'19.25"
wayPoint name = RENRO - Latitude 37.48 - Longitude = -86.66
Index is: 232
ID is: 232 - WayPoint is: BWG - Latitude = N36▒55'43.46" - Longitude = W086▒26'36.36"
wayPoint name = BWG - Latitude 36.93 - Longitude = -86.44
Index is: 233
ID is: 233 - WayPoint is: RACEY - Latitude = N41▒25'00.94" - Longitude = W073▒11'38.10"
wayPoint name = RACEY - Latitude 41.42 - Longitude = -73.19
Index is: 234
ID is: 234 - WayPoint is: SORRY - Latitude = N41▒28'43.10" - Longitude = W073▒01'02.67"
wayPoint name = SORRY - Latitude 41.48 - Longitude = -73.02
Index is: 235
ID is: 235 - WayPoint is: YALER - Latitude = N41▒30'56.61" - Longitude = W072▒54'39.09"
wayPoint name = YALER - Latitude 41.52 - Longitude = -72.91
Index is: 236
ID is: 236 - WayPoint is: HFD - Latitude = N41▒38'27.97" - Longitude = W072▒32'50.70"
wayPoint name = HFD - Latitude 41.64 - Longitude = -72.55
Index is: 237
ID is: 237 - WayPoint is: LIN - Latitude = N38▒04'28.51" - Longitude = W121▒00'13.88"
wayPoint name = LIN - Latitude 38.07 - Longitude = -121.00
Index is: 238
ID is: 238 - WayPoint is: SEFFY - Latitude = N51▒23'24.47" - Longitude = W107▒08'15.94"
wayPoint name = SEFFY - Latitude 51.39 - Longitude = -107.14
Index is: 239
ID is: 239 - WayPoint is: FUDGY - Latitude = N52▒13'07.50" - Longitude = W110▒00'00.00"
wayPoint name = FUDGY - Latitude 52.22 - Longitude = -110.00
Index is: 240
ID is: 240 - WayPoint is: OMROD - Latitude = N53▒00'20.11" - Longitude = W113▒05'35.92"
wayPoint name = OMROD - Latitude 53.01 - Longitude = -113.09
Index is: 241
ID is: 241 - WayPoint is: YEG - Latitude = N53▒11'08.09" - Longitude = W113▒52'00.62"
wayPoint name = YEG - Latitude 53.19 - Longitude = -113.87
Index is: 242
ID is: 242 - WayPoint is: WYLDE - Latitude = N53▒36'52.20" - Longitude = W114▒53'38.40"
wayPoint name = WYLDE - Latitude 53.61 - Longitude = -114.89
Index is: 243
ID is: 243 - WayPoint is: YQU - Latitude = N55▒10'27.15" - Longitude = W119▒01'48.74"
wayPoint name = YQU - Latitude 55.17 - Longitude = -119.03
Index is: 244
ID is: 244 - WayPoint is: ELTEX - Latitude = N56▒53'57.14" - Longitude = W125▒00'00.00"
wayPoint name = ELTEX - Latitude 56.90 - Longitude = -125.00
Index is: 245
ID is: 245 - WayPoint is: KEVPO - Latitude = N58▒01'36.32" - Longitude = W130▒00'00.00"
wayPoint name = KEVPO - Latitude 58.03 - Longitude = -130.00
Index is: 246
ID is: 246 - WayPoint is: MITOM - Latitude = N58▒19'14.70" - Longitude = W131▒32'02.90"
wayPoint name = MITOM - Latitude 58.32 - Longitude = -131.53
Index is: 247
ID is: 247 - WayPoint is: DEEJA - Latitude = N58▒54'08.00" - Longitude = W135▒00'00.00"
wayPoint name = DEEJA - Latitude 58.90 - Longitude = -135.00
Index is: 248
ID is: 248 - WayPoint is: YAK - Latitude = N59▒30'38.98" - Longitude = W139▒38'53.27"
wayPoint name = YAK - Latitude 59.51 - Longitude = -139.65
Index is: 249
ID is: 249 - WayPoint is: KATAT - Latitude = N60▒15'29.17" - Longitude = W144▒42'18.77"
wayPoint name = KATAT - Latitude 60.26 - Longitude = -144.71
Index is: 250
ID is: 250 - WayPoint is: CASEL - Latitude = N60▒19'52.06" - Longitude = W145▒17'54.25"
wayPoint name = CASEL - Latitude 60.33 - Longitude = -145.30
Index is: 251
ID is: 251 - WayPoint is: JOH - Latitude = N60▒28'51.42" - Longitude = W146▒35'57.60"
wayPoint name = JOH - Latitude 60.48 - Longitude = -146.60
Index is: 252
ID is: 252 - WayPoint is: CREEL - Latitude = N40▒26'50.50" - Longitude = W073▒33'10.67"
wayPoint name = CREEL - Latitude 40.45 - Longitude = -73.55
Index is: 253
ID is: 253 - WayPoint is: RIFLE - Latitude = N40▒41'24.17" - Longitude = W072▒34'54.89"
wayPoint name = RIFLE - Latitude 40.69 - Longitude = -72.58
Index is: 254
ID is: 254 - WayPoint is: HTO - Latitude = N40▒55'08.38" - Longitude = W072▒19'00.13"
wayPoint name = HTO - Latitude 40.92 - Longitude = -72.32
Index is: 255
ID is: 255 - WayPoint is: PARCH - Latitude = N41▒05'57.21" - Longitude = W072▒07'14.66"
wayPoint name = PARCH - Latitude 41.10 - Longitude = -72.12
Index is: 256
ID is: 256 - WayPoint is: TRAIT - Latitude = N41▒17'04.75" - Longitude = W071▒55'03.35"
wayPoint name = TRAIT - Latitude 41.28 - Longitude = -71.92
Index is: 257
ID is: 257 - WayPoint is: PVD - Latitude = N41▒43'27.63" - Longitude = W071▒25'46.70"
wayPoint name = PVD - Latitude 41.72 - Longitude = -71.43
Index is: 258
ID is: 258 - WayPoint is: BOS - Latitude = N42▒21'26.82" - Longitude = W070▒59'22.37"
wayPoint name = BOS - Latitude 42.36 - Longitude = -70.99
Index is: 259
ID is: 259 - WayPoint is: COPLY - Latitude = N42▒29'52.21" - Longitude = W070▒33'28.56"
wayPoint name = COPLY - Latitude 42.50 - Longitude = -70.56
Index is: 260
ID is: 260 - WayPoint is: SCUPP - Latitude = N42▒36'11.01" - Longitude = W070▒13'49.34"
wayPoint name = SCUPP - Latitude 42.60 - Longitude = -70.23
Index is: 261
ID is: 261 - WayPoint is: CANAL - Latitude = N42▒40'08.51" - Longitude = W070▒01'21.75"
wayPoint name = CANAL - Latitude 42.67 - Longitude = -70.02
Index is: 262
ID is: 262 - WayPoint is: TUSKY - Latitude = N43▒33'53.99" - Longitude = W067▒00'00.00"
wayPoint name = TUSKY - Latitude 43.56 - Longitude = -67.00
Index is: 263
ID is: 263 - WayPoint is: OMSAT - Latitude = N47▒00'00.00" - Longitude = W052▒00'00.00"
wayPoint name = OMSAT - Latitude 47.00 - Longitude = -52.00
Index is: 264
ID is: 264 - WayPoint is: 47N050W - Latitude = N47▒30'00.00" - Longitude = W050▒00'00.00"
wayPoint name = 47N050W - Latitude 47.50 - Longitude = -50.00
Index is: 265
ID is: 265 - WayPoint is: 49N040W - Latitude = N49▒30'00.00" - Longitude = W040▒00'00.00"
wayPoint name = 49N040W - Latitude 49.50 - Longitude = -40.00
Index is: 266
ID is: 266 - WayPoint is: 51N030W - Latitude = N51▒30'00.00" - Longitude = W030▒00'00.00"
wayPoint name = 51N030W - Latitude 51.50 - Longitude = -30.00
Index is: 267
ID is: 267 - WayPoint is: 52N020W - Latitude = N52▒30'00.00" - Longitude = W020▒00'00.00"
wayPoint name = 52N020W - Latitude 52.50 - Longitude = -20.00
Index is: 268
ID is: 268 - WayPoint is: LIMRI - Latitude = N52▒00'00.00" - Longitude = W015▒00'00.00"
wayPoint name = LIMRI - Latitude 52.00 - Longitude = -15.00
Index is: 269
ID is: 269 - WayPoint is: XETBO - Latitude = N52▒00'00.00" - Longitude = W014▒00'00.00"
wayPoint name = XETBO - Latitude 52.00 - Longitude = -14.00
Index is: 270
ID is: 270 - WayPoint is: DOLIP - Latitude = N52▒00'00.00" - Longitude = W012▒00'00.00"
wayPoint name = DOLIP - Latitude 52.00 - Longitude = -12.00
Index is: 271
ID is: 271 - WayPoint is: LINRA - Latitude = N51▒34'47.00" - Longitude = W010▒01'55.99"
wayPoint name = LINRA - Latitude 51.58 - Longitude = -10.03
Index is: 272
ID is: 272 - WayPoint is: LESLU - Latitude = N51▒00'00.00" - Longitude = W008▒00'00.00"
wayPoint name = LESLU - Latitude 51.00 - Longitude = -8.00
Index is: 273
ID is: 273 - WayPoint is: INSUN - Latitude = N50▒23'43.00" - Longitude = W006▒19'23.99"
wayPoint name = INSUN - Latitude 50.40 - Longitude = -6.32
Index is: 274
ID is: 274 - WayPoint is: LND - Latitude = N50▒08'10.99" - Longitude = W005▒38'13.00"
wayPoint name = LND - Latitude 50.14 - Longitude = -5.64
Index is: 275
ID is: 275 - WayPoint is: NAKID - Latitude = N49▒42'54.00" - Longitude = W004▒37'22.99"
wayPoint name = NAKID - Latitude 49.72 - Longitude = -4.62
Index is: 276
ID is: 276 - WayPoint is: ANNET - Latitude = N49▒39'04.99" - Longitude = W004▒00'05.00"
wayPoint name = ANNET - Latitude 49.65 - Longitude = -4.00
Index is: 277
ID is: 277 - WayPoint is: UVSUV - Latitude = N49▒29'16.99" - Longitude = W001▒40'27.99"
wayPoint name = UVSUV - Latitude 49.49 - Longitude = -1.67
Index is: 278
ID is: 278 - WayPoint is: INGOR - Latitude = N49▒21'52.00" - Longitude = W000▒15'00.00"
wayPoint name = INGOR - Latitude 49.36 - Longitude = -0.25
Index is: 279
ID is: 279 - WayPoint is: LUKIP - Latitude = N49▒18'56.99" - Longitude = E000▒29'46.99"
wayPoint name = LUKIP - Latitude 49.32 - Longitude = 0.50
Index is: 280
ID is: 280 - WayPoint is: ERIXU - Latitude = N48▒05'00.00" - Longitude = E002▒15'35.00"
wayPoint name = ERIXU - Latitude 48.08 - Longitude = 2.26
Index is: 281
ID is: 281 - WayPoint is: ARKIP - Latitude = N47▒37'59.99" - Longitude = E002▒02'10.99"
wayPoint name = ARKIP - Latitude 47.63 - Longitude = 2.04
Index is: 282
ID is: 282 - WayPoint is: BALAN - Latitude = N46▒30'57.99" - Longitude = E001▒02'00.00"
wayPoint name = BALAN - Latitude 46.52 - Longitude = 1.03
Index is: 283
ID is: 283 - WayPoint is: FOUCO - Latitude = N45▒45'16.99" - Longitude = E000▒28'49.99"
wayPoint name = FOUCO - Latitude 45.75 - Longitude = 0.48
Index is: 284
ID is: 284 - WayPoint is: OSMOB - Latitude = N44▒38'57.00" - Longitude = W000▒20'18.00"
wayPoint name = OSMOB - Latitude 44.65 - Longitude = -0.34
Index is: 285
ID is: 285 - WayPoint is: BIDAC - Latitude = N43▒25'01.99" - Longitude = W001▒08'08.00"
wayPoint name = BIDAC - Latitude 43.42 - Longitude = -1.14
Index is: 286
ID is: 286 - WayPoint is: ARVID - Latitude = N43▒04'33.99" - Longitude = W001▒27'53.00"
wayPoint name = ARVID - Latitude 43.08 - Longitude = -1.46
Index is: 287
ID is: 287 - WayPoint is: PPN - Latitude = N42▒44'02.00" - Longitude = W001▒42'07.00"
wayPoint name = PPN - Latitude 42.73 - Longitude = -1.70
Index is: 288
ID is: 288 - WayPoint is: NOLSA - Latitude = N42▒25'39.00" - Longitude = W001▒54'27.00"
wayPoint name = NOLSA - Latitude 42.43 - Longitude = -1.91
Index is: 289
ID is: 289 - WayPoint is: ALEPO - Latitude = N42▒20'36.99" - Longitude = W001▒57'48.00"
wayPoint name = ALEPO - Latitude 42.34 - Longitude = -1.96
Index is: 290
ID is: 290 - WayPoint is: VASUM - Latitude = N42▒16'18.99" - Longitude = W002▒00'39.99"
wayPoint name = VASUM - Latitude 42.27 - Longitude = -2.01
Index is: 291
ID is: 291 - WayPoint is: GARVU - Latitude = N42▒10'15.99" - Longitude = W002▒04'40.00"
wayPoint name = GARVU - Latitude 42.17 - Longitude = -2.08
Index is: 292
ID is: 292 - WayPoint is: BANEV - Latitude = N41▒30'08.99" - Longitude = W002▒30'52.00"
wayPoint name = BANEV - Latitude 41.50 - Longitude = -2.51
Index is: 293
ID is: 293 - WayPoint is: BAN - Latitude = N41▒19'25.00" - Longitude = W002▒37'47.00"
wayPoint name = BAN - Latitude 41.32 - Longitude = -2.63
Index is: 294
ID is: 294 - WayPoint is: GOTOR - Latitude = N40▒06'38.99" - Longitude = W003▒43'28.00"
wayPoint name = GOTOR - Latitude 40.11 - Longitude = -3.72
Index is: 295
ID is: 295 - WayPoint is: KAMPO - Latitude = N39▒44'00.00" - Longitude = W004▒03'18.99"
wayPoint name = KAMPO - Latitude 39.73 - Longitude = -4.06
Index is: 296
ID is: 296 - WayPoint is: MONTO - Latitude = N39▒13'17.99" - Longitude = W004▒29'49.00"
wayPoint name = MONTO - Latitude 39.22 - Longitude = -4.50
Index is: 297
ID is: 297 - WayPoint is: MOLIN - Latitude = N39▒00'00.00" - Longitude = W004▒41'08.99"
wayPoint name = MOLIN - Latitude 39.00 - Longitude = -4.69
Index is: 298
ID is: 298 - WayPoint is: HIJ - Latitude = N38▒30'29.00" - Longitude = W005▒05'58.99"
wayPoint name = HIJ - Latitude 38.51 - Longitude = -5.10
Index is: 299
ID is: 299 - WayPoint is: SVL - Latitude = N37▒25'39.00" - Longitude = W005▒45'45.00"
wayPoint name = SVL - Latitude 37.43 - Longitude = -5.76
Index is: 300
ID is: 300 - WayPoint is: SANTA - Latitude = N37▒40'07.00" - Longitude = W006▒17'53.99"
wayPoint name = SANTA - Latitude 37.67 - Longitude = -6.30
Index is: 301
ID is: 301 - WayPoint is: ROSAL - Latitude = N38▒01'16.99" - Longitude = W007▒06'03.99"
wayPoint name = ROSAL - Latitude 38.02 - Longitude = -7.10
Index is: 302
ID is: 302 - WayPoint is: OKASI - Latitude = N48▒05'00.00" - Longitude = E002▒46'40.00"
wayPoint name = OKASI - Latitude 48.08 - Longitude = 2.78
Index is: 303
ID is: 303 - WayPoint is: SIQLE - Latitude = N47▒01'15.99" - Longitude = E003▒14'12.99"
wayPoint name = SIQLE - Latitude 47.02 - Longitude = 3.24
Index is: 304
ID is: 304 - WayPoint is: UTUVA - Latitude = N45▒51'48.00" - Longitude = E003▒29'27.99"
wayPoint name = UTUVA - Latitude 45.86 - Longitude = 3.49
Index is: 305
ID is: 305 - WayPoint is: LERGA - Latitude = N45▒15'26.00" - Longitude = E003▒45'00.99"
wayPoint name = LERGA - Latitude 45.26 - Longitude = 3.75
Index is: 306
ID is: 306 - WayPoint is: LANVI - Latitude = N48▒18'42.00" - Longitude = E005▒47'50.00"
wayPoint name = LANVI - Latitude 48.31 - Longitude = 5.80
Index is: 307
ID is: 307 - WayPoint is: EPL - Latitude = N48▒19'03.99" - Longitude = E006▒03'33.99"
wayPoint name = EPL - Latitude 48.32 - Longitude = 6.06
Index is: 308
ID is: 308 - WayPoint is: OBAKI - Latitude = N48▒21'57.00" - Longitude = E006▒25'49.99"
wayPoint name = OBAKI - Latitude 48.37 - Longitude = 6.43
Index is: 309
ID is: 309 - WayPoint is: POGOL - Latitude = N48▒23'56.99" - Longitude = E006▒41'36.00"
wayPoint name = POGOL - Latitude 48.40 - Longitude = 6.69
Index is: 310
ID is: 310 - WayPoint is: OBORN - Latitude = N48▒27'42.99" - Longitude = E007▒12'06.00"
wayPoint name = OBORN - Latitude 48.46 - Longitude = 7.20
Index is: 311
ID is: 311 - WayPoint is: LUPEN - Latitude = N48▒26'06.00" - Longitude = E007▒44'01.00"
wayPoint name = LUPEN - Latitude 48.43 - Longitude = 7.73
Index is: 312
ID is: 312 - WayPoint is: GESLU - Latitude = N48▒27'42.99" - Longitude = E009▒41'19.00"
wayPoint name = GESLU - Latitude 48.46 - Longitude = 9.69
Index is: 313
ID is: 313 - WayPoint is: LURER - Latitude = N48▒27'44.99" - Longitude = E010▒36'03.00"
wayPoint name = LURER - Latitude 48.46 - Longitude = 10.60
Index is: 314
ID is: 314 - WayPoint is: LELTA - Latitude = N48▒29'35.00" - Longitude = E010▒57'18.99"
wayPoint name = LELTA - Latitude 48.49 - Longitude = 10.96
Index is: 315
ID is: 315 - WayPoint is: MAH - Latitude = N48▒15'48.00" - Longitude = E011▒18'42.99"
wayPoint name = MAH - Latitude 48.26 - Longitude = 11.31
Index is: 316
ID is: 316 - WayPoint is: OTT - Latitude = N48▒10'48.99" - Longitude = E011▒48'59.99"
wayPoint name = OTT - Latitude 48.18 - Longitude = 11.82
Index is: 317
ID is: 317 - WayPoint is: EBEDA - Latitude = N48▒09'37.00" - Longitude = E012▒07'36.99"
wayPoint name = EBEDA - Latitude 48.16 - Longitude = 12.13
Index is: 318
ID is: 318 - WayPoint is: AMDID - Latitude = N48▒05'49.99" - Longitude = E012▒23'49.00"
wayPoint name = AMDID - Latitude 48.10 - Longitude = 12.40
Index is: 319
ID is: 319 - WayPoint is: TITIG - Latitude = N48▒03'31.99" - Longitude = E012▒33'34.00"
wayPoint name = TITIG - Latitude 48.06 - Longitude = 12.56
Index is: 320
ID is: 320 - WayPoint is: NEMAL - Latitude = N47▒55'04.99" - Longitude = E013▒29'53.99"
wayPoint name = NEMAL - Latitude 47.92 - Longitude = 13.50
Index is: 321
ID is: 321 - WayPoint is: ARSIN - Latitude = N47▒34'01.99" - Longitude = E016▒45'13.00"
wayPoint name = ARSIN - Latitude 47.57 - Longitude = 16.75
Index is: 322
ID is: 322 - WayPoint is: VAJDI - Latitude = N47▒22'32.00" - Longitude = E018▒17'08.99"
wayPoint name = VAJDI - Latitude 47.38 - Longitude = 18.29
Index is: 323
ID is: 323 - WayPoint is: GILEP - Latitude = N47▒29'00.00" - Longitude = E018▒15'32.00"
wayPoint name = GILEP - Latitude 47.48 - Longitude = 18.26
Index is: 324
ID is: 324 - WayPoint is: BEGLA - Latitude = N47▒49'50.99" - Longitude = E017▒06'52.00"
wayPoint name = BEGLA - Latitude 47.83 - Longitude = 17.11
Index is: 325
ID is: 325 - WayPoint is: MOVOS - Latitude = N47▒54'40.99" - Longitude = E016▒26'13.99"
wayPoint name = MOVOS - Latitude 47.91 - Longitude = 16.44
Index is: 326
ID is: 326 - WayPoint is: RENKA - Latitude = N48▒35'05.00" - Longitude = E013▒30'18.99"
wayPoint name = RENKA - Latitude 48.58 - Longitude = 13.51
Index is: 327
ID is: 327 - WayPoint is: GONBA - Latitude = N48▒41'16.00" - Longitude = E013▒04'33.00"
wayPoint name = GONBA - Latitude 48.69 - Longitude = 13.08
Index is: 328
ID is: 328 - WayPoint is: STAUB - Latitude = N48▒47'09.00" - Longitude = E012▒39'28.99"
wayPoint name = STAUB - Latitude 48.79 - Longitude = 12.66
Index is: 329
ID is: 329 - WayPoint is: MAMOR - Latitude = N48▒53'08.99" - Longitude = E012▒13'19.99"
wayPoint name = MAMOR - Latitude 48.89 - Longitude = 12.22
Index is: 330
ID is: 330 - WayPoint is: UNKUL - Latitude = N49▒08'13.99" - Longitude = E011▒27'34.99"
wayPoint name = UNKUL - Latitude 49.14 - Longitude = 11.46
Index is: 331
ID is: 331 - WayPoint is: UPALA - Latitude = N49▒12'52.00" - Longitude = E011▒13'16.99"
wayPoint name = UPALA - Latitude 49.21 - Longitude = 11.22
Index is: 332
ID is: 332 - WayPoint is: PETIX - Latitude = N49▒20'28.00" - Longitude = E010▒45'16.99"
wayPoint name = PETIX - Latitude 49.34 - Longitude = 10.75
Index is: 333
ID is: 333 - WayPoint is: COSJE - Latitude = N49▒43'03.00" - Longitude = E009▒56'48.99"
wayPoint name = COSJE - Latitude 49.72 - Longitude = 9.95
Index is: 334
ID is: 334 - WayPoint is: RIDSU - Latitude = N49▒44'56.00" - Longitude = E008▒28'48.00"
wayPoint name = RIDSU - Latitude 49.75 - Longitude = 8.48
Index is: 335
ID is: 335 - WayPoint is: DONAB - Latitude = N49▒49'15.99" - Longitude = E008▒01'45.00"
wayPoint name = DONAB - Latitude 49.82 - Longitude = 8.03
Index is: 336
ID is: 336 - WayPoint is: SOBRA - Latitude = N49▒51'38.99" - Longitude = E007▒46'32.00"
wayPoint name = SOBRA - Latitude 49.86 - Longitude = 7.78
Index is: 337
ID is: 337 - WayPoint is: ULKIG - Latitude = N49▒52'11.00" - Longitude = E007▒43'09.99"
wayPoint name = ULKIG - Latitude 49.87 - Longitude = 7.72
Index is: 338
ID is: 338 - WayPoint is: RUDOT - Latitude = N49▒59'35.99" - Longitude = E006▒54'16.00"
wayPoint name = RUDOT - Latitude 49.99 - Longitude = 6.90
Index is: 339
ID is: 339 - WayPoint is: BITBU - Latitude = N49▒58'58.99" - Longitude = E006▒33'41.99"
wayPoint name = BITBU - Latitude 49.98 - Longitude = 6.56
Index is: 340
ID is: 340 - WayPoint is: ASMOX - Latitude = N49▒54'09.99" - Longitude = E006▒16'34.00"
wayPoint name = ASMOX - Latitude 49.90 - Longitude = 6.28
Index is: 341
ID is: 341 - WayPoint is: NISIV - Latitude = N49▒53'33.99" - Longitude = E006▒14'34.99"
wayPoint name = NISIV - Latitude 49.89 - Longitude = 6.24
Index is: 342
ID is: 342 - WayPoint is: DIEKIRCH - Latitude = N49▒51'41.00" - Longitude = E006▒07'46.99"
wayPoint name = DIEKIRCH - Latitude 49.86 - Longitude = 6.13
Index is: 343
ID is: 343 - WayPoint is: IDOSA - Latitude = N49▒44'30.00" - Longitude = E005▒52'11.00"
wayPoint name = IDOSA - Latitude 49.74 - Longitude = 5.87
Index is: 344
ID is: 344 - WayPoint is: TOLVU - Latitude = N49▒37'30.99" - Longitude = E005▒22'18.00"
wayPoint name = TOLVU - Latitude 49.63 - Longitude = 5.37
Index is: 345
ID is: 345 - WayPoint is: RAPOR - Latitude = N49▒35'28.99" - Longitude = E005▒12'47.00"
wayPoint name = RAPOR - Latitude 49.59 - Longitude = 5.21
Index is: 346
ID is: 346 - WayPoint is: VEDUS - Latitude = N49▒35'41.00" - Longitude = E004▒46'52.99"
wayPoint name = VEDUS - Latitude 49.59 - Longitude = 4.78
Index is: 347
ID is: 347 - WayPoint is: SEGRE - Latitude = N41▒01'21.99" - Longitude = W002▒22'35.00"
wayPoint name = SEGRE - Latitude 41.02 - Longitude = -2.38
Index is: 348
ID is: 348 - WayPoint is: YAKXU - Latitude = N42▒05'55.00" - Longitude = W001▒12'45.99"
wayPoint name = YAKXU - Latitude 42.10 - Longitude = -1.21
Index is: 349
ID is: 349 - WayPoint is: RONNY - Latitude = N42▒25'45.00" - Longitude = W000▒50'41.00"
wayPoint name = RONNY - Latitude 42.43 - Longitude = -0.84
Index is: 350
ID is: 350 - WayPoint is: TOPTU - Latitude = N42▒47'48.00" - Longitude = W000▒11'37.00"
wayPoint name = TOPTU - Latitude 42.80 - Longitude = -0.19
Index is: 351
ID is: 351 - WayPoint is: BUROX - Latitude = N43▒37'49.99" - Longitude = E001▒15'17.99"
wayPoint name = BUROX - Latitude 43.63 - Longitude = 1.25
Index is: 352
ID is: 352 - WayPoint is: DITEV - Latitude = N44▒29'00.99" - Longitude = E002▒54'08.99"
wayPoint name = DITEV - Latitude 44.48 - Longitude = 2.90
Index is: 353
ID is: 353 - WayPoint is: NINUN - Latitude = N44▒46'07.00" - Longitude = E003▒33'45.99"
wayPoint name = NINUN - Latitude 44.77 - Longitude = 3.56
Index is: 354
ID is: 354 - WayPoint is: MEZIN - Latitude = N45▒01'02.00" - Longitude = E004▒11'45.00"
wayPoint name = MEZIN - Latitude 45.02 - Longitude = 4.20
Index is: 355
ID is: 355 - WayPoint is: LATAM - Latitude = N45▒02'01.99" - Longitude = E004▒14'21.00"
wayPoint name = LATAM - Latitude 45.03 - Longitude = 4.24
Index is: 356
ID is: 356 - WayPoint is: OTROT - Latitude = N45▒06'49.00" - Longitude = E004▒26'44.00"
wayPoint name = OTROT - Latitude 45.11 - Longitude = 4.45
Index is: 357
ID is: 357 - WayPoint is: ETREK - Latitude = N45▒11'15.99" - Longitude = E004▒38'19.00"
wayPoint name = ETREK - Latitude 45.19 - Longitude = 4.64
Index is: 358
ID is: 358 - WayPoint is: LUXAN - Latitude = N45▒22'29.00" - Longitude = E005▒07'58.00"
wayPoint name = LUXAN - Latitude 45.37 - Longitude = 5.13
Index is: 359
ID is: 359 - WayPoint is: ARKOX - Latitude = N45▒26'23.99" - Longitude = E005▒18'27.00"
wayPoint name = ARKOX - Latitude 45.44 - Longitude = 5.31
Index is: 360
ID is: 360 - WayPoint is: LATOURDUPIN - Latitude = N45▒29'19.99" - Longitude = E005▒26'21.00"
wayPoint name = LATOURDUPIN - Latitude 45.49 - Longitude = 5.44
Index is: 361
ID is: 361 - WayPoint is: GIPNO - Latitude = N45▒33'36.00" - Longitude = E005▒31'45.00"
wayPoint name = GIPNO - Latitude 45.56 - Longitude = 5.53
Index is: 362
ID is: 362 - WayPoint is: NAVLA - Latitude = N45▒40'01.99" - Longitude = E005▒40'01.00"
wayPoint name = NAVLA - Latitude 45.67 - Longitude = 5.67
Index is: 363
ID is: 363 - WayPoint is: SOPLO - Latitude = N45▒43'44.00" - Longitude = E005▒44'45.00"
wayPoint name = SOPLO - Latitude 45.73 - Longitude = 5.75
Index is: 364
ID is: 364 - WayPoint is: OMASI - Latitude = N45▒54'21.99" - Longitude = E005▒58'27.00"
wayPoint name = OMASI - Latitude 45.91 - Longitude = 5.97
Index is: 365
ID is: 365 - WayPoint is: KINNI - Latitude = N46▒05'19.99" - Longitude = E006▒12'42.00"
wayPoint name = KINNI - Latitude 46.09 - Longitude = 6.21
Index is: 366
ID is: 366 - WayPoint is: MOLUS - Latitude = N46▒26'37.99" - Longitude = E006▒40'45.99"
wayPoint name = MOLUS - Latitude 46.44 - Longitude = 6.68
Index is: 367
ID is: 367 - WayPoint is: SOSAL - Latitude = N46▒33'28.99" - Longitude = E006▒53'03.99"
wayPoint name = SOSAL - Latitude 46.56 - Longitude = 6.88
Index is: 368
ID is: 368 - WayPoint is: TELNO - Latitude = N46▒46'18.99" - Longitude = E007▒16'14.99"
wayPoint name = TELNO - Latitude 46.77 - Longitude = 7.27
Index is: 369
ID is: 369 - WayPoint is: KORED - Latitude = N46▒51'01.99" - Longitude = E007▒24'50.99"
wayPoint name = KORED - Latitude 46.85 - Longitude = 7.41
Index is: 370
ID is: 370 - WayPoint is: KONOL - Latitude = N46▒59'43.00" - Longitude = E007▒40'50.99"
wayPoint name = KONOL - Latitude 47.00 - Longitude = 7.68
Index is: 371
ID is: 371 - WayPoint is: BERSU - Latitude = N47▒08'07.99" - Longitude = E007▒56'28.99"
wayPoint name = BERSU - Latitude 47.14 - Longitude = 7.94
Index is: 372
ID is: 372 - WayPoint is: SONOM - Latitude = N47▒47'02.99" - Longitude = E008▒53'45.99"
wayPoint name = SONOM - Latitude 47.78 - Longitude = 8.90
Index is: 373
ID is: 373 - WayPoint is: LADOL - Latitude = N48▒09'59.99" - Longitude = E008▒57'11.99"
wayPoint name = LADOL - Latitude 48.17 - Longitude = 8.95
Index is: 374
ID is: 374 - WayPoint is: EMPAX - Latitude = N48▒27'42.99" - Longitude = E008▒59'53.00"
wayPoint name = EMPAX - Latitude 48.46 - Longitude = 9.00
Index is: 375
ID is: 375 - WayPoint is: NELLI - Latitude = N48▒37'40.00" - Longitude = E009▒01'24.99"
wayPoint name = NELLI - Latitude 48.63 - Longitude = 9.02
Index is: 376
ID is: 376 - WayPoint is: KOVAN - Latitude = N48▒52'57.00" - Longitude = E009▒05'02.99"
wayPoint name = KOVAN - Latitude 48.88 - Longitude = 9.08
Index is: 377
ID is: 377 - WayPoint is: OKIBA - Latitude = N49▒12'52.99" - Longitude = E009▒18'57.99"
wayPoint name = OKIBA - Latitude 49.21 - Longitude = 9.32
Index is: 378
ID is: 378 - WayPoint is: ROLSO - Latitude = N49▒21'15.00" - Longitude = E009▒18'19.00"
wayPoint name = ROLSO - Latitude 49.35 - Longitude = 9.31
Index is: 379
ID is: 379 - WayPoint is: RIMKI - Latitude = N49▒44'56.00" - Longitude = E009▒21'50.00"
wayPoint name = RIMKI - Latitude 49.75 - Longitude = 9.36
Index is: 380
ID is: 380 - WayPoint is: LOHRE - Latitude = N50▒04'01.00" - Longitude = E009▒29'11.00"
wayPoint name = LOHRE - Latitude 50.07 - Longitude = 9.49
Index is: 381
ID is: 381 - WayPoint is: TIKNI - Latitude = N50▒24'34.99" - Longitude = E009▒52'23.99"
wayPoint name = TIKNI - Latitude 50.41 - Longitude = 9.87
Index is: 382
ID is: 382 - WayPoint is: GAPLA - Latitude = N50▒39'13.99" - Longitude = E010▒16'49.99"
wayPoint name = GAPLA - Latitude 50.65 - Longitude = 10.28
Index is: 383
ID is: 383 - WayPoint is: TAMEB - Latitude = N50▒48'28.00" - Longitude = E010▒43'48.00"
wayPoint name = TAMEB - Latitude 50.81 - Longitude = 10.73
Index is: 384
ID is: 384 - WayPoint is: WEMAR - Latitude = N50▒58'58.99" - Longitude = E011▒15'06.99"
wayPoint name = WEMAR - Latitude 50.98 - Longitude = 11.25
Index is: 385
ID is: 385 - WayPoint is: RELKO - Latitude = N51▒03'34.99" - Longitude = E011▒29'01.99"
wayPoint name = RELKO - Latitude 51.06 - Longitude = 11.48
Index is: 386
ID is: 386 - WayPoint is: NAMUB - Latitude = N51▒07'24.99" - Longitude = E011▒40'42.99"
wayPoint name = NAMUB - Latitude 51.12 - Longitude = 11.68
Index is: 387
ID is: 387 - WayPoint is: NOTGO - Latitude = N51▒12'38.00" - Longitude = E011▒56'48.00"
wayPoint name = NOTGO - Latitude 51.21 - Longitude = 11.95
Index is: 388
ID is: 388 - WayPoint is: RUDAK - Latitude = N51▒46'42.00" - Longitude = E012▒54'57.99"
wayPoint name = RUDAK - Latitude 51.78 - Longitude = 12.92
Index is: 389
ID is: 389 - WayPoint is: VFA - Latitude = N37▒00'48.99" - Longitude = W007▒58'30.00"
wayPoint name = VFA - Latitude 37.01 - Longitude = -7.98
Index is: 390
ID is: 390 - WayPoint is: MINTA - Latitude = N37▒07'43.99" - Longitude = W007▒22'59.99"
wayPoint name = MINTA - Latitude 37.13 - Longitude = -7.38
Index is: 391
ID is: 391 - WayPoint is: OSLEP - Latitude = N37▒09'54.99" - Longitude = W007▒11'30.99"
wayPoint name = OSLEP - Latitude 37.17 - Longitude = -7.19
Index is: 392
ID is: 392 - WayPoint is: OXACA - Latitude = N37▒57'00.00" - Longitude = W006▒00'00.00"
wayPoint name = OXACA - Latitude 37.95 - Longitude = -6.00
Index is: 393
ID is: 393 - WayPoint is: DIONY - Latitude = N38▒35'49.99" - Longitude = W005▒28'36.99"
wayPoint name = DIONY - Latitude 38.60 - Longitude = -5.48
Index is: 394
ID is: 394 - WayPoint is: PARKA - Latitude = N39▒00'00.00" - Longitude = W005▒09'00.00"
wayPoint name = PARKA - Latitude 39.00 - Longitude = -5.15
Index is: 395
ID is: 395 - WayPoint is: TLD - Latitude = N39▒58'09.99" - Longitude = W004▒20'15.00"
wayPoint name = TLD - Latitude 39.97 - Longitude = -4.34
Index is: 396
ID is: 396 - WayPoint is: SIE - Latitude = N41▒09'05.99" - Longitude = W003▒36'16.99"
wayPoint name = SIE - Latitude 41.15 - Longitude = -3.60
Index is: 397
ID is: 397 - WayPoint is: EDIGO - Latitude = N41▒30'15.00" - Longitude = W003▒24'41.99"
wayPoint name = EDIGO - Latitude 41.50 - Longitude = -3.41
Index is: 398
ID is: 398 - WayPoint is: DGO - Latitude = N42▒27'11.99" - Longitude = W002▒52'51.00"
wayPoint name = DGO - Latitude 42.45 - Longitude = -2.88
Index is: 399
ID is: 399 - WayPoint is: ABRIX - Latitude = N43▒38'47.00" - Longitude = W001▒57'44.99"
wayPoint name = ABRIX - Latitude 43.65 - Longitude = -1.96
Index is: 400
ID is: 400 - WayPoint is: ASKAN - Latitude = N45▒02'39.99" - Longitude = W001▒02'22.99"
wayPoint name = ASKAN - Latitude 45.04 - Longitude = -1.04
Index is: 401
ID is: 401 - WayPoint is: ETPAR - Latitude = N45▒11'44.99" - Longitude = W000▒51'42.00"
wayPoint name = ETPAR - Latitude 45.20 - Longitude = -0.86
Index is: 402
ID is: 402 - WayPoint is: POI - Latitude = N46▒34'52.00" - Longitude = E000▒17'52.99"
wayPoint name = POI - Latitude 46.58 - Longitude = 0.30
Index is: 403
ID is: 403 - WayPoint is: BOKNO - Latitude = N47▒02'48.99" - Longitude = E000▒41'30.00"
wayPoint name = BOKNO - Latitude 47.05 - Longitude = 0.69
Index is: 404
ID is: 404 - WayPoint is: DEVRO - Latitude = N47▒29'43.99" - Longitude = E000▒44'18.99"
wayPoint name = DEVRO - Latitude 47.50 - Longitude = 0.74
Index is: 405
ID is: 405 - WayPoint is: VANAD - Latitude = N47▒50'14.00" - Longitude = E000▒54'26.00"
wayPoint name = VANAD - Latitude 47.84 - Longitude = 0.91
Index is: 406
ID is: 406 - WayPoint is: PIWIZ - Latitude = N48▒12'54.00" - Longitude = E001▒05'55.99"
wayPoint name = PIWIZ - Latitude 48.22 - Longitude = 1.10
Index is: 407
ID is: 407 - WayPoint is: VADOM - Latitude = N48▒33'01.99" - Longitude = E001▒16'14.99"
wayPoint name = VADOM - Latitude 48.55 - Longitude = 1.27
Index is: 408
ID is: 408 - WayPoint is: BAMES - Latitude = N48▒58'30.99" - Longitude = E001▒29'10.00"
wayPoint name = BAMES - Latitude 48.98 - Longitude = 1.49
Index is: 409
ID is: 409 - WayPoint is: ARSAF - Latitude = N49▒21'03.00" - Longitude = E002▒08'03.00"
wayPoint name = ARSAF - Latitude 49.35 - Longitude = 2.13
Index is: 410
ID is: 410 - WayPoint is: KOPOR - Latitude = N49▒30'50.99" - Longitude = E002▒25'17.00"
wayPoint name = KOPOR - Latitude 49.51 - Longitude = 2.42
Index is: 411
ID is: 411 - WayPoint is: EGOZE - Latitude = N49▒33'09.99" - Longitude = E002▒29'22.00"
wayPoint name = EGOZE - Latitude 49.55 - Longitude = 2.49
Index is: 412
ID is: 412 - WayPoint is: NURMO - Latitude = N49▒49'33.99" - Longitude = E002▒45'18.99"
wayPoint name = NURMO - Latitude 49.83 - Longitude = 2.76
Index is: 413
ID is: 413 - WayPoint is: PERON - Latitude = N49▒54'45.00" - Longitude = E002▒50'23.99"
wayPoint name = PERON - Latitude 49.91 - Longitude = 2.84
Index is: 414
ID is: 414 - WayPoint is: SULEX - Latitude = N50▒00'00.00" - Longitude = E002▒55'31.99"
wayPoint name = SULEX - Latitude 50.00 - Longitude = 2.93
Index is: 415
ID is: 415 - WayPoint is: CMB - Latitude = N50▒13'41.00" - Longitude = E003▒09'05.00"
wayPoint name = CMB - Latitude 50.23 - Longitude = 3.15
Index is: 416
ID is: 416 - WayPoint is: VEKIN - Latitude = N50▒24'14.99" - Longitude = E003▒16'29.99"
wayPoint name = VEKIN - Latitude 50.40 - Longitude = 3.27
Index is: 417
ID is: 417 - WayPoint is: ARVOL - Latitude = N50▒32'45.00" - Longitude = E003▒29'48.99"
wayPoint name = ARVOL - Latitude 50.55 - Longitude = 3.50
Index is: 418
ID is: 418 - WayPoint is: LATID - Latitude = N14▒28'35.00" - Longitude = E077▒56'55.99"
wayPoint name = LATID - Latitude 14.48 - Longitude = 77.95
Index is: 419
ID is: 419 - WayPoint is: VIRAM - Latitude = N15▒21'33.99" - Longitude = E078▒05'55.00"
wayPoint name = VIRAM - Latitude 15.36 - Longitude = 78.10
Index is: 420
ID is: 420 - WayPoint is: BOSGA - Latitude = N16▒12'33.99" - Longitude = E078▒14'16.00"
wayPoint name = BOSGA - Latitude 16.21 - Longitude = 78.24
Index is: 421
ID is: 421 - WayPoint is: SAKRO - Latitude = N16▒34'00.16" - Longitude = E078▒17'47.35"
wayPoint name = SAKRO - Latitude 16.57 - Longitude = 78.30
Index is: 422
ID is: 422 - WayPoint is: HIA - Latitude = N17▒13'40.10" - Longitude = E078▒24'20.87"
wayPoint name = HIA - Latitude 17.23 - Longitude = 78.41
Index is: 423
ID is: 423 - WayPoint is: BUSBO - Latitude = N19▒14'58.00" - Longitude = E078▒07'30.00"
wayPoint name = BUSBO - Latitude 19.25 - Longitude = 78.12
Index is: 424
ID is: 424 - WayPoint is: ASIPI - Latitude = N20▒31'29.99" - Longitude = E077▒52'44.99"
wayPoint name = ASIPI - Latitude 20.52 - Longitude = 77.88
Index is: 425
ID is: 425 - WayPoint is: TAMID - Latitude = N20▒41'17.99" - Longitude = E077▒50'56.00"
wayPoint name = TAMID - Latitude 20.69 - Longitude = 77.85
Index is: 426
ID is: 426 - WayPoint is: KAMLO - Latitude = N20▒55'08.99" - Longitude = E077▒48'02.99"
wayPoint name = KAMLO - Latitude 20.92 - Longitude = 77.80
Index is: 427
ID is: 427 - WayPoint is: UPTAR - Latitude = N21▒30'42.00" - Longitude = E077▒40'54.99"
wayPoint name = UPTAR - Latitude 21.51 - Longitude = 77.68
Index is: 428
ID is: 428 - WayPoint is: BIGIL - Latitude = N22▒07'01.99" - Longitude = E077▒33'56.00"
wayPoint name = BIGIL - Latitude 22.12 - Longitude = 77.57
Index is: 429
ID is: 429 - WayPoint is: BPL - Latitude = N23▒16'59.73" - Longitude = E077▒20'11.85"
wayPoint name = BPL - Latitude 23.28 - Longitude = 77.34
Index is: 430
ID is: 430 - WayPoint is: PUKES - Latitude = N24▒42'02.00" - Longitude = E077▒16'11.99"
wayPoint name = PUKES - Latitude 24.70 - Longitude = 77.27
Index is: 431
ID is: 431 - WayPoint is: BUKLO - Latitude = N25▒00'01.00" - Longitude = E077▒15'26.00"
wayPoint name = BUKLO - Latitude 25.00 - Longitude = 77.26
Index is: 432
ID is: 432 - WayPoint is: BAVOX - Latitude = N26▒08'30.99" - Longitude = E077▒12'55.99"
wayPoint name = BAVOX - Latitude 26.14 - Longitude = 77.22
Index is: 433
ID is: 433 - WayPoint is: AURANGABAD - Latitude = N19▒51'39.95" - Longitude = E075▒24'18.90"
wayPoint name = AURANGABAD - Latitude 19.86 - Longitude = 75.41
Index is: 434
ID is: 434 - WayPoint is: DUBOX - Latitude = N20▒22'15.00" - Longitude = E076▒49'56.00"
wayPoint name = DUBOX - Latitude 20.37 - Longitude = 76.83
Index is: 435
ID is: 435 - WayPoint is: NINAT - Latitude = N20▒32'48.00" - Longitude = E077▒24'56.00"
wayPoint name = NINAT - Latitude 20.55 - Longitude = 77.42
Index is: 436
ID is: 436 - WayPoint is: NAGPUR - Latitude = N21▒04'53.22" - Longitude = E079▒03'22.67"
wayPoint name = NAGPUR - Latitude 21.08 - Longitude = 79.06
Index is: 437
ID is: 437 - WayPoint is: TEGIG - Latitude = N21▒30'09.00" - Longitude = E080▒35'37.00"
wayPoint name = TEGIG - Latitude 21.50 - Longitude = 80.59
Index is: 438
ID is: 438 - WayPoint is: DOSAT - Latitude = N21▒41'32.99" - Longitude = E081▒18'24.00"
wayPoint name = DOSAT - Latitude 21.69 - Longitude = 81.31
Index is: 439
ID is: 439 - WayPoint is: OPONI - Latitude = N21▒47'03.00" - Longitude = E081▒38'24.00"
wayPoint name = OPONI - Latitude 21.78 - Longitude = 81.64
Index is: 440
ID is: 440 - WayPoint is: NIPAD - Latitude = N21▒52'17.99" - Longitude = E081▒59'52.99"
wayPoint name = NIPAD - Latitude 21.87 - Longitude = 82.00
Index is: 441
ID is: 441 - WayPoint is: OTABA - Latitude = N22▒11'02.99" - Longitude = E083▒19'22.99"
wayPoint name = OTABA - Latitude 22.18 - Longitude = 83.32
Index is: 442
ID is: 442 - WayPoint is: KINKI - Latitude = N22▒19'17.99" - Longitude = E083▒55'38.00"
wayPoint name = KINKI - Latitude 22.32 - Longitude = 83.93
Index is: 443
ID is: 443 - WayPoint is: AGROM - Latitude = N22▒31'44.99" - Longitude = E084▒49'59.99"
wayPoint name = AGROM - Latitude 22.53 - Longitude = 84.83
Index is: 444
ID is: 444 - WayPoint is: JAMSHEDPUR - Latitude = N22▒48'47.47" - Longitude = E086▒10'26.15"
wayPoint name = JAMSHEDPUR - Latitude 22.81 - Longitude = 86.17
Index is: 445
ID is: 445 - WayPoint is: KAMGU - Latitude = N14▒58'31.00" - Longitude = E079▒25'12.00"
wayPoint name = KAMGU - Latitude 14.98 - Longitude = 79.42
Index is: 446
ID is: 446 - WayPoint is: KIKUR - Latitude = N15▒58'54.99" - Longitude = E079▒10'32.00"
wayPoint name = KIKUR - Latitude 15.98 - Longitude = 79.18
Index is: 447
ID is: 447 - WayPoint is: ANDAV - Latitude = N17▒28'18.00" - Longitude = E078▒48'49.00"
wayPoint name = ANDAV - Latitude 17.47 - Longitude = 78.81
Index is: 448
ID is: 448 - WayPoint is: ALBED - Latitude = N18▒07'01.99" - Longitude = E078▒39'23.99"
wayPoint name = ALBED - Latitude 18.12 - Longitude = 78.66
Index is: 449
ID is: 449 - WayPoint is: LAROB - Latitude = N19▒10'14.00" - Longitude = E078▒23'40.00"
wayPoint name = LAROB - Latitude 19.17 - Longitude = 78.39
Index is: 450
ID is: 450 - WayPoint is: SUDEL - Latitude = N19▒34'17.99" - Longitude = E078▒17'18.99"
wayPoint name = SUDEL - Latitude 19.57 - Longitude = 78.29
Index is: 451
ID is: 451 - WayPoint is: TASEX - Latitude = N20▒33'54.00" - Longitude = E078▒01'36.99"
wayPoint name = TASEX - Latitude 20.57 - Longitude = 78.03
Index is: 452
ID is: 452 - WayPoint is: RENAG - Latitude = N22▒03'12.00" - Longitude = E077▒39'32.00"
wayPoint name = RENAG - Latitude 22.05 - Longitude = 77.66
Index is: 453
ID is: 453 - WayPoint is: BHOPAL - Latitude = N23▒16'59.73" - Longitude = E077▒20'11.85"
wayPoint name = BHOPAL - Latitude 23.28 - Longitude = 77.34
Index is: 454
ID is: 454 - WayPoint is: INTIL - Latitude = N26▒27'51.00" - Longitude = E076▒32'40.99"
wayPoint name = INTIL - Latitude 26.46 - Longitude = 76.54
read wayPoints database result = True
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


## airlines routes waypoints

$ python manage.py AirlineRoutesWayPointsDatabaseLoad

Index is: 9
order is 10
wayPoint name is PUKES
latitude is N24▒42'02.00"
longitude is E077▒16'11.99"
----------- 10 -----------
Index is: 10
order is 11
wayPoint name is BUKLO
latitude is N25▒00'01.00"
longitude is E077▒15'26.00"
----------- 11 -----------
Index is: 11
order is 12
wayPoint name is BAVOX
latitude is N26▒08'30.99"
longitude is E077▒12'55.99"
----------- 12 -----------
Index is: 12
order is 13
wayPoint name is INTIL
latitude is N26▒27'51.00"
longitude is E076▒32'40.99"
----------- 13 -----------
(virtualEnv)
rober@RobertPastor MINGW64 ~/git/Airlines-Services/Airlines-Services (master)
$


## check the database table called airlines_airlinerouteswaypoints

SELECT * FROM public.airlines_airlineroutewaypoints
ORDER BY id ASC 

Successfully run. Total query runtime: 2 secs 415 msec.
569 rows affected.

