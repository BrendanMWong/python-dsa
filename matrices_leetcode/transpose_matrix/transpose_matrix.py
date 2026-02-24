class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # number of rows and columns in the original matrix
        row_count = len(matrix)
        column_count = len(matrix[0])

        # transpose dimensions are flipped
        # rows = original columns
        # columns = original rows
        output = [[0] * row_count for _ in range(column_count)]

        for row_index in range(row_count):
            for column_index in range(column_count):
                # plug old value into new place, not swapping
                output[column_index][row_index] = matrix[row_index][column_index]

        return output