class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # matrix format: output[row][column]
        # prefill the array with n rows and n columns
        output = []
        count = 0
        while count < n:
            row = [0] * n
            output.append(row)
            count += 1

        # num represents the values to be put into the matrix
        num = 1

        # set boundary initial indexes, right and bottom are n - 1 due to 0 indexing
        top, right, bottom, left = 0, n - 1, n - 1, 0

        # repeat until boundaries cross, no squares left to fill
        while top <= bottom and left <= right:
            # right + 1 because right boundary of range() is exclusive
            for column in range(left, right + 1):
                output[top][column] = num
                num += 1
            top += 1
            
            # bottom + 1 because right boundary of range() is exclusive
            for row in range(top, bottom + 1):
                output[row][right] = num
                num += 1
            right -= 1

            # right becuase the left boundary of range() is inclusive
            # left - 1 because the right boundary of range() is exclusive, but going backwards,
            # so left - 1 is used instead of left + 1
            for column in range(right, left - 1, -1):
                output[bottom][column] = num
                num += 1
            bottom -= 1

            # bottom becuase the left boundary of range() is inclusive
            # top - 1 because the right boundary of range() is exclusive, but going backwards,
            # so top - 1 is used instead of top + 1
            for row in range(bottom, top - 1, -1):
                output[row][left] = num
                num += 1
            left += 1
        
        return output