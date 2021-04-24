import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = self.dfs(nums=nums, path=[], result=[])
        return result

    def dfs(self, nums, path, result):
        # Deepest
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            # Except for current num
            new_nums = nums[:i] + nums[i + 1 :]
            # Add current num to path
            new_path = path + [nums[i]]
            self.dfs(nums=new_nums, path=new_path, result=result)
        return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
