class Solution(object):
    def evalRPN(self, arr):
        stack = []
        for i in arr:
            if i == '+':
                r=stack.pop()
                l=stack.pop()
                stack.append(l+r)
            elif i == '-':
                r=stack.pop()
                l=stack.pop()
                stack.append(l-r)
            elif i == '*':
                r=stack.pop()
                l=stack.pop()
                stack.append(l*r)
            elif i == '/':
                r=stack.pop()
                l=stack.pop()
                if l * r < 0:
                    stack.append(-(abs(l) // abs(r)))
                else:
                    stack.append(abs(l) // abs(r))
            else:
                stack.append(int(i))
        return stack.pop()
        """
        :type tokens: List[str]
        :rtype: int
        """
        