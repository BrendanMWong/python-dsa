class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # If stack is used as a boolean, it's false if it's empty
        for element in s:
            if stack and element == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and element == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and element == "]" and stack[-1] == "[":
                stack.pop()
            elif element == "(" or element == "{" or element == "[":
                stack.append(element)
            else:
                return False

        # return true if the stack is empty, empty = "not stack"
        return not stack