# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def postorderTraversal(self, root):
        postorder = []
        def post(root,postorder):
            if root == None:
                return None

            post(root.left,postorder)
            post(root.right,postorder)
            postorder.append(root.val)
        post(root, postorder)    
        return postorder
        
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        