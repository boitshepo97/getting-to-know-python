import pytest
from knowing_python import list_all_js_function_names

def test_list_all_js_function_names():
    #For all script.js, 
    # we would like to know all functions within the file.
    list_all_js_function_names("script.js")