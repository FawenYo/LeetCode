# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) - Easy

## Question

Given the `` root `` of a binary tree, _check whether it is a mirror of itself_ (i.e., symmetric around its center).

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;"/>

<pre>
<strong>Input:</strong> root = [1,2,2,3,4,4,3]
<strong>Output:</strong> true
</pre>

__Example 2:__

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;"/>

<pre>
<strong>Input:</strong> root = [1,2,2,null,3,null,3]
<strong>Output:</strong> false
</pre>

&nbsp;

__Constraints:__

* The number of nodes in the tree is in the range `` [1, 1000] ``.
* <code> -100 &lt;= Node.val &lt;= 100 </code>

&nbsp;
__Follow up:__ Could you solve it both recursively and iteratively?

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
