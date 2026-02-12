class Solution:
    def mySqrt(self, x: int) -> int:        
        left = 0
        right = x
        middle = right // 2

        while left <= right:
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                right = middle - 1
            else:
                left = middle + 1
            middle = left + (right - left) // 2
        
        # Return right because it's the largest integer whose square is <= x
        return right