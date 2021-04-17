import sys

sys.path.append(".")
from model import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # Sort list first
        nums.sort()

        for first_index, first_num in enumerate(nums):
            # Bypass if first_num is same with previous num
            if first_index >= 1 and first_num == nums[first_index - 1]:
                continue
            # Key point: find in dictionary has far BETTER performance than list
            remain = {}
            for second_num in nums[first_index + 1 :]:
                if second_num in remain:
                    # Found answer
                    result.add(
                        tuple(sorted((first_num, second_num, -first_num - second_num)))
                    )
                else:
                    remain[-first_num - second_num] = 1
        return sorted(result)


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    answer = Solution().threeSum(nums=nums)
    print(answer)
