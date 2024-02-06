from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]
        else:
            res = []
            dic = defaultdict(list)
            for string in strs:
                s = ''.join(sorted(string)) # 字串排序好當key
                dic[s].append(string)
                # print(dic)
            dic = sorted(dic.items(), key=lambda d: d[0])
            for key, value in dic:
                res.append(value)
            return res