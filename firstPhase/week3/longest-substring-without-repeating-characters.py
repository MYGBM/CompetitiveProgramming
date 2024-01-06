class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = set()
        total = 0
        left_pointer = 0
        
        for right_pointer in range(len(s)):
            while s[right_pointer] in elements:
                elements.remove(s[left_pointer])
                left_pointer += 1

            elements.add(s[right_pointer])
            total = max(total,right_pointer-left_pointer +1)
        
        return total



        