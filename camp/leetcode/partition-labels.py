class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        ans = []
        l = 0
    
        for i in range(len(s)):
            hashMap[s[i]] = i
        r = hashMap[s[0]]
        print(hashMap) 
        curr = 0
        while r < len(s):
            if hashMap[s[l]] > r:
                r = hashMap[s[l]]

            elif hashMap[s[l]] <r or (hashMap[s[l]]==r and l!=r): 
                l+=1
            
            #partitioning
            elif l==r:
                ans.append(r-curr+1)
                if r!=len(s)-1:
                    l = r+1
                    curr = l
                    r = hashMap[s[l]]
                else:
                    return ans
            
        
        return ans

    



        
        