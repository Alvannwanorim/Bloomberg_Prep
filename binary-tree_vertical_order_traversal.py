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

        while queue:
            node, col = queue.popleft()

            if node is not None:
                table[col].append(node.val)
                left = min(left, col)
                right = max(right, col)
                queue.append((node.right, col + 1))
                queue.append((node.left, col - 1))

        return [table[x] for x in range(left, right + 1)]


node1 = NodeTree(1)
node2 = NodeTree(2, node1)
node3 = NodeTree(3, None, node2)

sol = Solution()
print(sol.traversal(node3))
