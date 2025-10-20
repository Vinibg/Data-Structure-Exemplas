#This code is to find the longest substring without repeating characters

from collections import defaultdict

def longest_substring_without_repeating_characters(s: str) -> int:
    longest = 0
    l = 0
    counter: dict[str, int] = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]] += 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest

if __name__ == "__main__":
   string = input()
   res = longest_substring_without_repeating_characters(string)
   print(res)