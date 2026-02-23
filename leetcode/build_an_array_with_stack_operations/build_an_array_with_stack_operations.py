class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        stack_operations = []
        tracked_index = 0
        for num in range(1, n + 1):
            if tracked_index == len(target):
                break
            stack.append(num)
            stack_operations.append("Push")
            if num != target[tracked_index]:
                stack.pop()
                stack_operations.append("Pop")
            else:
                tracked_index += 1
        return stack_operations