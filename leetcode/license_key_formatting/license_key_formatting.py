class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        clean_s = s.replace("-", "").upper()

        # A list of chunks of the string
        parts = []
        
        # Process from the end
        for index in range(len(clean_s), 0, -k):
            # Prevents negative slicing
            start = max(0, index - k)
            parts.append(clean_s[start:index])

        # We built it backwards, so reverse
        return "-".join(reversed(parts))
            