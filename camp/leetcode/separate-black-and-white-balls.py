class Solution:
    def minimumSteps(self,  s: str) -> int:
        ones = []
        res = 0
        for idx,char in enumerate(s):
            if char=="1":
                ones.append(idx)
        for i in range(len(s)-1,-1,-1):
                if ones:
                    res+= abs(i-ones[-1])
                    ones.pop()
        return res


        
        


