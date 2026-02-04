class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for digit_place in range(len(digits) - 1, -1, -1):
            if digits[digit_place] < 9:
                digits[digit_place] = digits[digit_place] + 1
                return digits
            else:
                digits[digit_place] = 0
        return [1] + digits
        