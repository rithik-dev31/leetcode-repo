# Last updated: 8/12/2026, 11:31:53 AM
class MinStack:

    def __init__(self):

        self.stack=[]
        self.minstack=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if len(self.minstack)==0 or value<=self.minstack[-1]:
            self.minstack.append(value)

    def pop(self) -> None:
        
        if self.stack[-1]==self.minstack[-1]:
            self.minstack.pop()
        
        self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()