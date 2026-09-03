class MyQueue(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        s1=[]
        while self.stack:
            s1.append(self.stack.pop())
        self.stack.append(x)
        while s1:
            self.stack.append(s1.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()