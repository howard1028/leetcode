from collections import Counter
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        h = [(count , num) for num , count in c.items()]
        heapq.heapify(h) # min heap
        # print(h)

        while k > 0:
            count , num = heapq.heappop(h)
            # 最少的夠減
            if k >= count:
                k -= count
            # 不夠的要看減完有沒有剩
            else:
                heapq.heappush(h , (count - k , num))
                break
            
        return len(h)




        # s = dict(sorted(c.items() , key = lambda x:x[1]))
        # # print(dict(s))
        # for i in range(k):
        #     min_key = min(s.items() , key = lambda x:x[1])[0]
        #     # print(min_key)
        #     s[min_key] -= 1
        #     if s[min_key] == 0:
        #         del s[min_key]
        # return len(set(s))