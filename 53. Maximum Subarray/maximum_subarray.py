import sys

sys.path.append(".")
from model import *


# DP version
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


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    answer = Solution().maxSubArray(nums=nums)
    print(answer)
