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


if __name__ == "__main__":
    n = 1
    answer = Solution().countAndSay(n=n)
    print(answer)
