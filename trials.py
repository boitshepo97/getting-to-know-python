import re

# need to read line
# account for rows (start and end)
# make a dictionary to contain results

# re.search("/path/to/script.js")

def list_all_js_function_names(pfile):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    with open(pfile) as dataFile:
        data = dataFile.readlines()

        # searched = re.search("function", data)

        for line in data:
            if 'function' in line:
                print ('found')

            else:
                print ('did not find')


# file = "/path/to/script.js"


list_all_js_function_names("script.js")