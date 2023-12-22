class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:    
        inc_flag = 0
        if len(arr)<3:
            return False

        else:
            if arr[1]<=arr[0]:
                return False

            else:
                i = 0 
                while i < len(arr)-1:
                    if arr[i+1]<arr[i]:
                        inc_flag = 1
                        decreasing_index = i+1
                        break

                    elif arr[i+1]==arr[i]:
                        return False

                    i += 1
                
                if inc_flag!=1:
                    return False
                else:
                    while decreasing_index <len(arr)-1:
                        if arr[decreasing_index+1]>=arr[decreasing_index]:
                            return False
                        decreasing_index += 1
                    return True
                
            

                




            
        