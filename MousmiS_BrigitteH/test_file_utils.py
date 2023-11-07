import file_utils as fu
import os
import csv
import data


def test_get_file_content_case01():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "demo.txt")
    expected =  "Its Tuesday Today!"
    actual = fu.get_file_content(r'data\demo.txt')
    assert expected == actual
    
    # test_get_file_content_case01()
    
def test_get_file_content_case02():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "mousmi", "mousmi.txt")
    expected = "ERROR"
    
     
    actual = fu.get_file_content('mousmi.txt')
    
    assert expected == actual    
    
def test_write_to_file():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder,"data", "TestFile.txt")
    content = "Hello World"
    fu.write_to_file(file_name, content)
        