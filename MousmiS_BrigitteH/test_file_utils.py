import file_utils
import os
import csv


def test_get_file_content_case01():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "demo.txt")
    expected =  "Its Tuesday Today!"
    
     
    actual = file_utils.get_file_content(file_name)
    
    assert expected == actual
    
    
def test_get_file_content_case02():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "mousmi", "mousmi.txt")
    expected = None
    
     
    actual = file_utils.get_file_content(file_name)
    
    assert expected == actual    