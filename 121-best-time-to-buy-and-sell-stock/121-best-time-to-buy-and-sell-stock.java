class Solution {
    public int maxProfit(int[] prices) {
       /*
      int minPrice = Integer.MAX_VALUE; 
      int maxProfit = 0;  
      for(int i=0;i<prices.length;i++){
          if(prices[i]<minPrice){
              minPrice = prices[i];
          }
          else if(prices[i]-minPrice >maxProfit){
              maxProfit = prices[i]-minPrice;
          }
          
      } */
        if(prices.length<2){
            return 0;
        }
        else {
            int p1=0;
            int p2 =1;
            int maxProfit = 0;
            while(p2<prices.length) {
                if(prices[p2]<prices[p1]){
                    p1 = p2;
                    p2 = p2+1;
                }
                else {
                    int diff = prices[p2]-prices[p1];
                    if(diff>maxProfit){
                        maxProfit=diff;
                    }
                    p2++;
                }
            }
             return maxProfit;
        }
       
    }
}