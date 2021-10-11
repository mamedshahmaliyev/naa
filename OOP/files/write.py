import os, sys

# first open the file and assign handle to the variables
# modes w - write, r - read, a - append
f = open('a.txt', 'a')

# second write some data to the file using handle variable
# because w mode is used the file content will be overriden
f.write("\nSalam NAA")

# finally close the handle
f.close()



