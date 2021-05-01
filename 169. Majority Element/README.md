# [169. Majority Element](https://leetcode.com/problems/majority-element/) - Easy

## Question

Given an array `` nums `` of size `` n ``, return _the majority element_.

The majority element is the element that appears more than `` ⌊n / 2⌋ `` times. You may assume that the majority element always exists in the array.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> 3
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>

&nbsp;

__Constraints:__

* `` n == nums.length ``
* <code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code>
* <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>

&nbsp;
__Follow-up:__ Could you solve the problem in linear time and in `` O(1) `` space?

## Answer

本題題目中提到`more than ⌊n / 2⌋ times`，故只要先將 `nums` 做排序後取中間位數的數值便是答案，使用 `n//2` 以避免奇數除不盡的問題。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

```
