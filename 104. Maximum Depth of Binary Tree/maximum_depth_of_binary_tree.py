import sys

sys.path.append(".")
from model import *


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            # +1 for current node
            return (
                max(self.maxDepth(root=root.left), self.maxDepth(root=root.right)) + 1
            )
        else:
            return 0


if __name__ == "__main__":
    input_list = [3, 9, 20, null, null, 15, 7]
    root = list_to_treenode(data=input_list)
    answer = Solution().maxDepth(root=root)
    print(answer)
