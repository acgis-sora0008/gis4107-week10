#-------------------------------------------------------------------------------
# Name:        test_fix_haiti_file.py
#
# Purpose:	   Test functions in fix_haiti_file.py
#
# Author:      David Viljoen
#
# Created:     08/11/2021
#-------------------------------------------------------------------------------

import csv
import fix_haiti_file as fh


def test_fix_code_typical_code():
    """Given HT12345-01, expecting HT1245-01"""


def test_fix_file():
    """"Haiti_Admin_Names.csv contains ADMIN_CODES in the first column
        Haiti_Admin_Names_fixed.csv contains a fixed version. 
		TIP:  expected will be a "fixed" row of data
		      actual will be the row extracted from the fixed file
	"""
	

	## Optional:
    ## Once you have process_file "working", uncomment the 5 lines starting with
    ## file1 = ""
    ## Set kdiffexe to the path to kdiff3.exe on your computer
    ## Set file1 and file2 to the original and fixed eversion of the files
    ## This should provide a nice visual comparison of the file with and
    ## without the fix.  In general, this is not a good practice for testing.
    ## That is, launching an external application to show test results.
    ##
    # file1 = ""
    # file2 = ""
    # kdiffexe = '"C:\Program Files\KDiff3\kdiff3.exe"'
    # cmd = r'{} {} {}'.format(kdiffexe, file1, file2)
    # os.system(cmd)