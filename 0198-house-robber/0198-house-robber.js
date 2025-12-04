/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (!nums || nums.length <=0){
        return -1 

    }
    let memo = {}
    return robHouse (nums, 0)
    function robHouse(nums, index){
        const key = index
        if (key in memo){
            return memo[key]
        }

        if (index >= nums.length){
            return 0
        }

        const houseNotRobbed = robHouse(nums, index+1)

        const houseRobbed = nums[index] + robHouse(nums, index+2)

        const maxVal = Math.max(houseNotRobbed,houseRobbed )

        memo[key] = maxVal
        return maxVal

    }
};