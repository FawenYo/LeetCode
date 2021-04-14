# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Easy

## Question

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

### Example 1:

![Example Image](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```shell
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:

```shell
Input: root = [1,null,2]
Output: 2
```

### Example 3:

```shell
Input: root = []
Output: 0
```

### Example 4:

```shell
Input: root = [0]
Output: 1
```

## Constraints:

* The number of nodes in the tree is in the range $[0, 10^4]$.
* $-100 \leq Node.val \leq 100$

## Answer

比較左右的深度，並加上當前節點層

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            # +1 for current node
            return (
                max(self.maxDepth(root=root.left), self.maxDepth(root=root.right)) + 1
            )
        else:
            return 0

```
