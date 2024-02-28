class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window_size=10**6
        current_window_sum=0
        window_start=0

        for window_end in range(len(nums)):
            current_window_sum+=nums[window_end]

            while current_window_sum>=target:
                min_window_size=min(min_window_size,window_end-window_start+1)
                current_window_sum-=nums[window_start]
                window_start+=1

        return 0 if min_window_size==10**6 else min_window_size
        