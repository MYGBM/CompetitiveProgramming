class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        hashTable={}
        for i in range(0,n+1):
            hashTable[i]=0
        for i in nums:
            hashTable[i]+=1
        for num in hashTable:
            if hashTable[num]==0:
                return num