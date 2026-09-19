# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, tree):

        def height(root):
            if root == None:
                return 0

            lh = height(root.left)
            if lh == -1:
                return -1
            rh = height(root.right)
            if rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1
            
            return max(lh,rh) + 1
        return height(tree) != -1
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        