class Solution:
    def customSortString(self, order: str, s: str) -> str:
        time = defaultdict() # 出現次數

        for char in s:
            time[char] = time.get(char , 0) + 1

        res = ""
        for char in order:
            if char in time:
                res += char * time[char]
                del time[char]
        print(res)
        
        for key , value in time.items():
            res += key * value
        return res
        