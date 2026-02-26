class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # m = number of rows
        m = len(mat)
        # n = number of columns = number of elements in a row
        n = len(mat[0])
        
        output = []

        # biggest possible row + column sum is (m - 1) + (n - 1)
        # - 1 for both m and n due to 0 based indexing
        # this is the sum for the bottommost rightmost element
        max_sum = (m - 1) + (n - 1)

        # tracker for row + column = d_sum
        # + 1 because range() is right exclusive
        for d_sum in range(max_sum + 1):
            if d_sum < n:
                row = 0
                column = d_sum
            else:
                row = d_sum - n + 1
                column = n - 1

            temp = []

            while row < m and column >= 0:
                temp.append(mat[row][column])
                row += 1
                column -= 1
                        
            if d_sum % 2 == 0:
                # even sum diagonals are not reversed
                # appending lists requires extend()
                output.extend(reversed(temp))
            else:
                # odd sum diagonals are reversed
                output.extend(temp)

        return output