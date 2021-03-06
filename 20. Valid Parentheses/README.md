# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Easy

## Question

Given a string `` s `` containing just the characters `` '(' ``, `` ')' ``, `` '{' ``, `` '}' ``, `` '[' `` and `` ']' ``, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "()[]{}"
<strong>Output:</strong> true
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "(]"
<strong>Output:</strong> false
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = "([)]"
<strong>Output:</strong> false
</pre>

__Example 5:__

<pre>
<strong>Input:</strong> s = "{[]}"
<strong>Output:</strong> true
</pre>

&nbsp;

__Constraints:__

* <code>1 &lt;= s.length &lt;= 10<sup>4</sup></code>
* `` s `` consists of parentheses only `` '()[]{}' ``.

## Answer

Solution 1: 移除 `"()", "[]", "{}"` 後檢查是否為空

Solution 2: 出現關閉括號時檢查是否和前一個相配

```python
# Solution 1
class Solution:
    def isValid(self, s: str = "{[]}") -> bool:
        # Remove all "()", "[]" and "{}" in s
        while ("()" in s) or ("[]" in s) or ("{}" in s):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        if not s:
            return True
        else:
            return False


# Solution 2
class Solution:
    def isValid(self, s: str = "{[]}") -> bool:
        pair_map = {"(": ")", "[": "]", "{": "}"}
        pending = ""

        # s must be multiples of 2
        if len(s) % 2 == 0:
            for character in s:
                # Parentheses start
                if character in pair_map:
                    pending += character
                else:
                    if not pending:
                        return False

                    # Find last pending symbol
                    last_pair = pair_map[pending[-1]]
                    if last_pair == character:
                        pending = pending[:-1]
                    else:
                        return False
            if not pending:
                return True
            else:
                return False
        else:
            return False

```
