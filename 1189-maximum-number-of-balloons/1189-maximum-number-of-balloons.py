class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        # balloon = {'a':1 , 'b':1 , 'l':2 , 'o':2 , 'n':1}
        count = {}

        # for char in text:
        #     if char not in count:
        #         count[char] = 1
        #     else:
        #         count[char] += 1
        
        for char in text:
            count[char] = count.get(char, 0) + 1
        print(count)

        # 要湊出一個balloon要1b1a1n2l2o
        b = count.get('b' , 0)
        a = count.get('a' , 0)
        n = count.get('n' , 0)
        l = count.get('l' , 0) // 2
        o = count.get('o' , 0) // 2

        return min(a,b,n,l,o)
