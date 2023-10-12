class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)] # 每個set代表每個rows
        columns = [set() for _ in range(9)] # 每個set代表每個columns
        boxes = [set() for _ in range(9)] # 每個set代表每個3x3 box，從左上到右下

        # row major
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.' and (num in rows[i] or num in columns[j] or num in boxes[(i//3)*3 + (j//3)]):
                    return False
                rows[i].add(num)
                columns[j].add(num)
                boxes[(i//3)*3 + (j//3)].add(num)
        return True
    
    
    