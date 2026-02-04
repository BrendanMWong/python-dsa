class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while s[index] == ' ':
            index -= 1
        right_bound = index + 1
        while index >= -1:
            if s[index] == ' ':
                return len(s[index + 1:right_bound])
            index -= 1
        return len(s)
        