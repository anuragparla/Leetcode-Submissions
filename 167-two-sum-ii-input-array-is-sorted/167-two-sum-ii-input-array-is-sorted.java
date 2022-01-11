class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lp = 0;
        int rp = numbers.length -1;
        int p1 = 0, p2 = numbers.length-1;
        int x, y = 0;
        int[] res = new int[2];
        // step 1 : find the diff 
        // step 2: search it in the space : 
        // step3 : not found then try diff combi 
        while(p1 <p2) {
            
            if((numbers[p1] + numbers[p2]) == (target)) {
                break;
            }
            else if((numbers[p1] + numbers[p2]) > (target) ) {
                p2--;
            }
            else {
                p1++;
            }
        }
        res[0] = p1+1;
        res[1] = p2+1;
        return res;
    }
}