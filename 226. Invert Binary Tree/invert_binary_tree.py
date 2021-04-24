import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            result = TreeNode(val=root.val)
            result.left = self.invertTree(root=root.right)
            result.right = self.invertTree(root=root.left)
            return result
        else:
            return root


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
