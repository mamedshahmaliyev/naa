

# this script will draw T with * symbol of given width and height
w = int(input("Please enter width: "))
h = int(input("Please enter height: "))

# make sure that w is odd number for symmetry
if w % 2 == 0:
    w += 1

for i in range(h):
    # print head of T for first line
    if i == 0:
        j = 0
        while j < w:
            print("*", end='')
            j += 1
    else:
        j = 0
        while j < h/2:
            print(' ',end='')
            j += 1
        print("*", end='')
    print("")