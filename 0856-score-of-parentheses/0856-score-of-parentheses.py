class Solution(object):
    def scoreOfParentheses(self, s):

        stack = [0]
        score = 0

        for i in s:

            if i =="(":
                stack.append(0)

            else:

                inner = stack.pop()
                stack[-1] += max(2*inner , 1)
        return stack[0]

        """
        :type s: str
        :rtype: int
        """
        