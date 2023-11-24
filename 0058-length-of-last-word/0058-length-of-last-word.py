class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                count += 1
            elif s[i] == ' ' and count == 0:
                pass
            else:
                return count
        # 沒有空格
        return count