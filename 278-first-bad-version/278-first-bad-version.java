/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
     // n is the total no of version 
        // 1 2 3 4 5 6 7 8 9       isBadVersion(int version) --> gives bad or not 
        // if 1 v is bad then all followings are bad 
        // lets say 2 is fbv but mid is 5 so 5 is also a bad v 
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
        return lp;
    }
    
}