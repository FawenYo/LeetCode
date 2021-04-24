import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = 0
            previous = 1
            current = 2
            for _ in range(n - 2):
                result = previous + current
                previous = current
                current = result
            return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
