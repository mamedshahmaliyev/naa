
# wordsArr = ['abc', 'a', 'abdefg']

# time complexity - O( (number of the words) X (length of the shortest word))
# space complexity - O(length of the shortest word)
def longestCommonPrefix(wordsArr): # we assume that there is at least one word in wordArr
    prefix = ''
    i = -1
    while True:
        i += 1
        for word in wordsArr:
            if len(word) < i + 1 or word[i] != wordsArr[0][i]:
                return prefix
        prefix += wordsArr[0][i]

print(longestCommonPrefix(['abc', 'a', 'ab', 'cde']))
print(longestCommonPrefix(['abc', 'a', 'ab']))
print(longestCommonPrefix(['abc', 'ab', 'ab']))


    


    
         