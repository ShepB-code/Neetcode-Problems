# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root and root.left:
            self.invertTree(root.left)
        if root and root.right:
            self.invertTree(root.right)

        if root:
            root.left, root.right = root.right, root.left
            
        return root