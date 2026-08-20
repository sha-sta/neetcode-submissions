class MinStack:

    def __init__(self):
        self.mins = []
        self.vals = []

    def push(self, val: int) -> None:
        self.vals.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.vals.pop() == self.mins[-1]:
            self.mins.pop()
        

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.mins[-1]
