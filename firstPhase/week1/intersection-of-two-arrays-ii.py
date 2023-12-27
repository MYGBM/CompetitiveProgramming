class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)

        print(freq1)
        print(freq2)

        soln= []

        for val in freq1:
            if val in freq2:
                for i in range(min(freq1[val],freq2[val])):
                    soln.append(val)
        
        return soln



        