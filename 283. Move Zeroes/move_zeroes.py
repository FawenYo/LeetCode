import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0 and nums[first] == 0:
                # Switch number
                nums[first], nums[second] = nums[second], nums[first]

            if nums[first] != 0:
                first += 1


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
