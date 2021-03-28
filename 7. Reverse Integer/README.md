# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) - Easy

## Question

Given a signed 32-bit integer $x$, return $x$ with its digits reversed. If reversing $x$ causes the value to go outside the signed 32-bit integer range $[-2^{31}, 2^{31} - 1]$, then return $0$.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

## Examples

### Example 1:

```shell
Input: x = 123
Output: 321
```

### Example 2:

```shell
Input: x = -123
Output: -321
```

### Example 3:

```shell
Input: x = 120
Output: 21
```

### Example 4:

```shell
Input: x = 0
Output: 0
```

## Constraints:

* $-2^{31} \leq x \leq 2^{31} - 1$

## Answer

將 $x$ 轉為 string 後反轉

```python
class Solution:
    def reverse(self, x: int) -> int:
        input_data = str(x)
        if "-" not in input_data:
            # Directly reverse
            result = input_data[::-1]
        else:
            # Find number part
            number_part = input_data[1:]
            # -reverse_number
            result = f"-{number_part[::-1]}"
        result = int(result)
        if -(2 ** 31) < result < 2 ** 31 - 1:
            return result
        else:
            return 0

```
