class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        temp = ""  # 目前相同的字元

        while l < r:
            if s[l] == s[r]:
                temp = s[l]
                l += 1
                r -= 1
            elif s[l] == temp and s[r] != temp:
                l += 1
            elif s[l] != temp and s[r] == temp:
                r -= 1
            else:
                break
            # print(temp , s[l:r+1])

        if s[l:r+1] == temp:
            return 0
        return r - l + 1