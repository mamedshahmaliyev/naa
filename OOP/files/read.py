import os

if os.path.exists('a.txt'):
    f = open('a.txt', 'r')

    print(f.read(7))
    
    f.close()
else:
    print('a.txt does not exist!')