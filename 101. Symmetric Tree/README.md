# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - Easy

## Question

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Examples

### Example 1:

![Example Image](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```shell
Input: root = [1,2,2,3,4,4,3]
Output: true
```

### Example 2:

![Example Image](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```shell
Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Constraints:

* The number of nodes in the tree is in the range $[1, 1000]$.
* $-100 \leq Node.val \leq 100$

**Follow up**: Could you solve it both recursively and iteratively?

## Answer

Iteration (迭代): 迴圈重複執行

Recursive (遞迴): 重複呼叫 function

此處使用遞迴方式，檢查左右是否相同

```python
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

```
