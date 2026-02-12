# this is dynamic programming problem, DP

# messy version
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            prev_prev_num = 1
            prev_num = 2
            # current_num = prev_prev_num + prev_num
            for num in range(3, n + 1):
                current_num = prev_prev_num + prev_num
                prev_prev_num = prev_num
                prev_num = current_num 
            return current_num

# cleaner version
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1

        # _ is a variable that isn't used
        for _ in range(n - 1):
            prev, curr = curr, prev + curr

        return curr
