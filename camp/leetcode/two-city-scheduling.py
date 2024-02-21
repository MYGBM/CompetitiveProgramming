class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        def compare(arr):
            return arr[0] - arr[1]
        
        costs.sort(key= compare)

        ans = 0

        for i in range(len(costs)//2):
            ans+=costs[i][0]

        for j in range(len(costs)//2,len(costs)):
            ans+=costs[j][1]
        
        return ans




        