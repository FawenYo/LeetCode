# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Easy

## Question

Given the `` root `` of a binary tree, return _its maximum depth_.

A binary tree's __maximum depth__&nbsp;is the number of nodes along the longest path from the root node down to the farthest leaf node.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;"/>

<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> 2
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> 0
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> 1
</pre>

&nbsp;

__Constraints:__

* The number of nodes in the tree is in the range <code>[0, 10<sup>4</sup>]</code>.
* <code> -100 &lt;= Node.val &lt;= 100 </code>

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
