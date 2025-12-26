/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let lhsProduct = Array.from({length:nums.length}, ()=> 1)
    let rhsProduct = Array.from({length:nums.length}, ()=> 1)
    let product = 1 
    let res = []
    for (let i = 1; i<nums.length; i++){
        product = product * nums[i-1]
        lhsProduct[i] = product
    }
    product = 1 
    for(let i = nums.length - 2; i>= 0; i--){
        product = product * nums[i+1]
        rhsProduct[i] = product
    }

    for(let k = 0; k<nums.length; k++) {
        res[k] = lhsProduct[k] * rhsProduct[k];
    }

    return res
    // lhs = [1,1,2,6]
    // rhs = [24, 12, 4,1]

    
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

