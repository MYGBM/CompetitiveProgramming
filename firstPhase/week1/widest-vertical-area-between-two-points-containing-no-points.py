class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        # print(points)
        max_width = 0
        for idx, (x,y) in enumerate(points[:-1]):
            max_width = max(max_width,points[idx+1][0] - x)
        
        return max_width




           

        # def custom_comparator(points):
        #     for x, y in points:
        #         return y

        # points.sort(key=custom_comparator)
        # return points
           
        
        