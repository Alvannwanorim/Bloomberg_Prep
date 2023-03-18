from typing import List


class Solution:
    def twoCityScheduling(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[1]-x[0])
        res = 0
        # print(costs[:len(costs)//2])
        # print(costs[len(costs)//2:])
        for c in costs[len(costs)//2:]:
            res += c[0]

        for c in costs[:len(costs)//2]:
            res += c[1]

        return res


sol = Solution()
print(sol.twoCityScheduling([[10, 20], [30, 200], [400, 50], [30, 20]]))
print(sol.twoCityScheduling([[259, 770], [448, 54], [
      926, 667], [184, 139], [840, 118], [577, 469]]))
