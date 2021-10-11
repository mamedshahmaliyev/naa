# https://leetcode.com/problems/two-sum/


# linear time O(n), linear space O(n)
def targetSumExists1(arr, target):
    n = len(arr)

    arrSet = set()
    for n in arr:
        arrSet.add(n)

    for n in arr:
        if target - n in arrSet:
            return True
    
    return False

# quadratic time O(n^2), constant space O(1)
def targetSumExists2(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i] + arr[j] == target:
                    return True

    return False

print(targetSumExists1([1,2,3], 5))
print(targetSumExists2([1,2,3], 5))


    


    





    


    

