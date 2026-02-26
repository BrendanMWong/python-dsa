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
    
# Version written without any help
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        # number of rows is m
        m = len(matrix)
        # number of cols is n
        n = len(matrix[0])
        # init 4 boundaries, are indexes, top starts at 0, right starts at number of columns len(n) - 1
        # bottom starts at number of rows len(m) - 1, left starts at 0
        top, right, bottom, left = 0, n - 1, m - 1, 0

        # keep reading until any boundaries cross
        while top <= bottom and left <= right:
            # read every element in top row and put in output
            # range is from left to right + 1
            for index in range(left, right + 1):
                output.append(matrix[top][index])
            # move top down: top + 1
            top += 1

            # read every element in right col and put in output
            # range is from top to bottom + 1
            for index in range(top, bottom + 1):
                output.append(matrix[index][right])
            # move right to the left: right - 1
            right -= 1
            
            # check if boundary crossed
            if top <= bottom:
                # read every element in bottom row and put in output in reverse order
                # range is right, left - 1, -1
                for index in range(right, left - 1, -1):
                    output.append(matrix[bottom][index])
                # move bottom upwards: bottom - 1
                bottom -= 1

            # check if boundary crossed
            if left <= right:
                # read every element in left col and put in output in reverse order
                # range is bottom, top - 1, -1
                for index in range(bottom, top - 1, -1):
                    output.append(matrix[index][left])
                # move left to the right: left + 1
                left += 1
        return output