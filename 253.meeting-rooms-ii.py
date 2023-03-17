from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        L = len(intervals)
        ans = 0
        now_reserve = 0
        stack = []

        for interval in intervals:
            stack.append([interval[0], 1])
            stack.append([interval[1], -1])
        
        stack = sorted(stack)
        sorted_stack = deque(stack)

        while sorted_stack:
            pros = sorted_stack.popleft()
            now_reserve += pros[1]
            ans = max(ans, now_reserve)

        return ans 
        
        
