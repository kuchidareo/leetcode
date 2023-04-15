class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True

        for k in t:
            if s[i] == k:
                i += 1
            if i == len(s):
                return True
        return False

