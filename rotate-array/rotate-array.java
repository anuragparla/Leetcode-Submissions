class Solution {
    public void rotate(int[] nums, int k) {
        int nums_length = nums.length;
        int i = 0 , j = 0;
        int temp;
        int first_half =0;
        if (nums_length > 1 && k != nums_length) 
        {
            j = nums_length - 1;
          // reversing the array once 
            for ( i =0; i<nums_length/2; i++) {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                
                j -=1 ;
            }
            
            // revrsing from 0 to k 
            j = (k % nums_length) - 1;
            for ( int m = 0; m<((k % nums_length))/2 ; m++) {
                temp = nums[m];
                nums[m] = nums[j];
                nums[j] = temp;
                j -= 1;
            }
            
            // reversing from k to length
            j = nums_length -1;
            for ( int n = (k % nums_length); n<(nums_length+(k %               nums_length))/2;n++) {
                temp = nums[n];
                nums[n] = nums[j];
                nums[j] = temp;
                j -= 1;
            }
        }
        
            
        
        
    }
}