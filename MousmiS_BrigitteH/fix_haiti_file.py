#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
#
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     09/11/2021
#-------------------------------------------------------------------------------

import csv
import os


def fix_file(in_csv, out_csv, admin_code_column_index = 0):
    """in_csv = file where a column contains a admin_code that needs fixing.
                That is, the 5th character in admin_code needs to be removed.
       out_csv = file with same contents as in_csv with fixed admin_code
       admin_code_column_index = 0-based index of column containing the
                                 admin_code
    """
    script_folder = os.path.dirname(os.path.abspath(__file__))
    in_csv = os.path.join(script_folder, 'Haiti_Admin_Names.csv')
    with open(in_csv) as f:
        reader  =csv.reader(f)
        header = next(reader)
        for row in reader:
            print(row[0])

    

def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""

























