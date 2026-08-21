
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        inorder=[]
        def inord(root, inorder):
            if root == None:
                return
            
            inord(root.left,inorder)
            inorder.append(root.val)
            inord(root.right,inorder)
        inord(root, inorder)
        return inorder

        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        