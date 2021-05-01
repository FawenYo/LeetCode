import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        num_set = set(nums)
        for number in range(1, len(nums) + 1):
            if number not in num_set:
                result.append(number)
        return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
