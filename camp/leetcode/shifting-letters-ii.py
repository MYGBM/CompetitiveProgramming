class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # convert string to integer
        string = []
        for char in s:
            string.append(ord(char)-97)
        print(string)

        prefix_sum = [0 for _ in range(len(s)+1)]
        print(prefix_sum)

        for left,right,direction in shifts:
            if direction == 0:
                prefix_sum[left] += -1
                prefix_sum[right+1] += 1
            else:
                prefix_sum[left] += 1
                prefix_sum[right+1] -= 1
      
        #get the prefix_sum
        prefix_sum.pop()
        print(prefix_sum)
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        print(prefix_sum)

        #adding prefix_sum to string and converting back
        for i in range(len(string)):
            string[i] = chr((prefix_sum[i] + string[i])%26 +97)
        
        return "".join(string)



        
        
        
       

        