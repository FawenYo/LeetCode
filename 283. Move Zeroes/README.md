# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) - Easy

## Question

Given an integer array `` nums ``, move all `` 0 ``'s to the end of it while maintaining the relative order of the non-zero elements.

__Note__ that you must do this in-place without making a copy of the array.

&nbsp;

__Example 1:__

<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre>

__Example 2:__

<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code>
* <code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code>

&nbsp;
__Follow up:__ Could you minimize the total number of operations done?

## Answer

需要移動的情況是 `first` 為 0 而 `second` 不為0 的情況

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0 and nums[first] == 0:
                # Switch number
                nums[first], nums[second] = nums[second], nums[first]

            if nums[first] != 0:
                first += 1

```
