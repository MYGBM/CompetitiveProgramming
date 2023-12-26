class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primaryDiagonal = 0
        secondaryDiagonal =0 
        column = len(mat[0]) 
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row ==col:
                    repeated = mat[row][col]
                    primaryDiagonal += mat[row][col]

                elif row+col ==  column -1:
                    secondaryDiagonal += mat[row][col]
        
        return primaryDiagonal +secondaryDiagonal

        