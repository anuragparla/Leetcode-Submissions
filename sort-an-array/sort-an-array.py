class Solution(object):

    
    def merge_sort(self, left_list, right_list):
        # lp=0
        # rp=0
        # tempList = []
        # print(left)
        # while lp<len(list(left)) and rp<len(list(right)):
        #     if left[lp] < right[rp]:
        #         tempList.append(left[lp])
        #         lp +=1
        #     else:
        #         tempList.append(right[lp])
        #         rp +=1

        #     tempList.extend(left[lp:])
        #     tempList.extend(right[rp:])
        # return tempList     
        left_cursor = right_cursor = 0
        ret = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1
        
        # append what is remained in either of the lists
        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])
    
        return ret
        
        

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if len(nums) == 0 or len(nums) == 1:
        #     return nums
        # length = int (len(nums)/2)
        # left = merge(nums[:length])
        # right = merge(nums[length:])
        # print(type(left))
        # print(type(right))
        # return self.merge_sort(left,right)
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = self.sortArray(nums[0:pivot])
        right_list = self.sortArray(nums[pivot:])
        return self.merge_sort(left_list, right_list)