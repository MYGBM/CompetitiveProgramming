class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = 0
        check = skill[0] + skill[len(skill)-1]
        left = 0
        right = len(skill)-1

        while left < right:
            if skill[left] + skill[right] != check:
                return -1
            else:
                total += (skill[left]) * (skill[right])
            left += 1
            right -=1
        
        return total



        