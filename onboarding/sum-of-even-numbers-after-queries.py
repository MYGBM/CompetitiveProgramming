class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        for num in nums:
            if num%2==0:
                total += num

        output = []
        for val,index in queries:
            oldVal = nums[index]
            newVal = nums[index] + val
            if oldVal%2==0:
                if newVal%2==0:
                    total+= newVal - oldVal

                else:
                    total -=oldVal
            
            else:
                if newVal%2==0:
                    total += newVal

            nums[index] = newVal
            output.append(total)

        return output


        