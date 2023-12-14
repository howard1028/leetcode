import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap sort

        # print(nums)
        heapq.heapify(nums)
        res = []
        print(nums)

        for i in range(len(nums)):
            smallest = heapq.heappop(nums)
            res.append(smallest)

        return res