# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self, root, d):
        if root == None:
            return 0
        lh = self.height(root.left,d)
        rh = self.height(root.right,d)
        d[0] = max( d[0], lh+rh+1)
        return 1 + max(lh , rh)

    def diameterOfBinaryTree(self, root):
        d = [0]
        self.height(root,d)
        return d[0] - 1
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        