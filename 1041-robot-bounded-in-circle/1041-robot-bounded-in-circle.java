class Solution {
    public boolean isRobotBounded(String instructions) {
        int ns = 0, ew = 0;
        int direction = 1;   // 1 -> north; 2 -> east; 3 -> south; 4 -> west;
		
        for(char c: instructions.toCharArray()) {
            if(c == 'G') {
                if(direction == 1) { // North
                    ns++;
                } else if(direction == 2) { // East
                    ew++;
                } else if(direction == 3) { // South
                    ns--;
                } else { // West
                    ew--;
                }
            } else if(c == 'L') { // move left
                if(direction == 1) { 
                    direction = 5;
                }
                direction--;
            } else { // move right
                if(direction == 4) {
                    direction = 0;
                }
                direction++;
            }
        }

                
        // The robot stays in the circle if and only if (looking at the final vector) 
        // it changes direction (ie. doesn't stay pointing north), or it moves from origin (0,0).
        
        if (ns == 0 && ew == 0)
            return true;

        return (direction == 1) ? false : true;
    }
}