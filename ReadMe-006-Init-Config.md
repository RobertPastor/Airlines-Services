
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
