class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s為空則一定是subsequence
        if len(s) == 0:
            return True

        sp = 0 # s的pointer
        for char in t:
            if sp == len(s):
                return True
            if char == s[sp]:
                sp += 1
                
        if sp == len(s):
            return True
        else:
            return False