class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        time complexity: O(N)
        space complexity: O(N)
        approach:
        since each child must have at least 1 candy let's have allocate 1 candy to all children
        since a child will have 1 or 2 neighbors we need to make sure we compare on either sides
        when all the candies are of value 1, we can just increase the candy count by 1 if the neighbor to the left has a rating less than you 
        once it is done and while comparing the right neighbor's rating, we cannot blindly increase increase the candy count by 1 since the current child might have already had more candy than what would be given by increasing neighbor's candy count by 1 
        hence we need to do a max on both the values and then assign 
        finally sum the candies of given to all the children
        '''
        #base case
        if len(ratings) == 0 or ratings is None:
            return -1 
        if len(ratings) == 1:
            return 1
        candies = [1] * len(ratings)
        min_candies = 0
        #compare left
        for i in range(1,len(ratings)):
            if ratings[i]> ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        #compare right
        min_candies = candies[len(candies)-1]
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
            min_candies += candies[i]
        
        return min_candies
            
        