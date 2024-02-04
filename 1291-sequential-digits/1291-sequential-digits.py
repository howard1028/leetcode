class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num = "123456789"
        res = []

        # i:sliding window左界，j:右界
        for i in range(len(num)):
            for j in range(i+1 , len(num)+1 , 1):
                curr = int(num[i:j])
                if low <= curr and curr <= high:
                    res.append(curr)
        res.sort()
        return res