/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //let lhsProduct = Array.from({length:nums.length}, ()=> 1) 
    let res = Array.from({length:nums.length}, ()=> 1) // storing rhs product
    let product = 1 
    // store lhs product in result array
    for (let i = 1; i<nums.length; i++){
        product = product * nums[i-1]
        res[i] = product
    }
    product = 1 
    // on the fly calculate rhs product and multiply it with the lhs product in res array
    for(let i = nums.length - 2; i>= 0; i--){
        product = product * nums[i+1]
        res[i] = res[i] * product
    }
    return res 
};

/*
givrn array nums 
return an array answer such tht answer[i] === product of all except nums[i]
ex: answer[0] = product of answer[1...n-1] answer[1] = answer[0] * answer[1] *..n-1
brute force: 
[1,2,3,4]
i = 0 run a loop where it keeps multiplying everyt index value except i == 0 
this way i = 0 ; inner loop j= 0 but only i !=j then multiply => 2 x 3 x 4  = 24
i = 1 inner loop j = 0 i!=j multiply 1 x 3 x 4  = 12
*/

