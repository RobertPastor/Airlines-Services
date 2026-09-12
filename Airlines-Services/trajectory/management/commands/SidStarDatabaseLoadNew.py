
'''
Created on 11th September 2026

@author: robert
'''

import os

import logging
logger = logging.getLogger(__name__)


import pandas as pd
from trajectory.management.commands.SidStar.SidStarFinderFile import SidStarFinder
from trajectory.management.commands.SidStar.SidStarDatabaseLoader import SidStarLoaderOne

from django.core.management.base import BaseCommand
from trajectory.management.commands.SidStar.SidStarDatabaseLoader import SidStarLoaderOne

from trajectory.models import  AirlineAirport

class Command(BaseCommand):
    help = 'Reads the SID STAR waypoints and write them a Django table'
    def handle(self, *args, **options):

        logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)

        logger.info ( "--- manage SID STAR new generation ---")

        logging.basicConfig(level=logging.INFO)
        logger.info ( "--- read SID STAR files ---")
        
        sidStarFinder = SidStarFinder()
        sidStarFinder.check()
        logger.info ( sidStarFinder.getFilesFolder())
        logger.info ( sidStarFinder.FilesPrefixSID)
        logger.info ( sidStarFinder.FilesPrefixSTAR)

        sidStarFinder.findSidStarExcelFiles()
        sidStarFinder.checkAirports()

        for airportCode in sidStarFinder.getAirports():
            logger.info( str(airportCode).upper() )
            airportCode = str(airportCode).upper()

            airport = AirlineAirport.objects.filter(AirportICAOcode = airportCode).first()
            logger.info( airport )

        sidStarFinder.loadSidStarInDatabase()
        sidStarFinder.writeSidStarWayPoints()
