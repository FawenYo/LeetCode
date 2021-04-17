# [53. Maximum Subarray](https://leetcode.com/problems/count-and-say/) - Easy

## Question

Given an integer array `` nums ``, find the contiguous subarray (containing at least one number) which has the largest sum and return _its sum_.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code>
* <code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code>

&nbsp;
__Follow up:__ If you have figured out the `` O(n) `` solution, try coding another solution using the __divide and conquer__ approach, which is more subtle.

## Answer

DP (動態規劃)：`result` = `current_sum` = 0，遍歷 `nums` 的過程，如前面 `current_sum` 為負數，則重設 `current_sum = i`，並更新result

Divide-and-Conquer (分治法)：[教學](devide-and-conquer.md)

```python
# DP version｀
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Prevent nums are all negative
        result = current_sum = nums[0]
        for num in nums[1:]:
            # Reset current_sum if before (current_sum) is negative
            current_sum = max(current_sum + num, num)
            result = max(current_sum, result)
        return result


# Divide-and-Conquer version
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Base case
        if len(nums) == 1:
            return nums[0]
        else:
            mid = len(nums) // 2
            left_sum = self.maxSubArray(nums=nums[:mid])
            right_sum = self.maxSubArray(nums=nums[mid:])
            cross_sum = self.max_crossing_subarray(nums=nums, mid=mid)
            return max(left_sum, right_sum, cross_sum)

    def max_crossing_subarray(self, nums: List[int], mid: int) -> float:
        # Left side
        left_sum = -float("inf")
        current_sum = 0
        for i in nums[mid - 1 :: -1]:
            current_sum += i
            left_sum = max(current_sum, left_sum)

        # Right side
        right_sum = -float("inf")
        current_sum = 0
        for j in nums[mid::]:
            current_sum += j
            right_sum = max(current_sum, right_sum)

        # Return left + right
        return left_sum + right_sum

```
