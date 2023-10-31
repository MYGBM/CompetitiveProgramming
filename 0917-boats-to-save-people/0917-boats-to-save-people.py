class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort the people inorder to pair the heaviest people with the lightest people
        people.sort()

        boats=0
        l,r=0,len(people)-1

        while l<=r: # to handle the case for last person left
            #since the people array is sorted we can be sure that we are going to be pairing up the heaviest people with the lightest people
            if people[l]+people[r]<=limit:
                #incerement both pointers: essentially removing the people to a boat
                l+=1
                # r-=1
            #we want to reserve a separate boat for the heavy person
            boats+=1
            r-=1
        return boats
    






