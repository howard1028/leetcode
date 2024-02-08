from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = sorted(Counter(s).items() , key = lambda d:d[1] , reverse = True)
        return ''.join(char * count for char , count in c)
