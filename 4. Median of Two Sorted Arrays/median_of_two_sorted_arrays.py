import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combination = nums1 + nums2
        combination.sort()
        if len(combination) % 2 == 0:
            median = (
                combination[int(len(combination) / 2 - 1)]
                + combination[int(len(combination) / 2)]
            ) / 2
            return median
        else:
            return float(combination[int((len(combination)) // 2)])


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
