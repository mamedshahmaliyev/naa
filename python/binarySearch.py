
import random, time

# O(n)
def elementExistsInSortedArrayLinear(arrSorted, target):
    for e in arrSorted:
        if target == e:
            return True
    return False

# return True if element exists in array or return False otherwise
def elementExistsInSortedArrayLogarithmic(arrSorted, target):
    start, end = 0, len(arrSorted) - 1

    while start <= end:
        middle = (start + end) // 2
        if arrSorted[middle] == target:
            return True
        elif arrSorted[middle] < target:
            start = middle + 1
        elif arrSorted[middle] > target:
            end = middle - 1
    
    return False

# generate random sorted (strictly increasing) array with 10kk elements
arr = [1]
for _ in range(10**7):
    # in each step take number between the [previous + 1, previous + 100]
    e = random.randint(arr[-1] + 1, arr[-1] + 100)
    arr.append(e)

target = random.randint(arr[0], arr[-1])

# first measure linear time execution
st = time.time()
print(elementExistsInSortedArrayLinear(arr, target))
print("Linear execution time", format(time.time() - st, '.7f'))

# now measure logarithmic time execution
st = time.time()
print(elementExistsInSortedArrayLogarithmic(arr, target))
print("Logarithmic execution time", format(time.time() - st, '.7f'))
    

