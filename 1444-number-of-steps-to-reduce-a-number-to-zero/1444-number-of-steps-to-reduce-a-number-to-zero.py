class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num != 0:
            if num%2 == 0:
                num/=2
            else:
                num-=1
            count+=1
        return count
    
    #binary=bin(num)[2:]
    #num變二進位:0b...，[2:]從第二個開始取，不要取"0b"