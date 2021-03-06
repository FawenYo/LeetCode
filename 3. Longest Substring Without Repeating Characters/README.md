# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium

## Question

Given a string `` s ``, find the length of the __longest substring__ without repeating characters.

&nbsp;

__Example 1:__

<pre>
<strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "abc", with the length of 3.
</pre>

__Example 2:__

<pre>
<strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is "b", with the length of 1.
</pre>

__Example 3:__

<pre>
<strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</pre>

__Example 4:__

<pre>
<strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

&nbsp;

__Constraints:__

* <code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code>
* `` s `` consists of English letters, digits, symbols and spaces.

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
