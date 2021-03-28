# [1. Two Sum](https://leetcode.com/problems/two-sum/) - Easy

## Question

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1:

```shell
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:

```shell
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:

```shell
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

* $2 \leq nums.length \leq 10^3$
* $-10^9 \leq nums[i] \leq 10^9$
* $-10^9 \leq target \leq 10^9$
* **Only one valid answer exists.**

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
