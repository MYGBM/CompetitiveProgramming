class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compare(arr):
            return ((0-arr[0])**2 + (0-arr[1])**2)**0.5
        
        points.sort(key=compare, reverse=True) 
        j = k
        ans = []
        while j>0:
            ans.append(points[-1])
            points.pop()
            j-=1
        return ans

        