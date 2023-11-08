def get_file_content(file_name):
    try:
        # file_name = r"data\demo.txt"
        with open (file_name) as infile:
            contents = infile.read()
            # print(contents)
        return contents
    except FileNotFoundError:
        return "ERROR"
        
def write_to_file(file_name, content):
    """This function will not return anything

    Args:
        file_name (string): _description_
        content (string): _description_
        
    """
    file_name = r"data\TestFile.txt"
    with open (file_name,'w') as outfile:
        outfile.write("Hello World")
 