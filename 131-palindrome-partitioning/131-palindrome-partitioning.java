class Solution {
    
    private boolean isPali(String s, int i, int j) {
        
        while(i<j) {
            if(s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    private void dfs(int i, List<List<String>> res, List<String> part,String s) {
        if(i>=s.length()) {
            res.add(new ArrayList<String>(part));
            return;
        }
        for(int j = i; j<s.length();j++) {
            if (isPali(s,i,j)) {
                part.add(s.substring(i,j+1));
                dfs(j+1,res,part,s);
                part.remove(part.size()-1);
            }
        }
        //return res
    }
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<List<String>>();
        List<String> part = new ArrayList<String>();
        
        dfs(0,res,part,s);
        return res;
    }
}