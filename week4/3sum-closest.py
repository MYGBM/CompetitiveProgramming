class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_distance = float("inf")
        min_sum = 0
        curr_sum =0

        for i in range(len(nums)):

            l = i+1
            r = len(nums)-1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(target - curr_sum) < min_distance:
                    min_sum = curr_sum
                    min_distance = abs(target - curr_sum)

                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l +=1
                else:
                    min_sum = nums[i] + nums[l] +nums[r]
                    return min_sum

        return min_sum


                






        