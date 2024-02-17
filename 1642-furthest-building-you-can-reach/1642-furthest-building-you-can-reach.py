import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        p = []

        for i in range(len(heights) - 1):
            gap = heights[i+1] - heights[i]
            # 平的或向下
            if gap <= 0:
                continue
            
            bricks -= gap
            heapq.heappush(p , -gap) # 加負號：max heap

            # 先用磚塊，再用梯子
            if bricks < 0:
                bricks += -heapq.heappop(p)
                ladders -= 1

            if ladders < 0:
                return i
        return len(heights) - 1
