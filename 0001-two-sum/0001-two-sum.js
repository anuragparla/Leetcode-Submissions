/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    let mapNumberToIndices = new Map()
    for (let i = 0; i<nums.length; i++){
        let diff = target - nums[i]
        if (mapNumberToIndices.has(diff)) {
            return [i,mapNumberToIndices.get(diff) ]
        }
        else {
            mapNumberToIndices.set(nums[i],i)
        }
    }
    
};

