# Sliding window version, simple
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is longer than haystack, return early
        if len(needle) > len(haystack):
            return -1
        
        # How many possible places needle can be in haystack
        # +1 because 0 is an index position
        possible_places = len(haystack) - len(needle) + 1

        # Slide the window each iteration
        for index in range(possible_places):
            # Set where the sliding window is
            sliding_window_start = index
            sliding_window_end = index + len(needle)

            # Determine if the string in the sliding window equals needle
            if haystack[sliding_window_start:sliding_window_end] == needle:
                return sliding_window_start
        return -1
    
# KMP version
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Step 1: Build LPS array for the needle
        lps = [0] * len(needle)

        prefix_length = 0  # length of the current matching prefix
        needle_index = 1   # current position in needle while building LPS

        while needle_index < len(needle):
            if needle[needle_index] == needle[prefix_length]:
                prefix_length += 1
                lps[needle_index] = prefix_length
                needle_index += 1
            else:
                if prefix_length != 0:
                    prefix_length = lps[prefix_length - 1]
                else:
                    lps[needle_index] = 0
                    needle_index += 1

        # Step 2: Search needle inside haystack using LPS
        haystack_index = 0  # pointer in haystack
        needle_index = 0    # pointer in needle

        while haystack_index < len(haystack):
            if haystack[haystack_index] == needle[needle_index]:
                haystack_index += 1
                needle_index += 1

                if needle_index == len(needle):
                    return haystack_index - needle_index
            else:
                if needle_index != 0:
                    needle_index = lps[needle_index - 1]
                else:
                    haystack_index += 1

        return -1
