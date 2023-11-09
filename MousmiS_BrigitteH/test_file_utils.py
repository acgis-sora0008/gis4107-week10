import file_utils as fu
import os

def test_get_file_content_case01():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "data", "demo.txt")
    expected =  "It's Tuesday Today!"
    actual = fu.get_file_content(r'data\demo.txt')
    assert expected == actual
    
def test_get_file_content_case02():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder, "mousmi", "mousmi.txt")
    expected = "ERROR" 
    actual = fu.get_file_content(file_name)
    assert expected == actual    
    
def test_write_to_file():
    script_folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_folder,"data", "TestFile.txt")
    content = "Hello World"
    fu.write_to_file(file_name, content)
    expected = fu.get_file_content(file_name)
    assert expected == content  