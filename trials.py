import re



# re.search("/path/to/script.js")

def list_all_js_function_names(pfile):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    with open(pfile) as dataFile:
        data = dataFile.readlines()

        lineNumber = 0
        dictFunctions = []

        # searched = re.search("function", data)

        # print(searched[0])
        
        for line in data:
            lineNumber += 1

            if 'function' in line:

                functions = line.split(' ', 1)
                
                for function in functions:
                    if function.find('function') == -1:
                        # str = re.sub('[^A-Za-z0-9]+', '', function)
                        str = function.split('(', 1)
                        dictFunctions.append({'name':str[0], 'start_row':lineNumber, 'end_row':lineNumber})

    print(dictFunctions)       
                        
                


# file = "/path/to/script.js"


list_all_js_function_names("script.js")