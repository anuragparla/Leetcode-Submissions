/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    // var waysFor1Step = 0
    // var waysFor2Step = 0
    return recurse(n, {})

    function recurse(remainingSteps, memo){
        if (remainingSteps in memo){
            return memo[remainingSteps]
        }

        if (remainingSteps === 0){
            return 1
        }

        if (remainingSteps < 0){
            return 0
        }

         const waysFor1Step = recurse(remainingSteps - 1, memo)
         const waysFor2Step = recurse(remainingSteps - 2, memo)
        
        memo[remainingSteps] = waysFor1Step + waysFor2Step
       

        return waysFor1Step + waysFor2Step
        
    }
    

};