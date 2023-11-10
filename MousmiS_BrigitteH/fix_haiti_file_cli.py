import sys
import os

import fix_haiti_file as fh


def fix_file(in_csv, out_csv):
    """Function to fix the input CSV file.

    Args:
        in_csv (_type_): _description_
        out_csv (_type_): _description_
    """
    pass


def main():
    """The name flow to fix_haiti_file
    """
    if len(sys.argv) != 3:
        print("Usage: python fix_haiti_file_cli.py in_file fixed_file")
        sys.exit(1)
        
# Get input and output file paths from commanf line arguements
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
    
# Check if the input file exists  
    if not os.path.exists(in_file):
        print(f"The input file '{in_file}' does not exist.")
        sys.exit(1)
        
        # Call the fix_file function with input and output file paths
    fix_file(in_file, out_file)        

if __name__ == '__main__':
    main()