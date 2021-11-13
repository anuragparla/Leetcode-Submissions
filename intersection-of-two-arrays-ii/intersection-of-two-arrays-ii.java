class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> l = new ArrayList<Integer>();
        Map<Integer,Integer> hshmap = new HashMap();
        
        for(int i=0;i<nums1.length;i++){
            if(!(hshmap.containsKey(nums1[i]))){
                hshmap.put(nums1[i],0);
            }
            hshmap.put(nums1[i],hshmap.get(nums1[i])+1);
        }
        
        for(int j=0;j<nums2.length;j++){
            if(hshmap.containsKey(nums2[j])&&hshmap.get(nums2[j])>0){
                l.add(nums2[j]);
                hshmap.put(nums2[j],hshmap.get(nums2[j])-1);
                
            }
        }
    
        int[] res = new int [l.size()] ;
        for(int k=0;k<res.length;k++){
            res[k]=l.get(k);
        }
        
        return res;
    }
}