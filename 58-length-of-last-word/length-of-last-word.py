class Solution:
    def lengthOfLastWord(self, s):
        array = s.strip().split(' ')
        
        if (len(array) > 0):
            return len(array[len(array) - 1])
        else:
            return -1