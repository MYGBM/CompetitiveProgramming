class Solution:
    def maxScore(self, s: str) -> int:
        temp = list(s)
        s_original = [int(i) for i in temp]
        print(s_original)
        

        print(s_original)
        prefix_s = [s_original[0]]

        for i in range(1,len(s_original)):
            prefix_s.append(prefix_s[i-1] + s_original[i])
        
        maxi = float("-inf")
        for i in range(len(prefix_s)):
            if i==len(prefix_s)-1:
                break
            prefix_s[i] = (prefix_s[-1] -prefix_s[i]) + ((i+1) - prefix_s[i]) # right sum + left sum
            maxi = max(prefix_s[i],maxi)
        
        return maxi

    

        















        