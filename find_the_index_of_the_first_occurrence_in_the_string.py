
# Find the Index of the First Occurrence in the String (Easy)
# Given two strings needle and haystack, return the index of the first occurrence
# of needle in haystack, or -1 if needle is not part of haystack.
# Constraints:
# 1 <= haystack.length, needle.length <= 10ˆ4
# haystack and needle consist of only lowercase English characters.

# Time complexity: O(n * m) - n offsets to check, m characters to compare
# Space complexity: O(1)
def strStrEasy(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    for i in range(len(haystack) - len(needle) + 1):
        for j in range(i, i + len(needle)):
            if haystack[j] != needle[j - i]:
                break
        else:
            return i
    
    return -1


# Rabin-Karp
def rabin_karp(s: str, p: str, d: int=26, q: int=165580961) -> int:
    """ 
        Rabin-karp worst case complexity is O((n - m + 1) * m) in case we verify almost
        every shift(string containing only single repeated character). In expected case,
        we assume there will be only constant number c of valid shifts and complexity
        becomes O((n - m + 1) + cm) => O(n + m) and since m <= n, we get O(n) time
        d -> d-ary alphabet (english lowercase letters, by default 26)
        q -> modulo - choose prime number such that d*q and 10*q fits into computer word
        * Uses polynomial rolling hash not rabin-karp fingerprint
        * If hashes don't match, then pattern and substring don't match
        * Spurious hit is the case when hashes match and substring and pattern don't
        * Modulo should be chosen such that 10q and dq fit into single word
    """

    n = len(s)
    m = len(p)
    
    # Compute the largest weight such that we don't overflow
    h = 1
    for i in range(m):
        h = (h * d) % q
    shash, phash = 0, 0

    for i in range(m):
        phash = (d * phash + ord(p[i])) % q
        shash = (d * shash + ord(s[i])) % q

    for i in range(n - m + 1):
        if shash == phash:
            if s[i:i + m] == p:
                yield i

        # Recompute hash for substring without overflow
        if i < n - m:
            shash = ((d*shash % q) - (ord(s[i])*h % q) + ord(s[i + m])) % q

def strStrRabin(haystack: str, needle: str) -> int:
    for pos in rabin_karp(haystack, needle):
        return pos
    return -1


# KMP
# Time complexity: O(n + m) - m for prefix function and n for pattern matching
# Space complexity: O(m) - prefix function
def kmp(s: str, p: str):
    """ """
    n = len(s)
    m = len(p)

    prefix = [0] * (m + 1)
    k = 0 # Current longest prefix matching pattern suffix
    for i in range(2, m + 1):
        # If the current pattern characters don't match, look for the
        # longest prefix of length k, that has matching char at k + 1
        while k > 0 and p[k] != p[i - 1]:
            k = prefix[k]

        if p[i - 1] == p[k]:
            k = k + 1
        prefix[i] = k

    k = 0
    for i in range(n - m + 1):
        while k > 0 and p[k] != s[i]:
            k = prefix[k]
        if p[k] == s[i]:
            k = k + 1
        if k == m:
            k = prefix[k]
            yield i - m + 1

def strStrKMP(haystack: str, needle: str) -> int:
    for pos in kmp(haystack, needle):
        return pos
    return -1


if __name__ == "__main__":
    res = strStrEasy("sadbutsad", "sad")
    assert res == 0

    res = strStrEasy("leetcode", "leeto")
    assert res == -1

    res = strStrRabin("sadbutsad", "sad")
    assert res == 0

    res = strStrRabin("leetcode", "leeto")
    assert res == -1

    res = strStrKMP("sadbutsad", "sad")
    assert res == 0

    res = strStrKMP("leetcode", "leeto")
    assert res == -1
