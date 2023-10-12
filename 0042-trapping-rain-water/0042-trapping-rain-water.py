class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        if n <= 2:
            return 0
        
        # 紀錄每一點左邊高度最大值
        left_max = [0] * n 
        left_max[0] = height[0]
        
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])  
                
        # 紀錄每一點右邊高度最大值        
        right_max = [0] * n
        right_max[n-1] = height[n-1]
        
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i],right_max[i+1])
        
        # 計算水量
        total_water = 0
        for i in range(n):
            current_water = min(left_max[i],right_max[i]) - height[i]
            total_water += current_water
        
        return total_water