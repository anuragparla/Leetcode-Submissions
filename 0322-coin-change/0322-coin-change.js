/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    if (!coins || coins.length === 0){
        return -1
    }
    const result = recurse(coins,0, amount,{})
    return result === Infinity ? -1 : result

    function recurse(coins,index,amount,memo){
        const key = index + '-'+ amount

        if (amount === 0){
            return 0
        }

        if(amount <0 || index >= coins.length){
            return Infinity
        }

        if (key in memo){
            return memo[key]
        }

        const coinNotChosen = recurse(coins,index+1,amount, memo)

        const  coinChosen = recurse(coins, index, amount -coins[index], memo)

        const ifChoosing = coinChosen === Infinity ? Infinity : 1+coinChosen

        memo[key] = Math.min(coinNotChosen, ifChoosing)

        return memo[key]
    }

};