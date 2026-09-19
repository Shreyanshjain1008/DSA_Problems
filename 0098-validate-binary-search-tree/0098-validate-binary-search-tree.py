# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def validate(self, root, minimum, maximum):
        if root == None:
            return True

        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.validate(root.left, minimum, root.val) and self.validate(root.right, root.val, maximum)

    def isValidBST(self, root):
        return self.validate(root , float('-inf'), float('inf'))
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        