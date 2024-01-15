from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans2 = defaultdict() # 紀錄輸過幾次

        unique_numbers = set() # 全部出現的數字
        lose = set() # 輸過
        lose_once = set()

        for match in matches:
            unique_numbers.update(match)
            lose.update([match[1]])
            ans2[match[1]] = ans2.get(match[1], 0) + 1

        print(ans2)
        for i in ans2:
            if ans2[i] == 1:
                lose_once.add(i)

        print(lose_once)
        return [list(sorted(unique_numbers-lose)) , list(sorted(lose_once))]
        