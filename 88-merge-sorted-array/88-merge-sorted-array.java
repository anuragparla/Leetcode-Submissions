class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
       int i = nums1.length - nums2.length - 1;
       //for(int m = 0; m<nums)
       int j = nums2.length - 1;
       int k = nums1.length - 1;
        if(m == 0){
            for(int a = 0; a<nums2.length; a++) {
                nums1[a] = nums2[a];
            }
        }
       while(i >= 0 && j>= 0) {
           if(nums1[i] <= nums2[j])
           {
               nums1[k] = nums2[j];
               j -= 1;
           }
           else {
               nums1[k] = nums1[i];
               i -= 1;
           }
           k -= 1;
       }
        if(i <0) {
            while(j >= 0 && k>=0) {
               nums1[k] = nums2[j];
                k -=1;
                j -= 1;
            }
        }
    }
}