# 99% of this brute force version written without help
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # matrix row length
        m = len(matrix)
        # matrix col length
        n = len(matrix[0])
        # shortest matrix side
        short_s = min(m, n)
        # longest matrix side
        long_s = max(m, n)

        # keep track of number of submatrices of 1's
        total = 0

        # the max length of the largest possible square of 1's is the shortest side of the matrix
        # the min length of the largest possible square of 1's is 1
        for square_len in range(1, short_s + 1):
            for row in range(0, m - square_len + 1):
                for col in range(0, n - square_len + 1):
                    # keep track of if square is all 1's
                    is_ones = True
                    for mini_row in range(row, row + square_len):
                        for mini_col in range(col, col + square_len):
                            if matrix[mini_row][mini_col] != 1:
                                is_ones = False
                                break
                        if not is_ones:
                            break
                    if is_ones:
                        total += 1
        
        return total
    
# dynamic programming version
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get dimensions of the matrix
        n = len(matrix)    # number of rows
        m = len(matrix[0]) # number of columns
        
        # Create a DP table with same dimensions as matrix
        dp = [[0] * m for _ in range(n)]
        
        # Variable to store total count of squares
        ans = 0
        
        # Initialize first column of DP table
        for i in range(n):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]
        
        # Initialize first row of DP table
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]
        
        # Fill the DP table for remaining cells
        for i in range(1, n):
            for j in range(1, m):
                # Only process if current cell in matrix is 1
                if matrix[i][j] == 1:
                    # Find minimum of left, top, and diagonal cells and add 1
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                ans += dp[i][j]
        
        return ans
