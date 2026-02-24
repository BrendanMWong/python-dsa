class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1: flip the matrix vertically
        # step 2: transpose the matrix by its diagonal (top left to bottom right)

        # row length = len(matrix)
        # column length = len(matrix[0])
        n = len(matrix)

        # flip the matrix vertically
        # the operation "//" will automatically ignore the middle row
        for top_row in range(n // 2):
            # n - 1 due to 0 based indexing
            bottom_row = n - 1 - top_row
            matrix[top_row], matrix[bottom_row] = matrix[bottom_row], matrix[top_row]
        
        # transpose across the main diagonal
        # swap elements (row, column) with (column, row) for the upper triangle only
        for row in range(n):
            # only traverse elements above the diagonal to avoid double swapping
            # row + 1 to avoid the places on the diagonal
            for column in range(row + 1, n):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]



# alternate version with .reverse()

n = len(matrix)

# vertical flip
matrix.reverse()

# transpose
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]