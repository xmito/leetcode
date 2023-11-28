from typing import List
from collections import Counter

# Word Break II (Hard)
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct
# a sentence where each word is a valid dictionary word. Return all such possible
# sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# Constraints:
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Input is generated in a way that the length of the answer doesn't exceed 105.


# NOTATION:
# Let w be the maximum word length in wordDict
# Let m be number of words in wordDict
# Let n be a length of string s

# TIME COMPLEXITY:
# O(mw) - constructing trie (iteration over each word and character)
# O(n) - substring and sequences inititalization
# O(nˆ2) - for each prefix size, we iterate over following indices
# O(2ˆn) - Assume that F(i) is number of ways we can break input string prefix of length i.
# We can define it by F(i) = F(i-1) + F(i-2) + ... + F(1) in the worst case where we have
# words consisting of repeated single letter such that we have words of size from 1 up to n
# and input string repeats single letter n times. Then we can simplify:
# F(i) = 2F(i-1)
# This means number of solutions grows exponentially with increasing prefix size. For length
# n, this implies there are 2ˆn solutions. Alternative way of deriving this bound is to think
# about number of ways we can break input string. There are n-1 possible positions at which
# break can be done, so there are 2ˆn-1 possible breaks
# => O(nˆ2 + 2ˆn + mw)

# SPACE COMPLEXITY:
# O(mw) - trie
# O(n) - substring list
# O(nˆ2) - sequences list. For each prefix size i, we store up to i indices of words
# => O(nˆ2 + mw)

# Dynamic Programming with Trie Optimization: Store True/False for each prefix substring of size i
# dp(i) = any(s[i - word.length - 1:i] == word && dp(i - word.length))
# Time complexity: O(nˆ2 + 2ˆn + mw)
# Space complexity: O(nˆ2 + mw)
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.index = None
        self.children = {}

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    # Check whether all characters from s are contained in wordDict
    if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
        return []

    root = TrieNode()
    for index, word in enumerate(wordDict):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
        curr.index = index

    substring = [False] * (len(s) + 1)
    substring[0] = True
    sequences = {i: [] for i in range(len(s) + 1)}

    for i in range(1, len(s) + 1):
        if not substring[i - 1]:
            continue

        curr = root
        for j in range(i - 1, len(s)):
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]

            if curr.is_word:
                substring[j + 1] = True
                sequences[j + 1].append(curr.index)

    sentences = []
    def create_sentences(last: int, sentence: List[str]):
        if last == 0:
            sentences.append(" ".join(sentence))
            return

        for word_index in sequences[last]:
            word = wordDict[word_index]
            create_sentences(last - len(word), [word] + sentence)

    create_sentences(len(s), [])
    return sentences


if __name__ == "__main__":
    res = wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    print(res)
    assert res == ["cat sand dog", "cats and dog"]

    res = wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])
    print(res)
    assert res == ["pine applepen apple", "pineapple pen apple", "pine apple pen apple"]

    res = wordBreak("catsandog", ["cats","dog","sand","and","cat"])
    print(res)
    assert res == []
