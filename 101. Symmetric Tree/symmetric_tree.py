import sys

sys.path.append(".")
from model import *


# Recursive method
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_symmetric_tree(left: TreeNode, right: TreeNode):
            # Both left and right are not None and have same value
            if left and right and left.val == right.val:
                return is_symmetric_tree(
                    left=left.left, right=right.right
                ) and is_symmetric_tree(left=left.right, right=right.left)
            else:
                return left == right

        return is_symmetric_tree(left=root.left, right=root.right)


if __name__ == "__main__":
    input_list = [1, 2, 2, 3, 4, 4, 3]
    root = list_to_treenode(data=input_list)
    answer = Solution().isSymmetric(root=root)
    print(answer)
