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

    def build(self, arr, s, e):
        if s > e:
            return None
        
        mid = (s + e) // 2
        root = TreeNode(arr[mid])
        root.left = self.build(arr, s, mid-1)
        root.right = self.build(arr, mid+1, e)
        return root

    def balanceBST(self, root):
        
        inorder = []
        self.Inorder(root, inorder)
        return self.build(inorder, 0, len(inorder)-1)

        
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        