class Solution:
    def adjacentDuplicates(self, s: str, k: int) -> str:
        res = ""
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

            if stack[-1][1] == k:
                stack.pop()

        for char, count in stack:
            res += char * count

        return res


sol = Solution()
print(sol.adjacentDuplicates("wheere", 2))
print(sol.adjacentDuplicates("deeedbbcccbdaa", 2))
