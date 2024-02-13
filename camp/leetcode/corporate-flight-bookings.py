class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0 for i in range(n)]

        #handle the queries
        for left,right, value in bookings:
            prefix_sum[left-1] += value 
            if right != n:
                prefix_sum[right] -= value 

        print(prefix_sum)
        
        #calculate the prefix_sum

        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]

        print(prefix_sum)

        return prefix_sum
            
            

        