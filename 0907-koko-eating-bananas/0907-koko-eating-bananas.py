def CanEat(piles, k, h):
    total_time = 0
    for pile in piles:
        time = (pile - 1) // k + 1 # 時間=總數/速度
        total_time += time
        if total_time > h:
            return False
    return True

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k：每小時吃香蕉的速度
        # 傳回最小整數 k，使她能夠在 h 小時內吃完所有香蕉 (找最小速度)
        # k = 1 ~ max(piles)
        # h = len(piles) ~ 無限

        slow = 1
        fast = max(piles)

        while slow < fast:
            mid = (slow + fast) // 2
            if CanEat(piles, mid, h) is True:
                fast = mid
            else:
                slow = mid + 1
        return slow



