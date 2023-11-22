def CanShip(weights, days, w):
    total_weight = w # w：最大承重能力
    least_days = 0
    for weight in weights:
        # 該趟載不下了
        if total_weight + weight > w:
            least_days += 1
            total_weight = 0
        total_weight += weight
    if least_days > days:
        return False
    else:
        return True

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # 找最小承受重量
        lo = max(weights)
        # hi = 0
        # for weight in weights:
        #     hi += weight
        hi = sum(weights)
        min_capacity = hi # 目前最小承受重量

        print(hi,'\n')

        while lo <= hi: 
            mid = lo + (hi - lo) // 2 
            if CanShip(weights, days, mid):
                hi = mid - 1
                min_capacity = mid
            else:
                lo = mid + 1
            print(mid)
        return min_capacity
