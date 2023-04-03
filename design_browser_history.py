class TreeNode:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = TreeNode(homepage)

    def visit(self, url: str) -> None:
        node = TreeNode(url)
        curr = self.root
        curr.next = node
        node.prev = curr
        self.root = node

    def back(self, steps: int) -> str:
        while steps and self.root.prev:
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while steps and self.root.next:
            self.root = self.root.next
            steps += 1
        return self.root.val


sol = BrowserHistory("leetcode.com")
print(sol.visit("google.com"))
print(sol.visit("facebook.com"))
print(sol.visit("youtube.com"))
print(sol.back(1))
print(sol.back(1))
print(sol.back(1))
print(sol.forward(1))
print(sol.visit("linkedin.com"))
print(sol.forward(2))
print(sol.back(2))
print(sol.back(7))
