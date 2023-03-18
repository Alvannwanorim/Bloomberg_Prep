from typing import List


class OrderedStream:
    def __init__(self, n: int) -> None:
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.stream[id] = value
        res = []

        if id == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1

            return res


sol = OrderedStream(5)
print(sol.insert(3, "cccc"))
print(sol.insert(1, "aaaaa"))
print(sol.insert(2, "bbbbb"))
print(sol.insert(5, "eeeee"))
print(sol.insert(4, "ddddd"))
