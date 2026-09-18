# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def buildTree(self, preorder, inorder):
        self.preidx = 0
        D = {}

        n = len(inorder)
        for i in range(n):
            D[inorder[i]] = i

        
        def build(s, e):

            if s > e:
                return None
            rootval = preorder[self.preidx]
            self.preidx += 1

            root = TreeNode(rootval)

            x = D[rootval]

            root.left = build(s, x-1)
            root.right = build(x+1, e)

            return root
        return build(0, n-1)
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        