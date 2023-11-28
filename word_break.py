from typing import List
from collections import deque
from bisect import bisect_right

# Word Break (Medium)
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
# into a space-separated sequence of one or more dictionary words. Note that the same word
# in the dictionary may be reused multiple times in the segmentation.
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


# NOTATION:
# Let w be the maximum word length in wordDict
# Let m be number of words in wordDict
# Let n be a length of string s

# TIME COMPLEXITY:
# O(mw) - creating words set
# O(n) - creating substring
# O(nˆ3) - each starting index is pushed and popped from queue at most once (we use substring
# list prevent that). For each such index, we iterate over possible end indices (O(n)),
# create slice (at most O(n)) and verify if such word exists (O(1))
# => O(nˆ3 + mw)

# SPACE COMPLEXITY:
# O(mw) - words set
# O(n) - substring list
# => O(n + mw)

# Time complexity: O(nˆ3 + mw)
# Space complexity: O(n + mw)
def wordBreakBfs(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    substring = [False] * len(s)

    queue = deque([0])
    while queue:
        start = queue.popleft()
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if substring[end - 1]:
                continue

            if s[start:end] in words:
                substring[end - 1] = True
                queue.append(end)

    return False


# NOTATION:
# Let w be the maximum word length in wordDict
# Let m be number of words in wordDict
# Let n be a length of string s

# TIME COMPLEXITY:
# O(m) for word_by_length dictionary initialization
# O(wlogw) for sorting word lengths list
# O(nlogw) for bisect_right over all iterations
# O(nmw) - to check whether we can form a word of certain size we have to iterate over all words in the worst case and do comparisons
# => O(n * (logw + mw) + wlogw)

# SPACE COMPLEXITY:
# O(m) for storing words by their lengths in word_by_length dict
# O(n) for substring list that holds results for subproblems
# O(w) for word_lengths list that holds sorted word lengths
# => O(n + m + w)

# Dynamic Programming: Store True/False for each prefix substring of size i
# dp(i) = any(s[i - word.length - 1:i] == word && dp(i - word.length))
# Time complexity: O(n * (logw + mw) + wlogw)
# Space complexity: O(n + w + m)
def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_by_length = {}
    for word in wordDict:
        word_by_length.setdefault(len(word), [])
        word_by_length[len(word)].append(word)

    word_lengths = sorted(word_by_length.keys())
    substring = [False] * (len(s) + 1)
    substring[0] = True

    for i in range(word_lengths[0], len(s) + 1):
        index = bisect_right(word_lengths, i)

        for word_length in word_lengths[:index]:
            size = i - word_length
            if not substring[size]:
                continue

            for word in word_by_length[word_length]:
                if word == s[size:size + word_length]:
                    substring[i] = True
                    break

            if substring[i]:
                break

    return substring[len(s)]


# NOTATION:
# Let w be the maximum word length in wordDict
# Let m be number of words in wordDict
# Let n be a length of string s

# TIME COMPLEXITY:
# O(mw) - constructing trie (iteration over each word and character)
# O(n) - substring inititalization
# O(nˆ2) - for each prefix size, we iterate over following indices
# => O(nˆ2 + mw)

# SPACE COMPLEXITY:
# O(mw) - trie
# O(n) - substring list
# => O(n + mw)

# Dynamic Programming with Trie Optimization: Store True/False for each prefix substring of size i
# dp(i) = any(s[i - word.length - 1:i] == word && dp(i - word.length))
# Time complexity: O(nˆ2 + mw)
# Space complexity: O(n + mw)
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

def wordBreakTrie(s: str, wordDict: List[str]) -> bool:
    root = TrieNode()
    for word in wordDict:
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
    
    substring = [False] * (len(s) + 1)
    substring[0] = True

    for i in range(1, len(s) + 1):
        # If we cant construct prefix one smaller, there's
        # no point in expanding from that prefix
        if not substring[i - 1]:
            continue

        curr = root
        for j in range(i - 1, len(s)):
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]
            
            if curr.is_word:
                substring[j + 1] = True

    return substring[len(s)]


if __name__ == "__main__":
    res = wordBreakTrie("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb", [
        "abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a",
        "bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb",
        "bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd",
        "ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb",
        "ddadbad","badb","ab","aaaaa","acba","abbb",
    ])
    assert res == True

    res = wordBreakTrie("leetcode", ["leet", "code"])
    assert res == True

    res = wordBreakTrie("applepenapple", ["apple", "pen"])
    assert res == True

    res = wordBreakTrie("catsandog", ["cats","dog","sand","and","cat"])
    assert res == False
