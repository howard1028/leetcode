class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        count = {0:1} # 初始化，存sub sum出現幾次

        for i in nums:
            prefix_sum += i

            # prefix_sum - k 為 sub sum，則計算有幾個
            if prefix_sum - k in count: # 每個 prefix sum 輪流檢查
                res += count[prefix_sum - k]

            # prefix_sum 為 sub sum，則更新
            if prefix_sum in count:
                count[prefix_sum] += 1
            else:
                count[prefix_sum] = 1
        return res