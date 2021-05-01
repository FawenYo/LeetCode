# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Medium

## Question

Given an integer array `` nums `` and an integer `` k ``, return _the_ <code>k<sup>th</sup></code> _largest element in the array_.

Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>4</sup></code>
* <code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code>

## Answer

本題只需將 `nums` 進行排序，就可以找到答案

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

```
