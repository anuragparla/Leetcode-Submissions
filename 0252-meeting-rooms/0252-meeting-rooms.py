class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals:
            intervals.sort(key=lambda intrvl:intrvl[0])
        else:
            return True
        if len(intervals) == 1:
            return True
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
