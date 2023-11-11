import fix_haiti_file as fh
import sys
import os
import csv

def fix_file(in_csv, out_csv, admin_code_column_index = 0):
    """Function to fix the input CSV file.

    Args:
        in_csv: input csv file
        out_csv: output csv file
    """
# fix_file function 
    with open(out_csv, 'w', newline= '') as o:
        writer = csv.writer(o)
        with open(in_csv) as i:
            reader = csv.reader(i)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                admin_code = row[admin_code_column_index]
                if len(admin_code) == 10:
                    index = 4
                    new_admin_code = admin_code[0:index] + admin_code[index + 1:]
                    row[admin_code_column_index] = new_admin_code
                    writer.writerow(row)
                else:
                    return 'incorrect admin code entry'

def main():
    """The name flow to fix_haiti_file
    """
    if len(sys.argv) != 3:
        print("Usage: python fix_haiti_file_cli.py in_file fixed_file")
        sys.exit(1)
        
# Get input and output file paths from command line arguments
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
# Check if the input file exists  
    if not os.path.exists(in_file):
        print(f"The input file '{in_file}' does not exist.")
        sys.exit(1)
        
# Call the fix_file function with input and output file paths defined in json file
    fix_file(in_file, out_file)        

if __name__ == '__main__':
    main()