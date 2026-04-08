class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.minSt or val <= self.minSt[-1]:
            self.minSt.append(val)

    def pop(self) -> None:
        if not self.st:
            return None

        ans = self.st[-1]
        self.st.pop()

        if self.minSt[-1] == ans:
            self.minSt.pop()

        return ans

    def top(self) -> int:
        if not self.st:
            return None
        return self.st[-1]

    def getMin(self) -> int:
        if not self.minSt:
            return None
        return self.minSt[-1]