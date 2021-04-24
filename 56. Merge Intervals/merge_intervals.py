import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        else:
            result = []

            intervals.sort()
            temp_start, temp_end = intervals[0]
            for start, end in intervals[1:]:
                if start <= temp_end:
                    temp_end = max(temp_end, end)
                else:
                    result.append([temp_start, temp_end])
                    temp_start = start
                    temp_end = end
            result.append([temp_start, temp_end])
            return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
