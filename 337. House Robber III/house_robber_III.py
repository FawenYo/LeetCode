from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    null = None

    def list_to_treenode(data: List[int], index: int = 0) -> Optional[TreeNode]:
        result = None
        if index < len(data):
            if data[index] is not None:
                result = TreeNode(data[index])
                result.left = list_to_treenode(data, 2 * index + 1)
                result.right = list_to_treenode(data, 2 * index + 2)
            else:
                return None
        return result

    input_list = [3, 2, 3, null, 3, null, 1]
    root = list_to_treenode(data=input_list)
    answer = Solution().rob(root=root)
    print(answer)
