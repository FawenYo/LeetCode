# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Medium

## Question

Given the `` head `` of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.

__Follow up:__&nbsp;Could you do this in one pass?

&nbsp;

__Example 1:__

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;"/>

<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

&nbsp;

__Constraints:__

* The number of nodes in the list is `` sz ``.
* <code> 1 &lt;= sz &lt;= 30 </code>
* <code> 0 &lt;= Node.val &lt;= 100 </code>
* <code> 1 &lt;= n &lt;= sz </code>

## Answer

分別建立 `before` 和 `after` 兩個ListNode，`after`先跑n步，當`after`跑到底的時候，`before.next`就是要移除的Node。

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        after = before = head
        # After = start from nth
        for _ in range(n):
            after = after.next
        if not after:
            return head.next
        # Got last nth when after ended
        while after.next:
            after = after.next
            before = before.next

        before.next = before.next.next
        return head

```
