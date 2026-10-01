class Solution(object):
    def isValid(self, s):

        valid_seq = {')' : '(' ,  ']' : '[' , '}' : '{'}
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in valid_seq:
                if not stack or valid_seq[i] != stack[-1]:
                    return False

                stack.pop()
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        