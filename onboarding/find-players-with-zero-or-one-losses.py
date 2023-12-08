class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers= {}
        champions=set()
        
        # adding players who lost and their number of losses
        for i in range(len(matches)):
            if matches[i][1] not in losers:
                losers[matches[i][1]]=1
            else:
                 losers[matches[i][1]]+=1
                    
       # adding players who never lost                 
        for i in range(len(matches)):
            if matches[i][0] not in losers:
                champions.add(matches[i][0])
        champions=list(champions)
                
        #list comprehension to get players with one loss
        one_loss=[x for x in losers if losers[x]==1]
        
        
        one_loss.sort()
        champions.sort()
        
        return [champions,one_loss]
        
        
        
                
        

        
        
        