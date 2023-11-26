class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            res = [[1],[1,1]] # 最終要返回的
            for numRow in range(numRows-2):
                new = [1] # 每次要添加的
                for i in range(len(res[-1])-1):
                    new.append(res[-1][i] + res[-1][i+1])
                new.append(1)
                res.append(new)
            return res
            