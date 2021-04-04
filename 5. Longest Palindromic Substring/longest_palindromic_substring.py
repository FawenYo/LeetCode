# Simple version
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


if __name__ == "__main__":
    s = "aacabdkacaa"
    answer = Solution().longestPalindrome(s=s)
    print(answer)
