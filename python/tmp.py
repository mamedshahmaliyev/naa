
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# F(n) = F(n-1) + F(n-2)

from functools import cache, lru_cache

class Fibonacci:
    def __init__(self):
        self.numberOfCalls = 0
        self.memo = {}

    # O(2^n)
    def fib(self, n):
        self.numberOfCalls += 1
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # O(n)
    def fibMemo(self, n):
        self.numberOfCalls += 1
        if n in self.memo:
            return self.memo[n]
        if n == 0 or n == 1:
            return n
        self.memo[n] = self.fibMemo(n-1) + self.fibMemo(n-2)
        return self.memo[n]

    # O(n)
    @cache
    def fibMemo2(self, n):
        self.numberOfCalls += 1
        if n in self.memo:
            return self.memo[n]
        if n == 0 or n == 1:
            return n
        self.memo[n] = self.fibMemo2(n-1) + self.fibMemo2(n-2)
        return self.memo[n]

a = Fibonacci()
b = Fibonacci()
c = Fibonacci()

n = 6

print(a.fib(n), a.numberOfCalls)
print(b.fibMemo(n), b.numberOfCalls)
print(c.fibMemo2(n), c.numberOfCalls)


prev1, prev2 = 0, 1

for i in range(2, n+1):
    prev1, prev2 = prev2, prev1 + prev2
    
print(prev2)