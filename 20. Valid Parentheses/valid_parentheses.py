import sys

sys.path.append(".")
from model import *


# Solution 1
class Solution:
    def isValid(self, s: str = "{[]}") -> bool:
        # Remove all "()", "[]" and "{}" in s
        while ("()" in s) or ("[]" in s) or ("{}" in s):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        if not s:
            return True
        else:
            return False


# Solution 2
class Solution:
    def isValid(self, s: str = "{[]}") -> bool:
        pair_map = {"(": ")", "[": "]", "{": "}"}
        pending = ""

        # s must be multiples of 2
        if len(s) % 2 == 0:
            for character in s:
                # Parentheses start
                if character in pair_map:
                    pending += character
                else:
                    if not pending:
                        return False

                    # Find last pending symbol
                    last_pair = pair_map[pending[-1]]
                    if last_pair == character:
                        pending = pending[:-1]
                    else:
                        return False
            if not pending:
                return True
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    s = "()"
    answer = Solution().isValid(s=s)
    print(answer)
