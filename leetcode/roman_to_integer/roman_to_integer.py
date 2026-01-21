# Brute force method
class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        i = 0

        while i < len(s):
            # Check subtraction pairs first
            if i + 1 < len(s) and s[i] == "I" and s[i + 1] == "V":
                output += 4
                i += 2
            elif i + 1 < len(s) and s[i] == "I" and s[i + 1] == "X":
                output += 9
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "L":
                output += 40
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "C":
                output += 90
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "D":
                output += 400
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "M":
                output += 900
                i += 2
            else:
                # Check single letters next
                if s[i] == "I":
                    output += 1
                elif s[i] == "V":
                    output += 5
                elif s[i] == "X":
                    output += 10
                elif s[i] == "L":
                    output += 50
                elif s[i] == "C":
                    output += 100
                elif s[i] == "D":
                    output += 500
                elif s[i] == "M":
                    output += 1000
                i += 1
        return output

# Optimized method using a dictionary
class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral character to its integer value
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        output = 0 # Final integer result
        prev_value = 0 # Value of the previous (right-side) numeral

        # Loop through the string from right to left
        for char in reversed(s):
            # Convert the current Roman numeral to its integer value
            current_value = roman_numerals[char]

            # If the current value is smaller than the value to its right, subtract it; otherwise, add it
            if current_value < prev_value:
                output -= current_value
            else:
                output += current_value

            # Update the previous value for the next iteration
            prev_value = current_value

        return output