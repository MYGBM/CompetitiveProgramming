class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            image[row] = image[row][::-1]
            for col in range(len(image[row])):
                if image[row][col]==0:
                    image[row][col]=1
                else:
                    image[row][col]=0


        return image
        