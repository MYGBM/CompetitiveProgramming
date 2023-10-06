class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        majority=len(nums)/2
        for key,value in hash_map.items():
            if value>majority:
                return key
        return -1


        