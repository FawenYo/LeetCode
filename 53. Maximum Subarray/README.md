# [53. Maximum Subarray](https://leetcode.com/problems/count-and-say/) - Easy

## Question

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Examples

### Example 1:

```shell
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

### Example 2:

```shell
Input: nums = [1]
Output: 1
```

### Example 3:

```shell
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Constraints:

* $1 \leq nums.length \leq 3 * 10^4$
* $-10^5 <= nums[i] <= 10^5$

**Follow up**: If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

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
