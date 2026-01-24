class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, there is no common prefix
        if not strs:
            return ""

        # Loop through each character index of the first string
        for char_index in range(len(strs[0])):
            # Compare this character with the same position in every string
            for current_string in strs:
                # If the current string is too short
                # OR the characters do not match, stop immediately
                if char_index >= len(current_string) or current_string[char_index] != strs[0][char_index]:
                    # Return everything before char_index in the first string of strs
                    return strs[0][:char_index]

        # If we never found a mismatch, the entire first string is the prefix
        return strs[0]
