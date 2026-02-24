class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # List[List[int]] = matrix[row][column]
        output = []

        # boundaries
        # when top boundary goes down, it starts at 0 and it increases
        # when right boundary goes left, it starts at len(matrix[0]) - 1 and it decreases
        # when bottom boundary goes up, it starts at len(matrix) - 1 and it decreases
        # when left boundary goes right, it starts at 0 and increases
        top, right, bottom, left = 0, len(matrix[0]) - 1, len(matrix) - 1, 0

        while top <= bottom and left <= right:
            # the first vertical and horizontal boundary change don't need guardrails because the loop condition 
            # guarantees at least one valid row and one valid column at the start of the iteration

            # to include right: use right + 1 because range excludes stop
            for column in range(left, right + 1):
                output.append(matrix[top][column])
            top += 1

            # to include bottom: use bottom + 1 because range excludes stop
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1

            # stepping is -1 to go backwards 
            # to include left: stop at left - 1 marked, the equivalent of + 1 for other direction
            if top <= bottom:
                for column in range(right, left - 1, -1):
                    output.append(matrix[bottom][column])
                bottom -= 1

            # stepping is -1 to go backwards 
            # to include top: stop at top - 1 marked, the equivalent of + 1 for other direction
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1

        return output