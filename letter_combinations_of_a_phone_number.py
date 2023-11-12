from typing import List

# Letter Combinations of a Phone Number (Medium)
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in
# any order. A mapping of digits to letters (just like on the telephone
# buttons) is given below. Note that 1 does not map to any letters.
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

MAP = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


# Time complexity: 4ˆN * N where N is length of digits
# Space complexity: 4ˆN * N
def letterCombinationsBrute(digits: str) -> List[str]:
    results = []
    if not digits:
        return results
    
    results = MAP[digits[0]]
    for digit in digits[1:]:
        temp = []
        for result in results:
            temp += [result + letter for letter in MAP[digit]]
        results = temp
    
    return results


# Time complexity: 4ˆN * N where N is length of digits. 4ˆN number of combinations and for
# each combination we have to concatenate letters when appending to combinations list
# Space complexity: O(N) - space for path (up to N chars)
def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        for letter in MAP[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations


if __name__ == "__main__":
    res = letterCombinations("23")
    print(res)
    assert res == ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    res = letterCombinations("")
    print(res)
    assert res == []

    res = letterCombinations("2")
    print(res)
    assert res == ["a","b","c"]
