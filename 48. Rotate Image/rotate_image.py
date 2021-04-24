import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the Matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(len(matrix)):
            row_length = len(matrix[i]) - 1
            for j in range(row_length):
                if j * 2 > row_length:
                    break
                matrix[i][j], matrix[i][row_length - j] = (
                    matrix[i][row_length - j],
                    matrix[i][j],
                )


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
