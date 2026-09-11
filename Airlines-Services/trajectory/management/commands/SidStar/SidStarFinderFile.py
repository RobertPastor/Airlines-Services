

'''
Created on 11 September 2026

@author: robert
class dedicated to find SID STAR EXCEL xlsx files

'''

import os
import logging
logger = logging.getLogger(__name__)

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

    # loop through the files in the folder
    def findSidStarExcelFiles(self):
        logger.info(" --------findSidStarExcelFiles-------- ")
        for file in os.listdir( self.getFilesFolder() ):
            full_path = os.path.join(self.getFilesFolder(), file)
            if ( os.path.isfile(full_path) and \
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) ):
                logger.info ( self.className + str(file) )

    def getAirports(self):
        logger.info(" --------getAirports-------- ")
        for file in os.listdir( self.getFilesFolder() ):
            airportStr = ""
            full_path = os.path.join(self.getFilesFolder(), file)
            if ( os.path.isfile(full_path) and \
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) ):
                logger.info ( file )
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
                ( file.startswith( self.FilesPrefixSID ) or file.startswith( self.FilesPrefixSTAR ) ) ):
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