import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def decodeString(self, s: str) -> str:
        repeat_times = 0
        string = ""
        memory = []
        for character in s:
            # Repeat times
            if character.isdigit():
                repeat_times = repeat_times * 10 + int(character)
            # Sub string start
            elif character == "[":
                # Move repeat times & current string into memory
                memory.append(repeat_times)
                memory.append(string)
                string = ""
                repeat_times = 0
            elif character.isalpha():
                string += character
            # Sub string end
            elif character == "]":
                previous_string = memory.pop()
                previous_times = memory.pop()
                string = previous_string + previous_times * string
        return string


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
