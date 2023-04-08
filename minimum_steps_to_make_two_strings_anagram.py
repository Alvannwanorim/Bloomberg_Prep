from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mapS = Counter(s)
        mapT = Counter(t)

        res = 0
        for char in mapS:

            if mapS[char] - mapT[char] >= 0:
                res += 1

        return res


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        mapS = {}

        for c in s:
            mapS[c] = 1 + mapS.get(c, 0)

        res = 0

        for c in t:
            if c in mapS and mapS[c] > 0:
                mapS[c] -= 1
            else:
                res += 1
        return res


sol = Solution()
print(sol.minSteps("bab", "aba"))
print(sol.minSteps("leetcode", "practice"))
