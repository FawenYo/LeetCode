# With string version
class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_data = str(x)
        return input_data[::-1] == input_data


# Without string version
class Solution:
    def isPalindrome(self, x: int) -> bool:
        origin = x
        reverse = 0
        if x < 0:
            return False
        else:
            while x > 0:
                last_number = x % 10
                reverse = reverse * 10 + last_number
                x = x // 10
            if origin == reverse:
                return True
            else:
                return False


if __name__ == "__main__":
    x = 121
    answer = Solution().isPalindrome(x=x)
    print(x)
