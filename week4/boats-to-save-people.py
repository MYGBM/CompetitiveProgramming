class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people)-1

        while l <= r:

            if people[r]+people[l] > limit or people[r] == limit:
                boats +=1
                r -=1
            elif people[r] + people[l]<=limit:
                boats += 1
                l += 1
                r -= 1
            

        return boats




            
        