class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for temp_index in range(len(temperatures)):
            while stack != [] and temperatures[stack[-1]] < temperatures[temp_index]:
                popped_index = stack.pop()
                answer[popped_index] = temp_index - popped_index
            stack.append(temp_index)
        return answer