class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Convert both strings to lists of integers
        num1 = list(map(int, num1))
        num2 = list(map(int, num2))
        
        # Find the minimumLength
        min_len = num1
        max_len = num2
        if len(num2) < len(num1):
            min_len = num2
            max_len = num1

        # Handle the case for unequal length strings
        # Add leading zeros in front of the smaller list
        if len(num1) != len(num2):
            leading_zeros = len(max_len) - len(min_len)
            # Add the leading zeros to the smaller list
            min_len = [0] * leading_zeros + min_len

        # Add element by element
        sum_list = []
        sum_carry = 0
        for i in range(len(min_len) - 1, -1, -1):
            temp_sum = max_len[i] + min_len[i] + sum_carry
            # Handle overflow
            if temp_sum >= 10:
                sum_carry = temp_sum // 10
                temp_sum = temp_sum % 10
            else:
                sum_carry = 0
            sum_list.append(temp_sum)

        #handle carry over case at the end
        if sum_carry>0:
            sum_list.append(sum_carry)
        sum_list.reverse()
        
        # Convert the sum_list back to a string
        result = ''.join(map(str, sum_list))
        
        return result
    
           












        
        