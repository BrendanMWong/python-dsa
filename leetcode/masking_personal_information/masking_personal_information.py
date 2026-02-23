class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s_lower = s.lower()
            name, email = s_lower.split('@')
            return name[0] + '*****' + name[-1] + '@' + email
        else:
            output = ''
            for char in s:
                if char.isdigit():
                    output += char
            country_code_digits = len(output) - 10
            prefix = ''
            for digit in range(country_code_digits):
                prefix += '*'
            if prefix != '':
                prefix += '-'
                prefix = '+' + prefix
            return prefix + '***-***-' + output[-4:]