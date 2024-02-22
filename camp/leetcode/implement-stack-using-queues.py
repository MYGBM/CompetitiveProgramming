class MyStack:

    def __init__(self):
        self.stack = deque([])

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        i =0
        while i <len(self.stack)-1:
            temp = self.stack.popleft()
            self.stack.append(temp)
            i+=1
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]
        
    def empty(self) -> bool:
        if self.stack:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()