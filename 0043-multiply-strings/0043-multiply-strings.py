class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Reverse the input strings
        num1 = num1[::-1]
        num2 = num2[::-1]

        # Initialize the result list with zeros
        result = [0] * (len(num1) + len(num2))

        # Perform digit multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2

                # Calculate carry and current digit
                carry = product // 10
                digit = product % 10

                # Update the result list
                result[i + j] += digit
                result[i + j + 1] += carry

        # Perform carry propagation
        for i in range(len(result) - 1):
            carry = result[i] // 10
            result[i] %= 10
            result[i + 1] += carry

        # Reverse the result and convert to string
        result = result[::-1]
        result_str = ''.join(map(str, result))

        # Remove leading zeros
        while len(result_str) > 1 and result_str[0] == '0':
            result_str = result_str[1:]

        return result_str





        