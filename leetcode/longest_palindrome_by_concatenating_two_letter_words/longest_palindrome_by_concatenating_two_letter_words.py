class Solution:
    def longestPalindrome(self, words):
        freq = {}
        length = 0
        used_middle = False

        for word in words:
            reverse = word[::-1]

            if reverse in freq and freq[reverse] > 0:
                length += 4
                freq[reverse] -= 1
            else:
                freq[word] = freq.get(word, 0) + 1

        # check if we can place one palindrome word in middle
        for word in freq:
            if word[0] == word[1] and freq[word] > 0:
                length += 2
                break

        return length