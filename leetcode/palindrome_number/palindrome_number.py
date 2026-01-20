# No strings used
# Half reversal, made from scratch

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        reverse = 0
        while reverse < x:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10

        if x == reverse // 10 or x == reverse:
            return True
        return False

# Full reversal, easier to understand, slower
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x
    
# String used, simplest
# Fastest speed on LeetCode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s= str(x)
        # Slice syntax: sequence[start:stop:step]
        # Start is inclusive, default is 0
        # Stop is exclusive, default is end of sequence
        # Step is the increment, default is 1
        return s==s[::-1]

