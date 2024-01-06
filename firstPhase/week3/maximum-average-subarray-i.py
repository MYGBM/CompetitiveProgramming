class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pointer1 = 0
        pointer2 = k
        currSum = sum(nums[pointer1:pointer1+k])
        maxi = currSum
        while pointer2 < len(nums):
            currSum += nums[pointer2]
            currSum -= nums[pointer1]
            maxi= max(currSum,maxi)
            pointer1 += 1
            pointer2 +=1
        return maxi/k



        