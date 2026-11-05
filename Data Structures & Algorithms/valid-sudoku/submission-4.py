class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range (9):
            for col in range (9):
                curr = board[row][col]
                if (curr != "."):
                    if (curr in rows[row] or curr in cols[col] or curr in squares[row // 3, col // 3]):
                        return False
                    rows[row].add(curr)
                    cols[col].add(curr)
                    squares[row // 3, col // 3].add(curr)
        return True