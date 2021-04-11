# [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) - Medium

## Question

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if **two directly-linked houses were broken into on the same night**.

Given the `root` of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

## Examples

### Example 1:

![Example Image](https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg)

```shell
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

### Example 2:

![Example Image](https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg)

```shell
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```

## Constraints:

* The number of nodes in the tree is in the range $[0, 10^4]$.
* $0 \leq Node.val \leq 10^4$

## Answer

(待補齊)

```python
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

```
