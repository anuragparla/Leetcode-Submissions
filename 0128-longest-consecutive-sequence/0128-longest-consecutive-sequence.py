class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' goal is to find the max consec number sequence
        time complexity should be O(N)
        array is unsorted
        duplicates values are present
        t1: [ 1,1,1,100,2,3,10,4,5,11,12] max = 5 
        t2: = [] max = 0 
        t3 [1] max = 1 
        t4 [ -1,-2,-100,-3,-4,200,500] max = 4
        approach1: sorting can be used but time taken is O(NlogN) so can't do that
        approach2: since we have duplicates present we can use hash set to eliminate duplicates.
        iterate over the set
        if the element has no previous it marks the start of the sequence
        loop till n+1 not present and increment the seq_length.
        once loop exits calculate max_length
        else:
            move to next element
        if asked to return the sequence then whenever loop is terminated record the start and end values 
        finally return all the values in that range
        '''
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1
        non_duplicated_set = set(nums)
        start = 0
        end = 0
        seq_length = 0
        max_seq_length = 0
        for num in non_duplicated_set:
            if num-1 not in non_duplicated_set:
                start = num
                seq_length +=1
                while num+1 in non_duplicated_set:
                    seq_length +=1
                    num += 1 
                end = num
                max_seq_length = max (max_seq_length, seq_length)
                seq_length = 0 
            else:
                continue
        return max_seq_length

1,100,2,3,10,4,5,11,12



        