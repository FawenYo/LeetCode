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
