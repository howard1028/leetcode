class Solution:

    def validPalindrome(self, s: str) -> bool:

        def judge(s, left, right): # second chance
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True    

        left = 0
        right = len(s) - 1 

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return judge(s, left+1 , right) or judge(s, left, right-1)

        return True
            