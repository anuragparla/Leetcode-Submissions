class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
       //System.out.println(nums1[4]); 
        int k = m+n-1,i=m-1,j=n-1;
        while(i>=0 && j>=0){
            if(nums1[i]<nums2[j]){
                nums1[k]=nums2[j];
                j--;
                k--;
            }
            else{
                //int temp = nums1[i];
                nums1[k] = nums1[i];
                //nums2[j] = temp;
                i--;
                //j--;
                k--;
            }
        }
        
        while(j>=0){
            nums1[k]=nums2[j];
            k--;
            j--;
        }
    }
}