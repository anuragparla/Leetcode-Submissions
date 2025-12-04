/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (!coins || coins.length === 0){
        return -1
    }
    
    const result = recurse(coins,amount,{})
    return result === Infinity ? -1 : result
    function recurse(coins,amount,memo){
        
        if (amount in memo ) {
            return memo[amount]
        }

        if (amount === 0){
            return 0
        }

        if (amount < 0){
            return Infinity
        }
        let minCoins = Infinity

        for (let coin of coins){
            const res = recurse(coins,amount - coin, memo) 
            if (res !== Infinity){

            minCoins = Math.min(minCoins, 1+res)
            }
        }

        memo[amount] = minCoins
        return minCoins
          
    }
};