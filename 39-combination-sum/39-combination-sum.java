class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
         /*
         -> distinct integers candidates[]
         -> target integer target 
         --> different combinations which result in target 
         --> one of the number in the combination should be different to make it unqiue
         --> total combinations to be less than 150
         
         */
        
        List<List<Integer>>[] dp = new List[target + 1];
        dp[0] = new ArrayList<>();
        dp[0].add(new ArrayList<>());
          
        for (int c : candidates) {
            for (int i = c; i <= target; i++) {
                if (dp[i - c] != null) {
                    if (dp[i] == null)
                        dp[i] = new ArrayList<>();
                                    
                    for (List<Integer> list : dp[i - c]) {
                        List<Integer> copy = new ArrayList<>(list);
                        copy.add(c);
                        
                        dp[i].add(copy);
                    }
                }
            }            
        } 
        
        return dp[target] == null ? new ArrayList<>() : dp[target];
    }
}