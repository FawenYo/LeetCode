import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.current_min = float("inf")
        self.previous_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.current_min:
            self.previous_min.append(self.current_min)
            self.current_min = val

    def pop(self) -> None:
        if self.stack[-1] == self.current_min:
            self.current_min = self.previous_min.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    Check().run_code(solution=MinStack(), test_data_path=f"{folder_path}/test_data.txt")
