class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i] == [x[j] for x in grid]:
                    # print(grid[i],[x[j] for x in grid])
                    count += 1
        return count