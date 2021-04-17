import sys

sys.path.append(".")
from model import *


class Solution:
    def reverse(self, x: int) -> int:
        input_data = str(x)
        if "-" not in input_data:
            # Directly reverse
            result = input_data[::-1]
        else:
            # Find number part
            number_part = input_data[1:]
            # -reverse_number
            result = f"-{number_part[::-1]}"
        result = int(result)
        if -(2 ** 31) < result < 2 ** 31 - 1:
            return result
        else:
            return 0


if __name__ == "__main__":
    x = 123
    answer = Solution().reverse(x=x)
    print(answer)
