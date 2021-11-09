class Solution {
    public int removeElement(int[] nums, int val) {
        
        int count =0,i=0,j=nums.length-1;
        
        while(i<=j){
            if(nums[i]== val && nums[j]==val){
                j--;
                count++;
            }
            else if(nums[j]==val){
                i++;
                j--;
                count++;
            }
            else if(nums[i]==val){
                swap(nums,i,j);
                i++;
                j--;
                count++;
            }
            else{
                i++;
            }
                
            }
       
            return nums.length-count;
        
        }
    private void swap(int[] nums,int i,int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
        
    }
