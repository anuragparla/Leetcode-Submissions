class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        '''
        digit is an array of strings
        tgt is also a digit string
        eventhough they say its digit concatenation is string based
        if target and digit string array ele are equal, we cannot use that
        '''
        valid_pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        valid_pairs += 1
        return valid_pairs

