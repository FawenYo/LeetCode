from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            remain_value = target - value
            # Search if remain_value exists in remaining list
            if remain_value in nums[index + 1 :]:
                # +1 for remain
                remain_index = index + 1 + nums[index + 1 :].index(remain_value)
                return [index, remain_index]
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    answer = Solution().twoSum(nums=nums, target=target)
    print(answer)
