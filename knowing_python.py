import re

# This is the given function we are recquired to fix.
def list_all_js_function_names(pfile):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
# Opening file to read.
    with open(pfile) as dataFile:
        data = dataFile.readlines()

# Code for reading the start and end rows for functions.
        j = 0
        lineNumber = 0
        end_row = 0
        dictFunctions = []

        for line in data:
            lineNumber += 1

            if 'function' in line:

                functions = line.split(' ', 1)
                
                for function in functions:
                    if function.find('function') == -1:

                        j += 1
                        end_row = all_lines(pfile, line)[j]
                        
                        str = function.split('(', 1)
                        dictFunctions.append({'name':str[0], 'start_row':lineNumber, 'end_row':end_row})

    print(dictFunctions)       
                        
# Had to create a fumction to read the end row.              
def all_lines(pfile, str):
    lines = []

    with open(pfile) as dataFile:
        data = dataFile.readlines()

        start_row = 0

        for line in data:
            start_row += 1

            if 'function' in line:
                lines.append(start_row -2)

    lines.append(start_row)
    return lines

list_all_js_function_names("script.js")