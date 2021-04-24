import pathlib
import sys

folder_path = str(pathlib.Path(__file__).parent.absolute())

sys.path.append(".")
from check import Check
from model import *


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # Both are not None
        if root1 and root2:
            # Current node
            root = TreeNode(val=root1.val + root2.val)
            # Left node
            root.left = self.mergeTrees(root1=root1.left, root2=root2.left)
            # Right node
            root.right = self.mergeTrees(root1=root1.right, root2=root2.right)
            return root
        else:
            return root1 or root2


if __name__ == "__main__":
    Check().run_code(solution=Solution(), test_data_path=f"{folder_path}/test_data.txt")
