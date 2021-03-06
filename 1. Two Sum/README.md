# [1. Two Sum](https://leetcode.com/problems/two-sum/) - Easy

## Question

Given an array of integers `` nums ``&nbsp;and an integer `` target ``, return _indices of the two numbers such that they add up to `` target ``_.

You may assume that each input would have ___exactly_ one solution__, and you may not use the _same_ element twice.

You can return the answer in any order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Output:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

&nbsp;

__Constraints:__

* <code>2 &lt;= nums.length &lt;= 10<sup>3</sup></code>
* <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>
* <code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code>
* __Only one valid answer exists.__

## Answer

遍歷 $nums$，看殘值是否存在於 $nums$ 中，

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            remain_value = target - value
            # Search if remain_value exist in remaining list
            if remain_value in nums[index + 1 :]:
                # +1 for remain
                remain_index = index + 1 + nums[index + 1 :].index(remain_value)
                return [index, remain_index]
        return []

```
