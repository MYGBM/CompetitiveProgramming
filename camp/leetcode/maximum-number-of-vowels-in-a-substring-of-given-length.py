class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        maxi_length = 0
        left = 0
        vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}

        for right in range(len(s)):
            if s[right] in vowels:
                vowels[s[right]]+=1
            
            if right-left+1 >k:
                if s[left] in vowels:
                    vowels[s[left]]-=1
                left+=1
            maxi_length = max(maxi_length,sum(vowels.values()))
        return maxi_length

        