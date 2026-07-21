class Solution:

    

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #handle empty list
        if not intervals:
            return [newInterval]
        merged = []
        idx = 1
        # if the newInterval has the smallest start value
        if newInterval[0] < intervals[0][0]:
            merged = [newInterval]
            idx = 0
        else:
            merged = [intervals[0]]

        # adding all the intervals up unit new interval
        while idx < len(intervals) and intervals[idx][0] <= newInterval[0]:
            self.merge(idx,intervals,merged)
            idx += 1 
        # adding new interval to the result
        if newInterval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1],newInterval[1])
        else:
            merged.append(newInterval)
        
        # add the remaining portion of the intervals to the  result 
        
        while idx < len(intervals):
            self.merge(idx,intervals,merged)
            idx += 1 
        
        return merged
    
    def merge(self,idx,intervals,merged):
        #check for overlap and merge
        if intervals[idx][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[idx][1])
        else:
            merged.append(intervals[idx])



        



        