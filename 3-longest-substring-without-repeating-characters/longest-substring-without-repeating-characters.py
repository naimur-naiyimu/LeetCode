class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i-j+1)
        return res