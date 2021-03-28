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


if __name__ == "__main__":
    s = "III"
    answer = Solution().romanToInt(s=s)
    print(answer)
