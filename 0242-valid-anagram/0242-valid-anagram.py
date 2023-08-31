class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s)!=len(t):
            return False
        else:
            hashTableS={}
            hashTableT={}
            for i in s:
                if i not in hashTableS:
                    hashTableS[i]=0
                hashTableS[i]+=1
            for i in t:
                if i not in hashTableT:
                    hashTableT[i]=0
                hashTableT[i]+=1
            for key in hashTableS:
                if key not in hashTableT or hashTableS[key] != hashTableT[key]:
                    return False

            return True
            
            
        

        
         

