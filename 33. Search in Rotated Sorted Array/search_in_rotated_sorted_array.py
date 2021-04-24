import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
