# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Medium

## Question

Given an array of integers `` nums `` sorted in ascending order, find the starting and ending position of a given `` target `` value.

If `` target `` is not found in the array, return `` [-1, -1] ``.

You must&nbsp;write an algorithm with&nbsp;`` O(log n) `` runtime complexity.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 8
<strong>Output:</strong> [3,4]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [5,7,7,8,8,10], target = 6
<strong>Output:</strong> [-1,-1]
</pre>

__Example 3:__

<pre><strong>Input:</strong> nums = [], target = 0
<strong>Output:</strong> [-1,-1]
</pre>

&nbsp;

__Constraints:__

* <code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code>
* <code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code>
* `` nums `` is a non-decreasing array.
* <code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code>

## Answer

透過 binary search 方式即可解題

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            # Find target
            if nums[start] == nums[end] == target:
                return [start, end]

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[start] != target:
                    start += 1
                if nums[end] != target:
                    end -= 1
        # Didn't find target
        return [-1, -1]

```
