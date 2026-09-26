class MinStack:

    def __init__(self):
        self.stack=[]
        self.Min=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.Min:
            self.Min.append(val)
        else:
            if self.Min[-1]>=val:
                self.Min.append(val)

    def pop(self) -> None:
        
        if self.Min[-1]==self.stack.pop():
            self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min[-1]
