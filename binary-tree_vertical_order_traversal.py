from collections import defaultdict, deque
from typing import List, Optional


class NodeTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def traversal(self, root: Optional[NodeTree]) -> List[List[int]]:
        queue = deque([(root, 0)])
        left, right = 0, 0
        table = defaultdict(list)
        if not root:
            return []

        while queue:
            node, col = queue.popleft()

            table[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        left = min(table.keys())
        right = max(table.keys())
        res = []
        for col in range(left, right + 1):
            res.append(table[col])

        return res


node1 = NodeTree(1)
node2 = NodeTree(2, node1)
node3 = NodeTree(3, None, node2)

sol = Solution()
print(sol.traversal(node3))
