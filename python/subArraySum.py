# find if there 3 consecutive elements the sum of which is less than target
# Time complexity O(n^2), Space complexity O(1)
def subArraySumLessThanQuadratic(arr, numberOfConsecutiveElements, target):
    for i in range(0, len(arr) - numberOfConsecutiveElements):

        # we declare a variable to save the sum
        s = arr[i]
        for j in range(i + 1, i + numberOfConsecutiveElements):
            s += arr[j]

        if s < target:
            return True
    return False

# Linear time complexity - O(n), Space complexity - O(1)
def subArraySumLessThanLinear(arr, numberOfConsecutiveElements, target):
    s = 0
    for i in range(len(arr)):
        s += arr[i]

        if i >= numberOfConsecutiveElements:
            s -= arr[i - numberOfConsecutiveElements]
        
        if i >= numberOfConsecutiveElements - 1:
            if s < target:
                return True
        
    return False

arr = [1, 2, 5, 8, 2, 22, 35, 4]
numberOfConsecutiveElements = 3

print(subArraySumLessThanLinear(arr, numberOfConsecutiveElements, 8))
print(subArraySumLessThanLinear(arr, numberOfConsecutiveElements, 9))


        


        