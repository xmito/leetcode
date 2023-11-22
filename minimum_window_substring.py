from collections import Counter, deque

# Minimum Window Substring (Hard)
# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring of s such that every character in t (including duplicates) is included in
# the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

# Time complexity: O(n * m) - n is s length and m is t length
# Space complexity: O(m)
def minWindowInitial(s: str, t: str) -> str:
    tcounter = Counter(t)
    scounter = Counter()
    spos, epos = 0, 0

    minlen = float('inf')
    minsub = ""
    for i in range(len(s)):
        letter = s[i]
        if letter not in tcounter:
            continue
        
        scounter[letter] += 1
        if scounter >= tcounter:
            while scounter[s[spos]] > tcounter[s[spos]] or s[spos] not in tcounter:
                if s[spos] in tcounter:
                    scounter[s[spos]] -= 1
                spos += 1

            epos = i
            if epos - spos + 1 < minlen:
                minlen = epos - spos + 1
                minsub = s[spos:epos + 1]

            scounter[s[spos]] -= 1
            spos += 1

    return minsub


# Time complexity: O(n + m) - m for creating Counter at the start. n because spos and
# epos pointers may iterate over the whole string s at most once each
# Space complexity: O(m) - we keep counts only for relevant letters in s
def minWindow(s: str, t: str) -> str:
    tcounter = Counter(t)
    scounter = Counter()
    spos, epos = 0, 0

    minlen = float("inf")
    minsub = ""

    # Number of characters from t present in sliding window
    formed = 0

    for i in range(len(s)):
        letter = s[i]
        if letter not in tcounter:
            continue

        scounter[letter] += 1
        if scounter[letter] == tcounter[letter]:
            formed += 1
        
        while formed == len(tcounter):
            if s[spos] not in tcounter:
                spos += 1
                continue

            if scounter[s[spos]] > tcounter[s[spos]]:
                scounter[s[spos]] -= 1
                spos += 1
                continue

            epos = i
            if epos - spos + 1 < minlen:
                minlen = epos - spos + 1
                minsub = s[spos:epos + 1]

            scounter[s[spos]] -= 1
            formed -= 1
            spos += 1

    return minsub

       
if __name__ == "__main__":
    res = minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
    print(res)
    assert res == "abbbbbcdd"

    res = minWindow("ADOBECODEBANC", "ABC")
    print(res)
    assert res == "BANC"

    res = minWindow("a", "a")
    print(res)
    assert res == "a"

    res = minWindow("a", "aa")
    print(res)
    assert res == ""

    res = minWindow("aa", "aa")
    print(res)
    assert res == "aa"