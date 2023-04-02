from collections import defaultdict
import heapq


class Leaderboard:

    def __init__(self):
        self.board = defaultdict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0
        self.board[playerId] += score

    def top(self, K: int) -> int:
        values = [v for _, v in sorted(
            self.board.items(), key=lambda item: item[1])]
        values.sort(reverse=True)
        total, i, = 0, 0

        while i < K:
            total += values[i]
            i += 1
        return total

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0


class Leaderboard2:

    def __init__(self):
        self.board = defaultdict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0
        self.board[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for i in self.board.values():
            heapq.heappush(heap, i)

            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heap.pop()

        return res

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0


sol = Leaderboard2()
sol.addScore(2, 1)
sol.addScore(3, 2)
sol.addScore(4, 6)
sol.addScore(5, 9)
print(sol.top(3))
