class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)
        res = []
        n = len(nums)
        
        for i in range(n):
            h[i+1] = 1
        # print(h)

        for i in range(n):
            h[nums[i]] -= 1
        # print(h)

        for key , value in h.items():
            # 重複出現
            if h[key] < 0:
                res.append(key)

        for key , value in h.items():                
            # 未出現
            if h[key] > 0:
                res.append(key)

        # print(res)

        return res