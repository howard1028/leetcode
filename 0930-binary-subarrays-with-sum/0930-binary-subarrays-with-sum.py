from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 計算prefix sum
        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)
        # print(psum)

        # 計算各種和出現次數
        count = 0
        sum_count = defaultdict(int)
        # psum 中找 psum[i] - psum[j] == goal 的 (psum[i] == goal - psum[j])
        for p in psum:
            count += sum_count[p]
            sum_count[p + goal] += 1
        # print(sum_count)
        return count