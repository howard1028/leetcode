class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        total = len(haystack)
        window = len(needle)

        for i in range(total - window + 1):
            if haystack[i:i+window] == needle:
                return i
        return -1