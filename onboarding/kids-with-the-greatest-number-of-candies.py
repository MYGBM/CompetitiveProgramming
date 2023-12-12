class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        # print(maxCandy)
        output = []
        for candy in candies:
            if candy+extraCandies >= maxCandy:
                output.append(True)
            else:
                output.append(False)
        return output
        