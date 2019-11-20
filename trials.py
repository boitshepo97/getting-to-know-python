import re



# re.search("/path/to/script.js")

def list_all_js_function_names(pfile):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    with open(pfile) as dataFile:
        data = dataFile.readlines()

        j = 0
        lineNumber = 0
        end_row = 0
        dictFunctions = []

        # searched = re.search("function", data)

        # print(searched[0])
        
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

# file = "/path/to/script.js"


list_all_js_function_names("script.js")