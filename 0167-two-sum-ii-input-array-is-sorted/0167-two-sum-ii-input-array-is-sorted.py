class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []
        while left != right:
            sum_of_two_numbers = numbers[left] + numbers[right]
            if sum_of_two_numbers == target:
                result.append(left +1)
                result.append(right +1)
                return result
            elif sum_of_two_numbers > target:
                right -= 1 
            else:
                left += 1
        
        
    