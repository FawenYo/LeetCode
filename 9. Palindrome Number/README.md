# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) - Easy

## Question

Given an integer $x$, return true if $x$ is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, $121$ is palindrome while $123$ is not.

## Examples

### Example 1:

```shell
Input: x = 121
Output: true
```

### Example 2:

```shell
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:

```shell
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Example 4:

```shell
Input: x = -101
Output: false
```

## Constraints:

* $-2^{31} \leq x \leq 2^{31} - 1$

**Follow up**: Could you solve it without converting the integer to a string?

## Answer

With string: 反轉 $x$ 並比對是否相同

Without string: 透過餘數抓最後一個數值，反轉後比對是否相同

```python
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

```
