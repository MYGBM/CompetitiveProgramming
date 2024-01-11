class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        l = 0
        r = 0

        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                count += 1
                l += 1
                r += 1

            elif s[r] < g[l]:
                r += 1
            
        return count






        