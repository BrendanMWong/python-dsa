# 99% of this version was written without help
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # n = square length
        n = len(grid)
        output_len = n - 2

        # init size of output matrix
        output = [[0] * output_len for _ in range(output_len)]

        # iterate through each square that isn't an edge square
        for row in range(1, n - 1):
            for col in range(1, n - 1):
                # find max in the 9 squares
                max_val = 0
                for mini_row in range(row - 1, row + 2):
                    for mini_col in range(col - 1, col + 2):
                        if grid[mini_row][mini_col] > max_val:
                            max_val = grid[mini_row][mini_col]
                # put that max in output
                # - 1 because it undos the left by 1 and top by 1 shift, as output doesn't need to avoid edges
                output[row - 1][col - 1] = max_val
        return output
    
# alternate version
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        output = []

        # slide 3x3 window
        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0

                # check the 3x3 block
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        max_val = max(max_val, grid[r][c])

                row.append(max_val)

            output.append(row)

        return output