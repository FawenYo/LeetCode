# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Medium

## Question

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

### Example 1:

```shell
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

### Example 2:

```shell
Input: s = "cbbd"
Output: "bb"
```

### Example 3:

```shell
Input: s = "a"
Output: "a"
```

### Example 4:

```shell
Input: s = "ac"
Output: "a"
```

## Constraints

* $1 \leq s.length \leq 1000$
* $s$ consist of only digits and English letters (lower-case and/or upper-case).

## Answer

以 Question.3 基礎做修改，若遇到曾出現過的字就檢查是否為回文

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        used_characters = {}
        longest_string = s[0]
        for character_index, character in enumerate(s):
            # Character has already appeared in string
            if character in used_characters:
                used_characters[character].append(character_index)
                for history_index in used_characters[character]:
                    sub_string = s[history_index : character_index + 1]
                    if sub_string == sub_string[::-1]:
                        longest_string = max(sub_string, longest_string, key=len)
                        break
            else:
                # Record character's index
                used_characters[character] = [character_index]
        return longest_string

```
