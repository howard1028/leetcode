class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True

        num = []
        while x >= 1:
            # print(x ,int(x % 10))
            num.append(int(x % 10))
            x /= 10
        # print(num)

        if num == num[::-1]:
            return True