

import os

import logging
logger = logging.getLogger(__name__)

import unittest

import pandas as pd
from SidStarFinderFile import SidStarFinder

#============================================
class Test_Main(unittest.TestCase):

    def test_main_one(self):

        logging.basicConfig(level=logging.INFO)
        logger.info ( "--- read SID STAR files ---")

        sidStarFinder = SidStarFinder()
        sidStarFinder.check()
        logger.info ( sidStarFinder.getFilesFolder())
        logger.info ( sidStarFinder.FilesPrefixSID)
        logger.info ( sidStarFinder.FilesPrefixSTAR)

    def test_main_two(self):
        sidStarFinder = SidStarFinder()
        sidStarFinder.check()
        sidStarFinder.findSidStarExcelFiles()

    def test_main_three(self):
        sidStarFinder = SidStarFinder()
        sidStarFinder.check()
        sidStarFinder.checkAirports()        


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.info("pandas version = " + pd. __version__)
    unittest.main()