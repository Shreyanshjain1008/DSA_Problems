class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(
                min(value, self.min_stack[-1])
            )
        """
        :type value: int
        :rtype: None
        """
        

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        if not self.stack:
            return -1
        return self.min_stack[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()