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


if __name__ == "__main__":
    s = "tmmzuxta"
    answer = Solution().lengthOfLongestSubstring(s=s)
    print(answer)
