class Solution:
    def smallestNumber(self, num: int) -> int:
        result = []
       

        if num >= 0:
            flag = 0
            nums = list(map(int,str(num)))
           
        else:
            flag = 1
            num = str(num)[1:]
            nums = list(map(int,str(num)))
    

        if flag ==0:
            nums.sort()
            for i in range(len(nums)):
                if nums[i]!= 0:
                    result.append(nums[i])
                    result.extend(nums[0:i])
                    result.extend(nums[i+1:len(nums)])
                    break
            else:
                return 0


        elif flag ==1:
            nums.sort(reverse=True)
            return 0 - int("".join(map(str,nums)))





        return int("".join(map(str,result)))
    

       