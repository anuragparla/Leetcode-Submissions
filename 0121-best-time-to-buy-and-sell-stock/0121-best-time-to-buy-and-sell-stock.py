class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        if len(prices)<2:
            return 0
        left,right = 0,1
        while left<right and right <len(prices):
            if prices[left]<prices[right]:
                profit = prices[right]-prices[left]
                maxProfit = max(maxProfit,profit)
                right +=1
            else:
                left = right
                right +=1
        return maxProfit


    

       