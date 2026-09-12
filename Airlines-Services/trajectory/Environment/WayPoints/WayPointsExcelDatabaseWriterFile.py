
'''
Created on 12th September 2026
write SID STAR way points in EXCEL database (temporary bug)
@author: robert

'''

import os
import logging
logger = logging.getLogger(__name__)

import pandas as pd

from trajectory.Guidance.WayPointFile import WayPoint
from trajectory.Guidance.Utils import convertDegreeMinuteSecondToDecimal

fieldNames = ['WayPoint', 'Country' , 'Type', 'Latitude', 'Longitude' , 'Name']

class WayPointsExcelDatabaseWriter(object):
    WayPointsDict = {}
    ColumnNames = []
    className = ''
    
    def __init__(self):
        self.className = self.__class__.__name__
        
        logging.info(self.className + ": ----- WayPoints Excel Database Writer init -----")
        
        self.FileName = 'WayPoints.xlsx'  
        self.FilesFolder = os.path.dirname(__file__)

        logging.info ( self.className + ': file folder= {0}'.format(self.FilesFolder) )
        self.FilePath = os.path.join(self.FilesFolder , self.FileName)
        logging.info ( self.className + ': file path= {0}'.format(self.FilePath) )

        self.sheetName = "WayPoints"

    def exists(self):
        logging.info(self.className + ": path exists = {0}".format(os.path.exists(self.FilesFolder)))
        logging.info(self.className + ": file exists = {0}".format(os.path.isfile(self.FilePath)))
        return os.path.exists(self.FilesFolder) and os.path.isdir(self.FilesFolder) and os.path.isfile(self.FilePath)

    def writeInExcelWayPointsFile(self , sidStarDataframe ):
        assert len(self.FilePath)  >0
        if not sidStarDataframe:
            ''' expecting a pandas dataframe with the content of the SID STAR excel file hence with the waypoints '''
            raise ValueError ( "sidStarDatame = {0} is None ".format( sidStarDataframe ))

        if self.exists() and sidStarDataframe:
            ''' get dataframe of the WayPoints.xlsx file '''
            df_WayPointsXlsxDataframe = pd.DataFrame(pd.read_excel(self.FilePath, sheet_name=self.sheetName , engine="openpyxl"))
            
            for wayPointIndex, wayPointRow in df_WayPointsXlsxDataframe.iterrows():
                logging.info('Index is: {}'.format(wayPointIndex))
                logging.info('ID is: {} - WayPoint is: {} - Latitude = {} - Longitude = {}'.format(wayPointIndex, wayPointRow['WayPoint'], \
                                            wayPointRow['Latitude'], wayPointRow['Longitude']))
                
                wayPointName = str(wayPointRow['WayPoint']).strip().upper()
                logger.info( self.className + " - " + wayPointName)

                for sidStarIndex , sidStarRow in sidStarDataframe:
                    logging.info('SidStar Index is: {}'.format(sidStarIndex))
                    logging.info('ID is: {} - WayPoint is: {} - Latitude = {} - Longitude = {}'.format(sidStarIndex, sidStarRow['WayPoint'], \
                                                                sidStarRow['Latitude'], sidStarRow['Longitude']))



