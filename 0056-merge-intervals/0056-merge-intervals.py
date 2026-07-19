class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start values
        intervals.sort(key=lambda intrvl:intrvl[0])
        merged = [intervals[0]]
        for start,end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],end)
            else:
                merged.append([start,end])
        return merged


        