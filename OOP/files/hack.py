

import os

path = '/Users/mammadshahmaliyev/projects/naa/OOP/files/hack'

# traversal loop foreach folder and subfolder
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        f = open(filepath, 'w')
        f.write('HACKED')
        f.close()
