class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalities = [0]*(len(customers)+1)
        customers += "N"

        n = 0
        for i in range(len(customers)):
            penalities[i] += n
            if customers[i] == "N":
                n += 1
        y = 0
        for i in range(len(customers)-1,-1,-1):
            if customers[i] == "Y":
                y += 1
            penalities[i] += y
        
        return penalities.index( min(penalities))
        

