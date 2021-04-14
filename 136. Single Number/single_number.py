from typing import List


# Simple method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        result = []
        for number in nums:
            if number not in seen:
                result.append(number)
            elif number in result:
                result.remove(number)
            seen[number] = 1
        return result[0]


# Sum method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        distinct_sum = sum(set(nums))
        return distinct_sum * 2 - sum(nums)


# XOR method
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR calculate

        a | b | a ^ b
        --|---|------
        0 | 0 | 0
        0 | 1 | 1
        1 | 0 | 1
        1 | 1 | 0

        a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        """
        result = 0
        for number in nums:
            result ^= number
        return result


if __name__ == "__main__":
    nums = [2, 2, 1, 3, 1, 3, 4]
    answer = Solution().singleNumber(nums=nums)
    print(answer)
