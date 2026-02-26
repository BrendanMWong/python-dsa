class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # number of rows in board
        m = len(board)
        # number of cols in board
        n = len(board[0])
        # init a reusable set
        s = set()
        # scan every row one by one
        for row in range(m):
            # look at every element in one row
            for num in board[row]:
                if num != ".":
                    if num in s:
                        return False
                    s.add(num)
            s.clear()
        # scan every col one by one
        for col in range(n):
            for row in range(m):
                num = board[row][col]
                if num != ".":
                    if num in s:
                        return False
                    s.add(num)
            s.clear()
        # for all 9 center squares
        for row_index in range(1, m, 3):
            for col_index in range(1, n, 3):
                # for every adjacent + center square
                for row_adj in range(-1, 2):
                    for col_adj in range(-1, 2):
                        # if the value is already in set
                        val = board[row_index + row_adj][col_index + col_adj]
                        if val != ".":
                            if val in s:
                                return False
                            s.add(val)
                s.clear()
        return True