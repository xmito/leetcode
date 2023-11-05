
# Longest Repeating Substring (Medium)
# Given a string s, return the length of the longest repeating substrings.
# If no repeating substring exists, return 0.

# Dummy approach - Look for repeating substring and proceed from the longest
# possibly repeating substrings to smaller ones. We can do that because if we
# have repeating substring of size L, than we also have repeating substring of
# size L - 1.
# Time complexity: If we have slen L, we do check for (N - L - 1) shifts and
# each shift costs L (because we need to create hash for substring of size L)
# All in all we have sum over slen L (1..N) of (N - L - 1) * L, which after
# simplification is in O(Nˆ3)
# Naive string matching takes time O((n - m + 1) * m) for substring of length m. If
# m = n / 2, the worst case complexity is O(nˆ2). Now if we check for all n substring
# lengths, complexity becomes O(nˆ3)
# Space complexity: O(Nˆ2) because for slen L we store (N - L) * L string characters
def DummyLongestRepeatingSubstring(s: str) -> int:
    n = len(s)
    for slen in range(n - 1, 0, -1):
        substrings = set()
        for i in range(0, n - slen + 1):
            j = i + slen
            if s[i:j] in substrings:
                return slen
            else:
                substrings.add(s[i:j])

    return 0


# Dummy approach with binary search - Use binary search to look for the longest
# length of repeating substring and store seen hashes in hashset
# Time complexity: worst case O(logn * nˆ2). Check for single substring length m
# takes O((n - m + 1) * m) time. The worst case is for m = n/2 and we get O(nˆ2)
# bound. Now, we also check at most logn substring lengths, thus the worst case
# complexity is O(logn * nˆ2)
# Space complexity: O(n), because we store at most n hashes with constant size in hashset
def BinarySearch(s: str, m: int) -> bool:
    """ Check if string s contains repeating substring of size m """
    n = len(s)
    hashes = set()
    for i in range(0, n - m + 1):
        j = i + m
        shash = hash(s[i:j])
        if shash in hashes:
            return True
        else:
            hashes.add(shash)

    return False

def BinaryLongestRepeatingSubstring(s: str) -> int:
    i, j = 1, len(s)
    while i <= j:
        m = i + (j - i) // 2

        if BinarySearch(s, m):
            i = m + 1
        else:
            j = m - 1
    
    return i - 1


# Approach with binary search for substring length and rabin karp for substring matching
def rabin_karp(s: str, p: str, d: int=26, q: int=165580961) -> int:
    """ 
        Rabin-karp worst case complexity is O((n - m + 1) * m) in case we verify almost
        every shift(string containing only single repeated character). In expected case,
        we assume there will be only constant number c of valid shifts and complexity
        becomes O((n - m + 1) + cm) => O(n + m) and since m <= n, we get O(n) time
        d -> d-ary alphabet (english lowercase letters, by default 26)
        q -> modulo - choose prime number such that d*q and 10*q fits into computer word
        * Uses polynomial rolling hash not rabin-karp fingerprint
    """

    n = len(s)
    m = len(p)
    h = d**(m - 1)
    shash, phash = 0, 0

    for i in range(m):
        phash = (d * phash + ord(p[i])) % q
        shash = (d * shash + ord(s[i])) % q

    for i in range(n - m + 1):
        if shash == phash:
            if s[i:i + m] == p:
                yield i

        # Recompute hash for substring
        if i < n - m:
            shash = (d*(shash - ord(s[i])*h) + ord(s[i + m])) % q


def search(s:str, m: int, q: int, d:int) -> bool:
    """
        Returns true if s contains any substring of size m multiple times
        s -> string
        m -> substring size
        q -> modulo
        d -> alphabet size
    """

    n = len(s)
    h = d**(m - 1)
    shash = 0
    hashes = set()

    for i in range(m):
        shash = d * shash + ord(s[i])
    hashes.add(shash)

    for i in range(1, n - m + 1):
        j = i + m - 1
        
        # Computing rolling hash without modulo
        # Python integers can hold arbitrary value not restricted by the size of
        # computer word. Algorithm will work, but complexity of operations on integers
        # larger than computer word will slow down computation dramatically (this can't
        # be used for large patterns). Otherwise complexity is O(n * logn)

        # Approach II: Store substrings for each hash. It will increase space
        # complexity to O(nˆ2), because we have O(n) shifts and each substring
        # of size at most n. After checking condition that hashes match, we need
        # to look if the current string is present in a list of substrings that had
        # the same hash value. We assume there will be only constant number of them,
        # so lookup will take O(n)
        # Time complexity would be O(nˆ2 * logn)

        shash = d*(shash - ord(s[i - 1])*h) + ord(s[j])
        if shash in hashes:
            return True
        hashes.add(shash)

    return False


def RabinKarpLongestRepeatingSubstring(s: str) -> int:
    q = 165580961
    d = 26
    i, j = 1, len(s)
    while i <= j:
        m = i + (j - i) // 2

        if search(s, m, q, d):
            i = m + 1
        else:
            j = m - 1
    
    return i - 1


if __name__ == "__main__":
    res = RabinKarpLongestRepeatingSubstring("abcd")
    print(res)
    assert res == 0

    # Longest repeating subtring is ab and ba
    res = RabinKarpLongestRepeatingSubstring("abbaba")
    print(res)
    assert res == 2

    # Longest repeating substring is aab
    res = RabinKarpLongestRepeatingSubstring("aabcaabdaab")
    print(res)
    assert res == 3