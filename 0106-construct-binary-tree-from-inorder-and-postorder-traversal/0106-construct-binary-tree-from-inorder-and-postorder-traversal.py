# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):

        D = {}

        n = len(inorder)
        for i in range(n):
            D[inorder[i]] = i

        self.postidx = n-1

        
        def build(s, e):

            if s > e:
                return None
                
            rootval = postorder[self.postidx]
            self.postidx -= 1

            root = TreeNode(rootval)

            x = D[rootval]
            
            root.right = build(x+1, e)
            root.left = build(s, x-1)

            return root
        return build(0, n-1)
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        