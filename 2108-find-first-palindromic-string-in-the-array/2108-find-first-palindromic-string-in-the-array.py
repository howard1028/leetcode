class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def checkPalindrome(string):
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        for s in words:
            if checkPalindrome(s):
                return s
        return ""
