class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        res = 0
        max_freq = max(dic.items() , key = lambda d:d[1])[1]
        # print(dic)
        # print(max(dic.items() , key = lambda d:d[1])[1])

        for key , value in dic.items():
            if value == max_freq:
                res += max_freq
        return res
