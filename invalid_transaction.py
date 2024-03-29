from typing import List
from collections import defaultdict


class Solution:
    def invalidTransaction(self, transactions: List[str]):
        res = []
        transaction = defaultdict(dict)

        for trans in transactions:
            name, time, amount, city = trans.split(",")

            time = int(time)
            if name not in transaction[time]:
                transaction[time][name] = {city, }
            else:
                transaction[time][name].add(city)

        for trans in transactions:
            name, time, amount, city = trans.split(",")
            time = int(time)
            if int(amount) > 1000:
                res.append(trans)
                continue
            for invalid_time in range(time - 60, time + 61):
                if invalid_time not in transaction:
                    continue
                if name not in transaction[invalid_time]:
                    continue

                if city not in transaction[invalid_time][name] or len(transaction[invalid_time][name]) > 1:
                    res.append(trans)

        return res


sol = Solution()
print(sol.invalidTransaction(["alice,20,800,mtv", "alice,50,100,beijing"]))
