class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_to_idx = {val:idx for idx,val in enumerate(nums2)}
        print(val_to_idx)
        stack = []
        answer = [-1 for i in range(len(nums2))]
        soln =[]
        
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                answer[val_to_idx[stack[-1]]] = nums2[i]
                stack.pop()
            if not stack:
                stack.append(nums2[i])
            elif stack and nums2[i]<=stack[-1]:
                stack.append(nums2[i])
        
        print(answer)      
        for i in range(len(nums1)):
            soln.append(answer[val_to_idx[nums1[i]]])
        
        return soln
        