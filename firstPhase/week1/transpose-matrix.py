class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = []
        for col_indx in range(len(matrix[0])):
            tempTransposed = []
            for row_indx in range(len(matrix)):
                tempTransposed.append(matrix[row_indx][col_indx])
            
            transposed.append(tempTransposed)

        
                
        return transposed
        
        