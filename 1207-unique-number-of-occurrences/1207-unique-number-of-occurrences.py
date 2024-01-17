class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict() # 紀錄數字出現次數
        count2 = defaultdict() # 出現次數出現的次數
        for num in arr:
            count[num] = count.get(num , 0) + 1
        print(set(count))
        print(count)

        count2 = {value:key for key , value in count.items()}
        return len(count) == len(set(count2))
