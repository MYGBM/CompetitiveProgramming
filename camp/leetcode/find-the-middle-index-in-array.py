class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = nums
        for i in range(1,len(prefix_sum)):
                prefix_sum[i] += prefix_sum[i-1]

        print(prefix_sum)

        for i in range(len(prefix_sum)):
            if i==0:
                left_sum = 0
                right_sum = prefix_sum[-1] - prefix_sum[i]
                if left_sum == right_sum:
                    return i
            elif i==len(prefix_sum)-1:
                left_sum = prefix_sum[i-1]
                right_sum = 0
                if left_sum == right_sum:
                    return i
            else:
                left_sum = prefix_sum[i-1]
                right_sum = prefix_sum[-1] - prefix_sum[i]
                if left_sum == right_sum:
                    return i

            

        return -1

        