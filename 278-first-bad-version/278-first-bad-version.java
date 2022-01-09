/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        /*
        int mid = 0;    
        int lp = 1;
        int rp = n;
        while(lp<rp) {
            mid = lp+(rp-lp)/2;
            if( isBadVersion(mid) != true) {
                lp = mid +1;
            }
            else {
                rp = mid;
            }
            
        }
        return lp;*/
        int left = 1, right = n;
        
        while(left < right) {
            int mid = left + (right-left) / 2;
            if (isBadVersion(mid) == true) right = mid;
            else left = mid+1;
        }
        return left;
    }
    
}