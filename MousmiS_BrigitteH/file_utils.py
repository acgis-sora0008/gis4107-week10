def get_file_content(file_name):
    try:
        # file_name = r"data\demo.txt"
        with open (file_name) as infile:
            contents = infile.read()
            # print(contents)
        return contents
    except FileNotFoundError:
        return "ERROR"
        


    
    