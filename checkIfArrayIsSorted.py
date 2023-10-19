class Solution:
    def arraySortedOrNot(self, arr, n):
        pointer1=0
        pointer2=1
        while pointer2<=len(arr)-1:
            if arr[pointer2]<arr[pointer1]:
                return 0
            pointer1+=1
            pointer2+=1
        return 1
        
