

# Longest Substring Without Repeating Characters (Medium)
# Given a string s, find the length of the longest substring without repeating characters.
# Constraints:
# 0 <= s.length <= 5 * 10ˆ4
# s consists of English letters, digits, symbols and spaces.


# TIME COMPLEXITY: O(n) - each letter is added and removed once with O(1) cost
# SPACE COMPLEXITY: O(min(m, n)) - minimum of letters and alphabet size
def lengthOfLongestSubstring(s: str) -> int:
    start, longest = 0, 0
    letters = set()

    for end in range(len(s)):
        # close window
        while s[end] in letters:
            letters.remove(s[start])
            start += 1

        # expand window
        letters.add(s[end])
        longest = max(longest, (end - start + 1))
    
    return longest 


# Instead of sliding window, do jumps to the next occurrence of letter
# TIME COMPLEXITY: O(n) - each letter is added at most once
# SPACE COMPLEXITY: O(min(m, n)) - minimum of letters and alphabet size
def lengthOfLongestSubstringOptimized(s: str) -> int:
    start, longest = 0, 0
    letters = {}

    for end in range(len(s)):

        if s[end] in letters:
            start = max(start, letters[s[end]] + 1)
        
        letters[s[end]] = end
        longest = max(longest, (end - start + 1))

    return longest

# Further possible improvement using ordinal values of letters


if __name__ == "__main__":
    ret = lengthOfLongestSubstringOptimized("abba")
    print(ret)
    assert ret == 2

    ret = lengthOfLongestSubstringOptimized("abcabcbb")
    print(ret)
    assert ret == 3

    ret = lengthOfLongestSubstringOptimized("bbbbb")
    print(ret)
    assert ret == 1

    ret = lengthOfLongestSubstringOptimized("pwwkew")
    print(ret)
    assert ret == 3

    ret = lengthOfLongestSubstringOptimized("abkcbkptne")
    print(ret)
    assert ret == 7
