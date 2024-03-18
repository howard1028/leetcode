class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1]) # 根據結束位置排序
        arrow = 1
        end = points[0][1]
        for start , finish in points:
            if start > end:
                arrow += 1
                end = finish
        return arrow