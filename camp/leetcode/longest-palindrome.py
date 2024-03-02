class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        max_odd = 0
        ans = 0
        to_be_popped = 1

        for key,value in count.items():
            if value %2 !=0 and value > max_odd:
                max_odd = value
                to_be_popped = key
                

        if to_be_popped in count:
            count.pop(to_be_popped)
        ans = max_odd
        print(to_be_popped)
        for _,value in count.items():
            if value%2==0:
                ans+= value
            elif value%2!=0:
                ans+= value-1
        
        return ans
            
        
        
        




