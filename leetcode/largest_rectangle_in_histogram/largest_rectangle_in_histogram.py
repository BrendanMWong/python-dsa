class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for current_index in range(len(heights)):
            while stack != [] and heights[current_index] < heights[stack[-1]]:
                popped_index = stack.pop()
                # computed_max = right boundary - left boundary - 1 (width) * height of shortest bar
                if stack != []:
                    left_boundary = stack[-1]
                else:
                    left_boundary = -1
                right_boundary = current_index
                computed_max = (right_boundary - left_boundary - 1) * heights[popped_index]
                max_area = max(max_area, computed_max)
            stack.append(current_index)
        while stack != []:
            popped_index = stack.pop()
            # computed_max = right boundary - left boundary - 1 (width) * height of shortest bar
            if stack != []:
                left_boundary = stack[-1]
            else:
                left_boundary = -1
            right_boundary = len(heights)
            computed_max = (right_boundary - left_boundary - 1) * heights[popped_index]
            max_area = max(max_area, computed_max)
        return max_area