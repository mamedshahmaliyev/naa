
import os

search = 'stdio'
path = '/Users/mammadshahmaliyev/projects/naa'

# traversal loop foreach folder and subfolder
for dirpath, dirnames, filenames in os.walk(path):
    if '/.' in dirpath: continue

    # traverse each file in the given folder
    for filename in filenames:

        # check if filename has .c extension
        if ''.join(filename[-2:]) == '.c':
            # get the full file path
            filepath = os.path.join(dirpath, filename)

            # open file for reading
            f = open(filepath, 'r')
            
            # for each line check if search is contained
            line = f.readline()
            while line:
                if search in line:
                    print(filepath)
                line = f.readline()

            f.close()
        
