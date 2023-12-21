class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi = 0
        
        for row in range(len(grid) - 2):
           for col in range(len(grid[0]) - 2):
               curr_sum = sum(grid[row][col : col + 3]) + grid[row + 1][col + 1] + sum(grid[row + 2][col : col + 3])
               maxi = max(curr_sum , maxi)       

        return maxi