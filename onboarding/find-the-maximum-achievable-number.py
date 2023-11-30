class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(2*t):
            num = num+1
        return num
        