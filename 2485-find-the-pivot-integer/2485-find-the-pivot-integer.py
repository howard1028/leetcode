class Solution:
    def pivotInteger(self, n: int) -> int:
        psum = [0]
        for i in range(1 , n+1):
            psum.append(psum[-1] + i)
        print(psum)
        
        for i in range(1 , n+1):
            if psum[-1] - psum[i-1] == psum[i]:
                return i
        return -1