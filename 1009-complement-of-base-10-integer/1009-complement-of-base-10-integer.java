class Solution {
    
    private int binaryToDecimal(List binList) {
        
        
        int prod = 1;
        int sum = 0;
        for ( int i=0;i<binList.size();i++) {
            prod = (int)Math.pow(2,i) * (int)binList.get(i);
            sum += prod;
        }
        
        return sum;
    }
    
    public int bitwiseComplement(int n) {
        if ( n == 0) {
            return 1;
        }
        else {
            int multiplier = 1;
            int res = 0;
            List<Integer> l = new ArrayList();
            while (n != 0) {
                int rem = n%2;
            //invert the rem and pass it to a decimal function 
                rem = rem ^ 1;
            
                l.add(rem);
                n = n/2;
            
        }
        
            res = binaryToDecimal(l); 
            return res;
        }
        
        //return 0;    
    }
    
    
}