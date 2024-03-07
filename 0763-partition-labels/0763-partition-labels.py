from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        dic = defaultdict(int)
        res = []

        # 紀錄最後出現位子
        for i in range(len(s)):
            dic[s[i]] = i
        
        start = 0
        end = dic[s[start]]

        for i in range(len(s)):
            if i > end:
                res.append(end - start + 1)
                start = i
            end = max(end , dic[s[i]])
        # 最後一次
        res.append(end - start + 1)
        return res

