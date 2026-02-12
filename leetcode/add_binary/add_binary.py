class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Fill the shorter string with 0's on the left, to make both strings equal length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        output = ''
        carry = '0'

        for i in range(max_len - 1, -1, -1):
            # this is a string of 3 chars, not a number, example: '101'
            bits = a[i] + b[i] + carry 

            # bits.count(value) counts how many (value) are in bits
            if bits.count('1') == 0:
                output = '0' + output
                carry = '0'
            elif bits.count('1') == 1:
                output = '1' + output
                carry = '0'
            elif bits.count('1') == 2:
                output = '0' + output
                carry = '1'
            else:
                output = '1' + output
                carry = '1'

        if carry == '1':
            output = '1' + output
        return output