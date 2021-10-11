



def calculateSumOfOddNumbersUsingWhileLoop2(n: int) -> int:
    s = 0
    a = 0
    while a <= n:
        a += 1
        if a % 2 == 0:
            continue
        s += a
    print("The sum of odd numbers up to {} = {}".format(n, s))

def calculateSumOfOddNumbersUsingWhileLoop(n: int) -> int:
    s = 0
    a = 1
    while a <= n:
        if a % 2 == 1:
            s += a
        # a += 2
        a += 1
    print("The sum of odd numbers up to {} = {}".format(n, s))

def calculateSumOfEvenNumbersUsingForLoop(n: int) -> int:
    s = 0
    for a in range(1, n + 1):
        if a % 2 == 1:
            continue
        s += a
    print("The sum of even numbers up to {} = {}".format(n, s))

def calculateSumUsingForLoop(n: int) -> int:
    s = 0
    for a in range(1, n + 1):
        s = s + a
        # print('a =', a, 's =', s)
    print("The sum of number up to {} is equal to {}".format(n, s))

def calculateSumUsingWhileLoop(n: int) -> int:
    s = 0
    a = 1
    while True:
        s += a # this is the same s = s + a
        a += 1
        # print('a = {}, n = {}'.format(a, n))
        if a > n:
            break
    print("The sum of number up to {} is equal to {}".format(n, s))

def calculateSumConstantTimeWithFormula(n):
    return n * (n + 1) / 2
# n = int(input('input your number: '))
n = 10**8
calculateSumConstantTimeWithFormula(n)
# calculateSumUsingForLoop(n)
# calculateSumUsingWhileLoop(n)
# calculateSumOfEvenNumbersUsingForLoop(n)
# calculateSumOfOddNumbersUsingWhileLoop2(n)
# calculateSumOfOddNumbersUsingWhileLoop(n)

# for i in range(n):
#     for j in range(n):
#         print ('{} * {} = {}'.format(i, j, i * j))

# O(n) - linear complexity 100 operations
# O(n^2) - quadratic complexity =  100*100
# 








