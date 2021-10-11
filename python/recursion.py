# sum of natural numbers up to n
def sum_rec(n): # TC - O(n), SC - O(n) because of recursion call stack
    if n < 1:
        print("Error: Only natural numbers")
        return None
    if n == 1:
        return n
    return n + sum_rec(n-1)

print('sum_rec', sum_rec(5), sum_rec(1), sum_rec(0)) # 1 + 2 + 3 + 4 + 5

def sum_loop(n): # TC - O(n), SC - O(1)
    s = 0
    for i in range(n+1):
        s += i
    return s

print('sum_loop', sum_loop(5), sum_loop(1), sum_loop(0)) # 1 + 2 + 3 + 4 + 5

# fact(n) = n * fact(n-1) 
def fact_rec(n): # TC - O(n), SC - O(n) because of recursion call stack
    if n == 1:
        return n
    return n * fact_rec(n-1)

print('fact_rec', fact_rec(5))

def fact_loop(n): # TC - O(n), SC - O(1)
    s = i = 1
    while i <= n:
        s = s * i
        i += 1
    return s

print('fact_rec', fact_loop(5))


# fib(n) = fib(n-1) + fib(n-2), n >= 0, Fibonachi sequence: 0, 1, 1, 2, 3, 5, 8, 13,...
def fib_rec(n): # TC - O(2^n), SC - O(1) excluding recursion call stack, try to calculate SC at home including recursion call stack
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)
print('fib_rec_memo', fib_rec(5), fib_rec(6))

memo = [None for _ in range(101)] # we use 100 here for simplicity
def fib_rec_memo(n): # TC - O(n), SC - O(n) excluding recursion call stack

    # base case
    if n <= 1:
        return n
    
    if memo[n] is None:
        memo[n] = fib_rec_memo(n-1) + fib_rec_memo(n-2)

    return memo[n]

print('fib_rec_memo', fib_rec_memo(5), fib_rec_memo(6), fib_rec_memo(100)) # fib_rec(100) does not work


import functools

@functools.cache # this decorator is for auto memoization
def fib_rec_memo_pythonic(n): # TC - O(n), SC - O(n) excluding recursion call stack

    # base case
    if n <= 1:
        return n
    
    return fib_rec_memo_pythonic(n-1) + fib_rec_memo_pythonic(n-2)

print('fib_rec_memo_pythonic', fib_rec_memo_pythonic(5), fib_rec_memo_pythonic(6), fib_rec_memo_pythonic(100)) # fib_rec(100) does not work


def fib_loop_memo(n): # TC - O(n), SC - O(n)

    memo = [0 for _ in range(n+1)]
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

print('fib_loop_memo', fib_loop_memo(5), fib_loop_memo(6), fib_loop_memo(100))


def fib_loop(n): # TC - O(n), SC - O(1)
    a, b, c = 0, 1, 1

    for _ in range(n-1):
        c = a + b
        a, b = b, c
    
    return c

print('fib_loop', fib_loop(5), fib_loop(6), fib_loop(100))


import math
def fib_formula(n): # TC - O(log(n)), SC - O(1)
    phi = ( 1 + math.sqrt(5) ) / 2

    return round((math.pow(phi, n) - math.pow(1 - phi, n)) / math.sqrt(5))

print('fib_formula', fib_formula(5), fib_formula(6), fib_formula(100))



