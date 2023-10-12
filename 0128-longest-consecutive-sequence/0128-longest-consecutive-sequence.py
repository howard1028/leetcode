import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        heap = []
        for i in nums:
            heapq.heappush(heap,i)

        print(heap)

        count = 1
        max_length = 1
        
        if len(heap) > 0:
            first = heapq.heappop(heap)

            while len(heap) > 0:
                second = heapq.heappop(heap)
                if second == first + 1:
                    count += 1
                elif second == first:
                    pass
                else:
                    count = 1
                if count > max_length:
                    max_length = count
                first = second
        else:
            max_length = 0
        return max_length