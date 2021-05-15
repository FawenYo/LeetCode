import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def countBits(self, num: int) -> List[int]:
        counter = [0]
        for i in range(1, num + 1):
            # >>: Bit-shifting, same as i // 2
            counter.append(counter[i >> 1] + i % 2)
        return counter


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
