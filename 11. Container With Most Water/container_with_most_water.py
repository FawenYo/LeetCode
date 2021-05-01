import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        first_point = 0
        last_point = len(height) - 1
        while first_point != last_point:
            if height[first_point] > height[last_point]:
                temp = height[last_point] * (last_point - first_point)
                if temp > result:
                    result = temp
                # Move last point inward
                last_point -= 1
            else:
                temp = height[first_point] * (last_point - first_point)
                if temp > result:
                    result = temp
                # Move first point inward
                first_point += 1
        return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
