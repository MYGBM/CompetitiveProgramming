#User function Template for python3

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
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Endshttps://media.geeksforgeeks.org/img-practice/prod/courses/1/Web/Other/Fab%20icon%20(1)_1697541057.svg