# Roman To Integer (Easy)
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making
# four. The same principle applies to the number nine, which is written as
# IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Let n be the length of roman symbols in a string
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def romanToInt(s: str) -> int:
    values = [1, 5, 10, 50, 100, 500, 1000]
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    res = 0
    i = 0
    while i < len(s):
        l1_idx = roman.index(s[i])
        l2_idx = roman.index(s[min(i + 1, len(s) - 1)])

        if l1_idx < l2_idx:
            res += values[l2_idx] - values[l1_idx]
            i += 2
            continue
        res += values[l1_idx]
        i += 1
    return res


# Let n be the length of roman symbols in a string
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def romanToIntImproved(s: str) -> int:
    mapping = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4,
    }
    i = 0
    result = 0
    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in mapping:
            result += mapping[s[i:i+2]]
            i += 2
        else:
            result += mapping[s[i]]
            i += 1

    return result


# Let n be the length of roman symbols in a string
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def romanToIntRightToLeft(s: str) -> int:
    last = len(s) - 1
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = mapping[s[last]]

    for i in range(last - 1, -1, -1):
        if mapping[s[i]] < mapping[s[i + 1]]:
            total -= mapping[s[i]]
        else:
            total += mapping[s[i]]

    return total


if __name__ == "__main__":
    ret = romanToInt("III")
    print(ret)
    assert ret == 3

    ret = romanToInt("LVIII")
    print(ret)
    assert ret == 58

    ret = romanToInt("MCMXCIV")
    print(ret)
    assert ret == 1994
