import sys

sys.path.append(".")
from model import *


class Solution:
    def rob(self, root: TreeNode) -> int:
        def result(node: TreeNode) -> Tuple[int, int]:
            if node:
                with_left, without_left = result(node=node.left)
                with_right, without_right = result(node=node.right)
                # If rob first
                rob_first = node.val + without_left + without_right
                # If skip first
                skip_first = max(with_left, without_left) + max(
                    with_right, without_right
                )
                return rob_first, skip_first
            else:
                return 0, 0

        return max(result(node=root))


if __name__ == "__main__":
    input_list = [3, 2, 3, null, 3, null, 1]
    root = list_to_treenode(data=input_list)
    answer = Solution().rob(root=root)
    print(answer)
