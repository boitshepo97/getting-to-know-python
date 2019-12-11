import pytest
from knowing_python import list_all_js_function_names

def test_list_all_js_function_names():
    #For all script.js, 
    # we would like to know all functions within the file.
    result = list_all_js_function_names("script.js")
    assert result == [{'name': 'promptUser', 'start_row': 7, 'end_row': 13}, {'name': 'Array.prototype.memory_card_shuffle', 'start_row': 15, 'end_row': 23}, {'name': 'newBoard', 'start_row': 25, 'end_row': 35}, {'name': 'memoryFlipCard', 'start_row': 37, 'end_row': 62}, {'name': 'flip2Back', 'start_row': 64, 'end_row': 80}]