class MinStack:

    def __init__(self):
        self.s = []
        self.mn = float('inf')

    def push(self, val: int) -> None:
        self.s.append(val)
        self.mn = min(self.mn, val)

    def pop(self) -> None:
        p = self.s.pop()
        if p == self.mn:
            self.mn = min(self.s) if self.s else float('inf')

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mn