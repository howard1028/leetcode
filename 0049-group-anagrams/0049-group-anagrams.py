class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord("a")] += 1
            dict[tuple(count)].append(string) #list轉成tuple才能當index
        return dict.values()