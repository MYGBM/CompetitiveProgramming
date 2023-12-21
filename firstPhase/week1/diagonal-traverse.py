class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        hashMap = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                hashMap[row+col].append(mat[row][col])
        print(hashMap)
        for key in hashMap:
            if key %2==0:
                output.extend(hashMap[key][::-1])
            else:
                output.extend(hashMap[key])
        return(output)