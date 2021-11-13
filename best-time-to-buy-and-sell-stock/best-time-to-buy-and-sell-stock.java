class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0,i=0,j=i+1,diff=0;
        while(i<prices.length-1 && j<prices.length){
            if(prices[i]>prices[j]){
                j++;
                i++;
            }
            else{
                
                maxProfit = max(maxProfit,prices[j]-prices[i]);
                j++;
                if((j<prices.length) && (prices[j]<prices[i])){
                    i=j;
                    j++;
                }
            }
        }
        return maxProfit;
    }
    
    private int max(int mp,int currpro){
        if(currpro>mp){
            return currpro;
        }
        else{
            return mp;
        }
    }
}