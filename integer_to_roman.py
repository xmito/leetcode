import bisect

# Integer To Roman (Medium)
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27
# is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making
# four. The same principle applies to the number nine, which is written as 
# IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# 3 => III, 58 => LVIII, 1994 => MCMXCIV

# Constraints:
# 1 <= num <= 3999


# Let n be number of symbols in a string
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def intToRoman(num: int) -> str:
    res = ''
    values = [1, 5, 10, 50, 100, 500, 1000]
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    while num:
        if num >= 900 and num < 1000:
            res += 'CM'
            num -= 900
            continue
        elif num >= 400 and num < 500:
            res += 'CD'
            num -= 400
            continue
        elif num >= 90 and num < 100:
            res += 'XC'
            num -= 90
            continue
        elif num >= 40 and num < 50:
            res += 'XL'
            num -= 40
            continue
        elif num == 9:
            res += 'IX'
            num -= 9
            continue
        elif num == 4:
            res += 'IV'
            num -= 4
            continue

        # returns i such that all e in values[:i] have e <= num
        # and all e in values[i:] have e > num
        idx = bisect.bisect_right(values, num)
        res += roman[idx - 1] * (num // values[idx - 1])
        num = num % values[idx - 1]

    return res


# Let n be number of symbols
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def intToRomanGreedy(num: int) -> str:
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
              (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
              (5, "V"), (4, "IV"), (1, "I")]

    result = ""
    for value, symbol in digits:
        if num == 0:
            break
        count, num = divmod(num, value)
        result += count * symbol

    return result


if __name__ == "__main__":
    ret = intToRomanGreedy(3)
    print(ret)
    assert ret == "III"

    ret = intToRomanGreedy(58)
    print(ret)
    assert ret == "LVIII"

    ret = intToRomanGreedy(1994)
    print(ret)
    assert ret == "MCMXCIV"

    ret = intToRomanGreedy(843)
    print(ret)
    assert ret == "DCCCXLIII"
