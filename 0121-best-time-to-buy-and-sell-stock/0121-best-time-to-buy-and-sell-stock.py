class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            # price下降，更新min price
            if prices[i] < min_price:
                min_price = prices[i]
            # price沒下降，算最大利潤
            else:
                current_profit = prices[i] - min_price
                max_profit = max(max_profit,current_profit)
                
        return max_profit