# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium

## Question

Given a string `s`, find the length of the **longest substring** without repeating characters.

## Examples

### Example 1:

```shell
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:

```shell
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:

```shell
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Example 4:

```shell
Input: s = ""
Output: 0
```

## Constraints

* $0 \leq s.length \leq 5 * 10^4$
* $s$ consists of English letters, digits, symbols and spaces.

## Answer

遇到曾經出現過的字時將start往右移 (ex. s="abbcdefa")

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_characters = {}
        max_length = start = 0
        for character_index, character in enumerate(s):
            # start <= used_characters[character] to prevent start move back to left
            if character in used_characters and start <= used_characters[character]:
                # Move start to character's previous index
                start = used_characters[character] + 1
            else:
                # Update max length
                max_length = max(max_length, character_index - start + 1)
            # Record character's last index
            used_characters[character] = character_index
        return max_length
```
