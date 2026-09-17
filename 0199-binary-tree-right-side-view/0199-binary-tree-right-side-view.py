# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return []
        
        q = deque([root])
        ans = []
        while q:
            level = []
            n = len(q)
            for i in range(1,n+1):
                node = q.popleft()
                if i == n:
                        ans.append(node.val)
                if node.left:
                        q.append(node.left)
                if node.right:
                        q.append(node.right)
        return ans
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        