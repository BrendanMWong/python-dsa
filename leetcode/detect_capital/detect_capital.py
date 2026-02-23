class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        elif word.isupper():
            return True
        elif len(word) > 1 and word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
