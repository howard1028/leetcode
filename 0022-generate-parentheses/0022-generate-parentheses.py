class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # left:左括號數，right:右括號數，用dfs做recursive
        def dfs(left,right,string):
            if left + right == 2*n:
                result.append(string)
                return 
            if left < n: # 左括號還不到一半，則(+1
                dfs(left+1,right,string+'(')
            if left > right: # 左括號比右括號多，則)+1
                dfs(left,right+1,string+')')

        result = []
        dfs(0,0,'')
        return result