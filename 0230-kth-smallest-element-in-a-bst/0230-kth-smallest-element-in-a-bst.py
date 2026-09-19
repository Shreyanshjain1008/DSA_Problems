# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def Inorder(self, root, inorder):
        if root == None:
                return
        self.Inorder(root.left, inorder)
        inorder.append(root.val)
        self.Inorder(root.right, inorder)

    def kthSmallest(self, root, k):

        inorder = []
        self.Inorder(root, inorder)
        return inorder[k-1]

        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        