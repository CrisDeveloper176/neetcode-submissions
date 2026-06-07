class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows    = {i: set() for i in range(9)}
        cols    = {i: set() for i in range(9)}
        squares = {(r,c): set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        
        return True   

