class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs)
        freq_arr = [0 for i in range(n+1)]

        for idx in costs:
            freq_arr[idx] += 1


        start = 0
        for idx,val in enumerate(freq_arr):
            for i in range(val):
                costs[start] = idx
                start += 1
        print(costs)
        total = costs[0]
        count = 0
        i =0
        # for i in range(len(costs)):
        #     if total<=coins:
        #         print(total)
        #         total += costs[i]
        #         count +=1
        #     else:
        #         break

        while i < len(costs) and coins - costs[i] >= 0:
            count += 1
            coins -= costs[i]
            i += 1

        return count


        