class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        sSort = s[:]
        sSort.sort(key = lambda x:len(x))
        longWord = len(sSort[-1])
        output = []
        
        for charIdx in range(0,longWord):
            temp = ""
            
            for wordIdx in range(0,len(s)):
                if len(s[wordIdx]) <= charIdx:
                    temp+=" "
                else:
                    temp+=s[wordIdx][charIdx]
                    
            output.append(temp.rstrip())
            
        return output
                    
        
                