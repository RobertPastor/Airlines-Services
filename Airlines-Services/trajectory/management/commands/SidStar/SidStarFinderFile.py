

'''
Created on 11 September 2026

@author: robert
class dedicated to find SID STAR EXCEL xlsx files

'''

import os
import logging
logger = logging.getLogger(__name__)
from trajectory.management.commands.SidStar.SidStarDatabaseLoaderFile import SidStarLoaderOne
from trajectory.Environment.WayPoints.WayPointsDatabaseFile import WayPointsDatabase

class SidStarFinder(object):

    FilesFolder = ""
    FilesPrefixSID = "SID"
    FilesPrefixSTAR = "STAR"
    sheetName = "WayPoints"
    fileNameSeparator = "-"

    # Initializer / Instance attributes
    def __init__(self):

        self.className = self.__class__.__name__
        self.FileNamePrefixList = ["SID","STAR"]
        self.sheetName = "WayPoints"
            
        # SID and STAR files are located in the same folder as this python file
        self.FilesFolder = os.path.dirname(__file__)
    
        logger.info ( self.className + ': file folder= {0}'.format(self.FilesFolder) )
        self.sheetName = "WayPoints"

    def check(self):
        logger.info(" --------check-------- ")
        if not os.path.isdir(self.FilesFolder):
            raise ValueError(f"Provided path is not a directory: {self.FilesFolder}")
        logger.info(self.className + " - folder {0} is a directory ".format( self.FilesFolder ))

    def getFilesFolder(self):
        return self.FilesFolder

    def isSID(self):
        pass

    # loop through all the files available in the folder
    def findSidStarExcelFiles(self):
        logger.info(" --------findSidStarExcelFiles-------- ")
        for file in os.listdir( self.getFilesFolder() ):
            full_path = os.path.join(self.getFilesFolder(), file)
            if ( os.path.isfile(full_path) and \
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) and \
                      ( file.endswith (".xlsx")  ) ):
                logger.info ( self.className + str(file) )
                yield full_path

    def getAirports(self):
        logger.info(" --------getAirports-------- ")
        for file in os.listdir( self.getFilesFolder() ):
            airportStr = ""
            full_path = os.path.join(self.getFilesFolder(), file)
            if ( os.path.isfile(full_path) and \
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) and \
                    ( file.endswith (".xlsx") ) ):
                logger.info(" -------- {0} -------- ".format(file))
                if file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) :
                    result = file.split(".")[0]
                    airportStr = result.split(self.fileNameSeparator)[1]
                    yield airportStr

    def checkAirports(self):
        logger.info(" --------checkAirports-------- ")
        ''' pattern is SID or STAR '''
        ''' if SID the a DASH separator followed by an ICAO airport code '''
        for file in os.listdir( self.getFilesFolder() ):
            full_path = os.path.join(self.getFilesFolder(), file)
            if ( os.path.isfile(full_path) and \
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) and \
                     ( file.endswith (".xlsx") ) ):
                logger.info ( file )
                if file.startswith( self.FilesPrefixSID ):
                    logger.info(  self.className + " - file = {0}".format( file ) + " -> is a SID ")
                    result = file.split(".")
                    logger.info(result[0])
                    result = result[0].split(self.fileNameSeparator)
                    logger.info(result) 

                    # airport is second element in array
                    logger.info("departure airport = {0}".format( result[1]) )
                    Adep =  result[1]
                    
                if file.startswith( self.FilesPrefixSTAR ):
                    logger.info(  self.className + " - file = {0}".format( file ) + " -> is a STAR ")

                    result = file.split(".")
                    logger.info(result[0])
                    result = result[0].split(self.fileNameSeparator)
                    logger.info(result) 

                    # airport is second element in array
                    logger.info("arrival airport = {0}".format( result[1]) )
                    # destination airport
                    Ades =  result[1]

    def extractAirportICAOcode( self , fileName ):
        result = fileName.split(".")
        result = result[0]
        arr = result.split(self.fileNameSeparator)
        airportICAOcode = arr[1]
        logger.info ( self.className + " - extract Airport ICAO code - " + airportICAOcode )
        return airportICAOcode

    def extractFirtLastWayPointName ( self , fileName ):
        firstLastWayPointName = ""
        result = fileName.split(".")
        result = result[0]
        arr = result.split(self.fileNameSeparator)
        if fileName.startswith( self.FilesPrefixSID ):
            firstLastWayPointName = arr[3]
        if fileName.startswith( self.FilesPrefixSTAR ):
            firstLastWayPointName = arr[2]
        return firstLastWayPointName

    def extractSidStarRunway ( self , fileName ):
        firstLastWayPointName = ""
        result = fileName.split(".")
        result = result[0]
        arr = result.split(self.fileNameSeparator)
        if fileName.startswith( self.FilesPrefixSID ):
            firstLastWayPointName = arr[2]
        if fileName.startswith( self.FilesPrefixSTAR ):
            firstLastWayPointName = arr[3]
        return firstLastWayPointName

    def loadSidStarInDatabase(self):
        logger.info(" --------load SID STAR model object only (SID STAR waypoints done separately)-------- ")
        ''' pattern is SID or STAR '''
        ''' if SID the a DASH separator followed by an ICAO airport code '''
        for fileName in os.listdir( self.getFilesFolder() ):
            full_path = os.path.join(self.getFilesFolder(), fileName)
            if ( os.path.isfile(full_path) and \
                ( fileName.startswith( self.FilesPrefixSID ) or fileName.startswith( self.FilesPrefixSTAR ) ) and \
                ( fileName.endswith (".xlsx") ) ):
                #logger.info ( self.className + " - " + fileName )

                if fileName.startswith( self.FilesPrefixSID ):
                    airportICAOcode = self.extractAirportICAOcode( fileName )
                    firstLastWayPointName = self.extractFirtLastWayPointName( fileName )
                    runwayStr = self.extractSidStarRunway( fileName )
                    sidStar = SidStarLoaderOne( isSID = True , 
                                                departureOrArrivalAirportICAO = airportICAOcode , 
                                                FirstLastWayPointName = firstLastWayPointName , 
                                                RunWayStr = runwayStr )
                    if (sidStar.exists()):
                        ret = sidStar.load()
                        sidStarDataWayPointDataframe = sidStar.getSidStarDataframe()
                        logger.info ("SID STAR loading result = {0}".format(ret))

                if fileName.startswith( self.FilesPrefixSTAR ):
                    airportICAOcode = self.extractAirportICAOcode( fileName )
                    firstLastWayPointName = self.extractFirtLastWayPointName( fileName )
                    runwayStr = self.extractSidStarRunway( fileName )
                    sidStar = SidStarLoaderOne( isSID = False , 
                                departureOrArrivalAirportICAO = airportICAOcode , 
                                FirstLastWayPointName = firstLastWayPointName , 
                                RunWayStr = runwayStr )
                    if (sidStar.exists()):
                        ret = sidStar.load()
                        sidStarDataWayPointDataframe = sidStar.getSidStarDataframe()
                        logger.info ("SID STAR loading result = {0}".format(ret))

    def writeSidStarWayPoints(self):
        ''' write the SID STAR way points inside the WayPoints.xlsx file '''
        ''' effective writing is done in wayPointsExcelDatabase.writeInExcelWayPointsFile '''
        # TODO  temporary fix - normally fix list should take its input from the AirlineWayPoints django table
        wayPointsExcelDatabase = WayPointsDatabase()
        if wayPointsExcelDatabase.exists():
            ''' if we arrive here , it means that there is an EXCEL WayPoints.xlsx file to load the SID STAR waypoints in '''
            logging.info(self.className + " --- path exists = {0}".format(os.path.exists(self.FilesFolder)))

            for fileName in os.listdir( self.getFilesFolder() ):
                full_path = os.path.join(self.getFilesFolder(), fileName)

                logger.info ( "-------- {0} --------".format(fileName))
                if ( os.path.isfile(full_path) and \
                    ( fileName.startswith( self.FilesPrefixSID ) or fileName.startswith( self.FilesPrefixSTAR ) ) and \
                        ( fileName.endswith (".xlsx") ) ):
                    ''' if we arrive here it means that in the current folder only SID STAR xlsx are filtered '''
                    logger.info ( self.className + " - " + fileName )

                    if fileName.startswith( self.FilesPrefixSID ) or fileName.startswith( self.FilesPrefixSTAR ) :
                        airportICAOcode = self.extractAirportICAOcode( fileName )
                        firstLastWayPointName = self.extractFirtLastWayPointName( fileName )
                        runwayStr = self.extractSidStarRunway( fileName )
                        ''' either a SID or a STAR - isSID is of type boolean '''
                        isSID = fileName.startswith( self.FilesPrefixSID )
                        sidStar = SidStarLoaderOne( isSID = isSID , 
                                    departureOrArrivalAirportICAO = airportICAOcode , 
                                    FirstLastWayPointName = firstLastWayPointName , 
                                    RunWayStr = runwayStr )
                        logger.info( str ( sidStar ) )
                        logger.info(sidStar.__class__.__name__)

                        if (sidStar.exists()):
                            sidStarWayPointDataframe = sidStar.getSidStarDataframe()
                            wayPointsExcelDatabase.writeInXlsxFileSidStarWayPoints( sidStarWayPointDataframe )
