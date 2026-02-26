class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # start at row 1, column 1 because row 0 elements and column 0 elements have no element to the to pleft
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                # compare current element to adjacent top left element
                if matrix[row][col] != matrix[row - 1][col - 1]:
                    return False
        return True
