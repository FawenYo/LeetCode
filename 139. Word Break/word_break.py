import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # ex. ["", "l", "le", "lee", "leet", "leetc", "leetco", "leetcod", "leetcode"]
        dp = [True] + [False] * len(s)

        for index in range(1, len(s) + 1):

            for word in wordDict:
                if dp[index - len(word)] and s[:index].endswith(word):
                    dp[index] = True

        return dp[-1]


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
