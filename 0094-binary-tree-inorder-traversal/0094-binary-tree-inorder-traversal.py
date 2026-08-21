# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        preorder=[]
        def pre(root, preorder):
            if root == None:
                return
            
            pre(root.left,preorder)
            preorder.append(root.val)
            pre(root.right,preorder)
        pre(root, preorder)
        return preorder

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        