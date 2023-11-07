from typing import List

# Group Anagrams (Medium)
# Given an array of strings strs, group the anagrams together. You can return the
# answer in any order. An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, typically using all the original letters exactly once.
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Time complexity: O(nk * logk), because there are n strings of length k and each one is sorted
# Space complexity: O(nk), because we store all anagrams in dictionary
def groupAnagramsEasy(strs: List[str]) -> List[List[str]]:
    sstrs = [str(sorted(s)) for s in strs]
    results = {}

    for i in range(len(strs)):
        results.setdefault(sstrs[i], [])
        results[sstrs[i]].append(strs[i])
    
    return list(results.values())


# Time complexity: O(nk)
# Space complexity: O(nk)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    results = {}
    for word in strs:
        fqtable = [0] * 26
        for char in word:
            fqtable[ord(char) - ord('a')] += 1
        results.setdefault(tuple(fqtable), [])
        results[tuple(fqtable)].append(word)

    return list(results.values())
    

if __name__ == "__main__":
    res = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)
    assert res == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    res = groupAnagrams([""])
    print(res)
    assert res == [[""]]

    res = groupAnagrams(["a"])
    print(res)
    assert res == [["a"]]
