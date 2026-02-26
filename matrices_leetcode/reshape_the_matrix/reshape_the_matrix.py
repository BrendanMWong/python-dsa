class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # length of input row
        m = len(mat)
        # length of input column
        n = len(mat[0])

        # check for compatibility right away
        if m * n != r * c:
            return mat
        
        # init the output array
        output = [[0] * c for _ in range(r)]
        
        # track the current row and column of output
        out_row = 0
        out_column = 0

        # populate output with values from mat
        for in_row in range(m):
            for in_column in range(n):
                output[out_row][out_column] = mat[in_row][in_column]
                out_column += 1
                # if output row is finished, move onto the next output row
                if out_column >= c:
                    out_column = 0
                    out_row += 1

        return output