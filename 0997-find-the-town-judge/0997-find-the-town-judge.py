from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        # trust_count紀錄信任幾個人
        # trusted_count紀錄被幾個人信任
        trust_count = defaultdict()
        trusted_count = defaultdict()
        
        for [ai , bi] in trust:
            trust_count[ai] = trust_count.get(ai , 0) + 1
            trusted_count[bi] = trusted_count.get(bi , 0) + 1

        # print(trust_count)
        # print(trusted_count)
        for ted , t in trusted_count.items():
            if trusted_count[ted] == n-1:
                if trust_count.get(ted) is None:
                    return ted
        return -1
        
