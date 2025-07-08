class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        max_water = 0
        while left != right:
            h = min(height[left],height[right])
            w = right - left
            max_water = max(max_water, (h*w))
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return max_water

        

        '''
        height of length n 
        no of vertical lines = n which means height array is the height of these lines 
        two endpoints of ith line are i,0 and i,height[i] => 
        that means lower end is i and upper  is height[i]
        find two lines such that they form a container that can hold max water 
        difference in the indexes gives the breadth 
        I think we can always start with left and right pointers l = 0 r = 8
        width = r - l 
        height = if height[r] <= height[l] then rth height else lth height 
        product of width n height gives vol 
        compare with max vol and update max vol 
        whose height is less move that pointer only 
        '''
