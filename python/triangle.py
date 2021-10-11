
# height of the triangle
numberOfLines = int(input("Enter the height of the triangle: "))

for i in range(1, numberOfLines + 1):
   
   # you can obtain below formulas by checking the pattern of the triangle
   # and counting number of spaces and asterisks in each line
   numberOfSpaces = numberOfLines - i
   numberOfAsterisks = 2 * i - 1
   
   print(' ' * numberOfSpaces + '*' * numberOfAsterisks)
    