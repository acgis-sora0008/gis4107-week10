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
    
    in_csv = os.path.join(script_folder, r'data\Haiti_Admin_Names.csv')
    out_csv = os.path.join(script_folder, 'haiti_admin_names_fixed.csv')
    
    with open(out_csv, 'w', newline= '') as o:
        writer = csv.writer(o)
        with open(in_csv) as i:
            reader = csv.reader(i)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                admin_code = row[admin_code_column_index]
                index = 4
                new_admin_code = admin_code[0:index] + admin_code[index + 1:]
                row[admin_code_column_index] = new_admin_code
                writer.writerow(row)

def fix_code(admin_code):
    """Returns code with 5th character removed.
    For example, given HT12345-01, return "HT1245-01"""
    index = 4
    new_admin_code = admin_code[0:index] + admin_code[index + 1:]
    return new_admin_code
























