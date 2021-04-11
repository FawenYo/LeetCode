from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return (
                max(self.maxDepth(root=root.left), self.maxDepth(root=root.right)) + 1
            )
        else:
            return 0


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

    input_list = [3, 9, 20, null, null, 15, 7]
    root = list_to_treenode(data=input_list)
    answer = Solution().maxDepth(root=root)
    print(answer)
