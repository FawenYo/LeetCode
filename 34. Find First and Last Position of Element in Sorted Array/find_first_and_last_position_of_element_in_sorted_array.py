import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # Find target
            if nums[start] == nums[end] == target:
                return [start, end]

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[start] != target:
                    start += 1
                if nums[end] != target:
                    end -= 1
        # Didn't find target
        return [-1, -1]


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
