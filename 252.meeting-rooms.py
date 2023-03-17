class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)
        L = len(intervals)
        for i in range(L-1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                return False
        return True
