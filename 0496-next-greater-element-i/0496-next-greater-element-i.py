class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        First store the number and its index for elements in nums1
        result = [-1] * len(nums1)
        Use for loop to iterate over nums2 
        while stack not empty:
            if nums2[i] > top of stack:
                stack.pop()
                if stack.pop in dict
                result[dict[stack.pop val]] = nums2[i]
            elif nums2[i] in dict:
                stack.append(nums2[i])
        '''
        result = [-1] * len(nums1)
        dict_of_number_indices = {}
        monotonic_decreasing_stack = []

        for i in range(len(nums1)):
                dict_of_number_indices[nums1[i]] = i

        for i in range(len(nums2)):
            curr = nums2[i]
            while monotonic_decreasing_stack and curr > monotonic_decreasing_stack[-1]:
                value = monotonic_decreasing_stack.pop()
                index = dict_of_number_indices[value]
                result[index] = curr
            if curr in dict_of_number_indices:
                monotonic_decreasing_stack.append(curr)
        return result

                


        