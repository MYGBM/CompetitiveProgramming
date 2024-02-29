class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0
        left = 0
        mini = inf
        for right in range(len(blocks)):
            if blocks[right] =="W":
                w_count +=1

            if right-left+1==k:
                mini = min(mini,w_count)
                if blocks[left]=="W":
                    w_count-=1
                left+=1
            print(w_count)    
        return mini
            
            
        