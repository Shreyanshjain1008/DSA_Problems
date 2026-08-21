# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        preorder=[]
        def pre(root, preorder):
            if root == None:
                return
            preorder.append(root.val)
            pre(root.left,preorder)
            pre(root.right,preorder)
        pre(root, preorder)
        return preorder

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        