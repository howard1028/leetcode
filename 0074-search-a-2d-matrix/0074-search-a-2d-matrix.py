class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 把全部看成1D array
        m = len(matrix) 
        n = len(matrix[0])
        left = 0
        right = m*n - 1

        while left <= right:
            # 找midian of midians
            mid = (left + right) // 2
            row , column = divmod(mid , n)
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
