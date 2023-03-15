from collections import defaultdict
import random


class RandomizedCollection:
    def __init__(self) -> None:
        self.numList = []
        self.hashMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = val in self.hashMap
        indx = len(self.numList)
        self.numList.append(val)
        self.hashMap[val].add(indx)
        return res

    def remove(self, val: int) -> bool:
        if not self.hashMap[val]:
            return False
        index = self.hashMap[val]
        last_val = self.numList[-1]
        self.numList[index] = last_val
        self.hashMap[last_val].add(index)
        self.hashMap[last_val].remove(len(self.numList))

        if (len(self.hashMap[val]) == 0):
            del self.hashMap[val]

        self.numList.pop()
        return True

    def grtRandom(self) -> int:
        return random.choice(self.numList)
