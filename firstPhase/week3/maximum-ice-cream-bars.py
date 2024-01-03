class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs)
        freq_arr = [0 for i in range(n+1)]

        for idx in costs:
            freq_arr[idx] += 1
        print(freq_arr)
        
        count = 0
        for i in range(len(freq_arr)):
            if coins >=0:
                if freq_arr[i] != 0:
                    count += min(freq_arr[i],coins//i)
                    coins = coins - (i)*(min(freq_arr[i],coins//i))
                    print(coins, count)

            else:
                break
        return count



        


        