# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Easy

## Question

Merge two sorted linked lists and return it as a __sorted__ list. The list should be made by splicing together the nodes of the first two lists.

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;"/>

<pre>
<strong>Input:</strong> l1 = [1,2,4], l2 = [1,3,4]
<strong>Output:</strong> [1,1,2,3,4,4]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> l1 = [], l2 = []
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> l1 = [], l2 = [0]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

* The number of nodes in both lists is in the range `` [0, 50] ``.
* <code> -100 &lt;= Node.val &lt;= 100 </code>
* Both `` l1 `` and `` l2 `` are sorted in __non-decreasing__ order.

## Answer

本題為練習ListNode操作，直接比較 `l1`, `l2` 的值即可

若其中一個跑完了，`current_node.next = l1 or l2`

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current_node = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        current_node.next = l1 or l2
        return result.next

```
