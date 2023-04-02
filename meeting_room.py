from typing import List


class Solution:
    def meetingRoom(self, intervals: List[List[int]]) -> int:
        """
        [[0,30],[5,25],[15,20]]
        [0,5,15]
        [20,25,30]
        [[0,30],[5,10],[15,20]]
        [0,5,15]
        [10,20,30]
        """
        start = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)
        s, e = 0, 0
        count, res = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
        res = max(res, count)
        return res


sol = Solution()
print(sol.meetingRoom([[0, 30], [5, 10], [15, 20]]))
print(sol.meetingRoom([[0, 30], [5, 25], [15, 20]]))
