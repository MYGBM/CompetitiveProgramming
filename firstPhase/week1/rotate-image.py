class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashMap =set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row,col) not in hashMap and (col,row) not in hashMap:
                    matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
                    hashMap.add((row,col))

        for row in range(len(matrix)):
            matrix[row]=matrix[row][::-1]
        
