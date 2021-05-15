import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            # Update Profit
            if profit > result:
                result = profit

            # Update Min Price
            if price < min_price:
                min_price = price
        return result


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
