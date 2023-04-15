class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            k = s[i]
            
            other_s = s[:i] + s[i+1:]
            if k not in other_s:
                return i
        return -1
