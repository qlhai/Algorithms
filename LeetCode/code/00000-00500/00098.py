# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        if not root:
            return True
        return dfs(root, float('-inf'), float('inf'))
