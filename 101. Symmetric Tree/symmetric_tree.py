from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    input_list = [1, 2, 2, 3, 4, 4, 3]
    root = list_to_treenode(data=input_list)
    answer = Solution().isSymmetric(root=root)
    print(answer)
