# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/) - Easy

## Question

Roman numerals are represented by seven different symbols: $I$, $V$, $X$, $L$, $C$, $D$ and $M$.

| Symbol | Value  |
| ------ | ------ |
| $I$    | $1$    |
| $V$    | $5$    |
| $X$    | $10$   |
| $L$    | $50$   |
| $C$    | $100$  |
| $D$    | $500$  |
| $M$    | $1000$ |

For example, $2$ is written as $II$ in Roman numeral, just two one's added together. $12$ is written as $XII$, which is simply $X + II$. The number $27$ is written as $XXVII$, which is $XX + V + II$.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not $IIII$. Instead, the number four is written as $IV$. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as $IX$. There are six instances where subtraction is used:

* $I$ can be placed before $V$ (5) and $X$ (10) to make 4 and 9.
* $X$ can be placed before $L$ (50) and $C$ (100) to make 40 and 90.
* $C$ can be placed before $D$ (500) and $M$ (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Examples

### Example 1:

```shell
Input: s = "III"
Output: 3
```

### Example 2:

```shell
Input: s = "IV"
Output: 4
```

### Example 3:

```shell
Input: s = "IX"
Output: 9
```

### Example 4:

```shell
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

### Example 5:

```shell
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Constraints:

* $1 \leq s.length \leq 15$
* $s$ contains only the characters ('$I$', '$V$', '$X$', '$L$', '$C$', '$D$', '$M$')
* It is **guaranteed** that s is a valid roman numeral in the range $[1, 3999]$.

## Answer

字典對照，並記錄前一個字母

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        previous_character = ""

        for each_character in s:
            result += roman_map[each_character]

            # Special condition
            if (
                each_character == "V"
                and previous_character == "I"
                or each_character == "X"
                and previous_character == "I"
            ):
                result -= 2
            elif (
                each_character == "L"
                and previous_character == "X"
                or each_character == "C"
                and previous_character == "X"
            ):
                result -= 20
            elif (
                each_character == "D"
                and previous_character == "C"
                or each_character == "M"
                and previous_character == "C"
            ):
                result -= 200

            # Update previous character
            previous_character = each_character
        return result

```
