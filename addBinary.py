class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Make the lengths similar
        min_len = a
        max_len = b
        if len(b) < len(a):
            min_len = b
            max_len = a

        # Add leading zeros in front of the smaller string
        if len(a) != len(b):
            leading_zeros = len(max_len) - len(min_len)
            # Add the leading zeros to the smaller string
            min_len = "0" * leading_zeros + min_len

        carry = 0
        result = ""
        for i in range(len(max_len)-1, -1, -1):
            summ = int(max_len[i]) + int(min_len[i]) + carry
            carry = summ // 2
            digit = summ % 2
            result = str(digit) + result

        if carry > 0:
            result = "1" + result

        return result
