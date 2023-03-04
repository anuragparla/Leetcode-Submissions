class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
     
        newImage = []
        for i in range(len(image)):
            x = image[i][::-1]
            for i in range (len(x)):
                if x[i] == 1:
                    x[i] = 0
                else:
                    x[i] = 1
            newImage.append(x)
        return newImage
