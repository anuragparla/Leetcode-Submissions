class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_height = 0
        max_width = 0
        max_area = 0
        while left<right:
            if left == right :
                break 
            elif height[left]<height[right]:
                max_height = height[left]
                max_width  = (right+1)-(left+1)
                if max_area < max_height * max_width:
                    max_area = max_height * max_width
                left +=1 
            elif height[left]>height[right]:
                max_height = height[right]
                max_width  = (right+1)-(left+1)
                if max_area < max_height * max_width:
                    max_area = max_height * max_width
                right -=1 
            else: 
                max_height = height[left]
                max_width = (right+1)-(left+1)
                if max_area < max_height * max_width:
                    max_area = max_height * max_width
                left +=1 
                right -=1
        return max_area
     
                    
                
                
                