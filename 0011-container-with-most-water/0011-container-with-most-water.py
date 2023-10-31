class Solution:
    def maxArea(self, height: List[int]) -> int:

    #    #BRUTE FORCE APPROACH O(n^2)
    #    area=0
    #    for l in range(len(height)):
    #        for w in range(l+1,len(height)):
    #            tempArea=(w-l) *min(height[w],height[l])
    #            area=max(area,tempArea)
    #    return area
    #    #OPTIMAL SOLUTION
         res=0
         l,r=0,len(height)-1
         while l<r:
            area=((r-l)*min(height[l],height[r]))
            res=max(res,area)
            if height[l]<height[r]:
                 l+=1
            else:
                r-=1
         return res



