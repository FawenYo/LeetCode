# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Easy

## Question

Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.

## Examples

### Example 1:

![Example1 image](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```shell
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:

```shell
Input: l1 = [], l2 = []
Output: []
```

### Example 3:

```shell
Input: l1 = [], l2 = [0]
Output: [0]
```

## Constraints:

* The number of nodes in both lists is in the range `[0, 50]`.
* $-100 \leq Node.val \leq 100$.
* Both `l1` and `l2` are sorted in non-decreasing order.

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
