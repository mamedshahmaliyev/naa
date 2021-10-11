
try:
    print(1/0)
except:
    print(1/0)

print("final line")
exit(0)






class NaaException(Exception):
    pass

arr = ['firuza', 'mehrali', 'maryam', 'ahmad', 'ravan', 'zakhra', 'rustam']

try:
    if input("Please enter student name from 1459i:") not in arr:
        raise NaaException
except:
    print("wrong student name")

print('student is from 1459i')
exit(0)



print("Salam")

try:
    print(1/0)
except Exception as e:
    print("Exception happened:", e)
finally: # assures code will be executed whether exception happens or no
    print('sdfasdfdsf')

print("Sagol")