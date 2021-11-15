class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<Integer> l1 = new ArrayList();
        l1.add(1);
        List<List<Integer>> ml = new ArrayList();
         ml.add(l1);
        if(numRows>1){
            List<Integer> l2 = new ArrayList();
        l2.add(1);
        l2.add(1);
        ml.add(l2);
        
        }
                
        for(int i=2;i<numRows;i++){
            List<Integer> temp = ml.get(i-1);
            List<Integer> newl = new ArrayList();
            int size = temp.size();
            for(int j=0;j<size;j++){

                if (j==0 || j==size-1){
                    newl.add(1);
                }
                if(j!=size-1){


                newl.add(temp.get(j)+temp.get(j+1));
                }
            }
            ml.add(newl);
        }

        return ml;
        
    }
}