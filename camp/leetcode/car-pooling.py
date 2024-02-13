class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        prefix_sum = [0 for i in range(1001)]
        # print(len(prefix_sum))
        # trips.sort(key=lambda x:x[1])
        for passenger,left,right in trips:
            prefix_sum[left] += passenger
            prefix_sum[right] -= passenger
        
        ans = [0]
        for i in range(len(prefix_sum)):
            ans.append(ans[i]+prefix_sum[i])
            if ans[i] > capacity:
                return False
        
        return True
        
            




        