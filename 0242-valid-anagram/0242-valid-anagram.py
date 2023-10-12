class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        while len(s) > 0:
            # 長度不同
            if len(s) != len(t):
                return False
            
            # 有沒有的字
            f = t.find(s[0])
            if f == -1 :
                return False
            
            word = s[0]
            s = s.replace(word,"",1)
            t = t.replace(word,"",1)
        
        return True