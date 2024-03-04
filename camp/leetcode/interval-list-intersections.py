class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        new = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            if start1 <= end2 and start2 <= end1:
                new_start = max(start1, start2)
                new_end = min(end1, end2)
                new.append([new_start, new_end])
            
            if end1 < end2:
                i += 1
            else:
                j += 1
                
        return new


