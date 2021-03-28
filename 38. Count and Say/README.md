# [38. Count and Say](https://leetcode.com/problems/count-and-say/) - Medium

## Question

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

* $countAndSay(1) = "1"$
* $countAndSay(n)$ is the way you would "say" the digit string from $countAndSay(n-1)$, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the **minimal** number of groups so that each group is a contiguous section all of the **same character**. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string $"3322251"$:

![image](https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg)

Given a positive integer $n$, return the $n^{th}$ term of the **count-and-say** sequence.

## Examples

### Example 1:

```shell
Input: n = 1
Output: "1"
Explanation: This is the base case.
```

### Example 2:

```shell
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

## Constraints:

* $1 \leq n \leq 30$

## Answer

紀錄數字和其個數

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            result = "1"
            for _ in range(n - 1):
                temp = ""
                previous_number = result[0]
                number_count = 0

                for each_number in result:
                    # Same as previous number
                    if each_number == previous_number:
                        number_count += 1
                    else:
                        # Update temp
                        temp += f"{number_count}{previous_number}"
                        # Update previous_number and number_count
                        previous_number = each_number
                        number_count = 1
                # Update temp
                temp += f"{number_count}{previous_number}"
                result = temp
            return result

```
