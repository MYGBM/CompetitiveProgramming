class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0
        while right <len(typed):
            
            if  left <len(name) and typed[right] == name[left]:
                left+=1
                right+=1

            elif right>0 and typed[right]==typed[right-1]:
                    right+=1
            else:
                return False

        return len(name) == left



        