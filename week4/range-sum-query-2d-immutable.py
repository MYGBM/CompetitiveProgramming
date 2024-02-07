class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = matrix
        self.prefix_range = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row==0 and col==0:
                    self.prefix[row][col] = self.prefix[row][col]
                elif row==0 and col!=0:
                    self.prefix[row][col] =  self.prefix[row][col-1]+self.prefix[row][col]
                elif row!=0 and col==0:
                    self.prefix[row][col] = self.prefix[row][col] +self.prefix[row-1][col]
                else:
                    self.prefix[row][col] = self.prefix[row-1][col]+self.prefix[row][col-1]+self.prefix[row][col]-self.prefix[row-1][col-1]
        
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            self.prefix_range = self.prefix[row2][col2]
        elif row1==0 and col1!=0:
            self.prefix_range = self.prefix[row2][col2] - self.prefix[row2][col1-1]
        elif row1!=0 and col1==0:
            self.prefix_range = self.prefix[row2][col2] - self.prefix[row1-1][col2]
        else:    
            self.prefix_range = self.prefix[row2][col2] -self.prefix[row2][col1-1]-self.prefix[row1-1][col2]+self.prefix[row1-1][col1-1]
        
        return self.prefix_range 


        




        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)