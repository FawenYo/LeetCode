import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        existing = {}
        for number in nums:
            if number in existing:
                return number
            else:
                existing[number] = 1
        return 0


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
