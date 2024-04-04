class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        res = 0
        for char in s:
            if char == '(':
                m += 1
                res = max(res , m)
            elif char == ')':
                m -= 1
            else:
                pass
        return res