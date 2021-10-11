
# arr = [1, 2, 3], target = 3 => [0, 1]
# Time complexity is O(n^2), space complexity - O(1)
def twoSumIndicesQuadratic(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
            

# Time complexity is O(n)
def twoSumIndices(arr, target):
    elementIndex = {}
    for i in range(len(arr)):
        a = arr[i]
        b = target - a # a + b = target, b = target - a

        if b in elementIndex:
            return elementIndex[b], i
    
        elementIndex[a] = i
        
print(twoSumIndices([1, 3, 2], 3))
print(twoSumIndices([1, 1, 2], 2))
print(twoSumIndices([4, 0, 1, 2], 2))