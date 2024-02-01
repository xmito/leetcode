

# Zigzag Conversion (Medium)
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given
# number of rows like this: (you may want to display this pattern in a
# fixed font for better legibility)
#P   A   H   N
#A P L S I I G
#Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

def decstep(step):
    """
        Given step between two top letters in columns, decstep yields a pair
        of values that when alternately added to initial index allow to iterate
        over letters that will be consecutive in string output
    """

    x = step
    y = 0
    while x != 0:
        yield x, y
        x = x - 2
        y = y + 2
    
    yield x, y 

def cycle(iterable):
    """ Infinite cycle for iterable that skips zero values """
    while True:
        for value in iterable:
            if value == 0:
                continue
            yield value 


# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    result = ''
    step = numRows + (numRows - 2) # Step between two letters on top
    
    # Initial index, List of index increments to cycle
    for i, (x, y) in enumerate(decstep(step)):
        generator = cycle([x, y])
        while i < len(s):
            result += s[i]
            i += next(generator)
    
    return result


if __name__ == "__main__":
    ret = convert("PAYPALISHIRING", numRows=3)
    print(ret)
    assert ret == "PAHNAPLSIIGYIR"

    ret = convert("PAYPALISHIRING", numRows=4)
    print(ret)
    assert ret == "PINALSIGYAHRPI"

    ret = convert("A", numRows=1)
    print(ret)
    assert ret == "A"

# The hard part will be to calculate how to jump to the next character.
# If we have to jump to the next section then it's simple: we only jump
# charsInSection characters. So, currIndex += charsInSection
# If we have to jump to the next character in the same section, then we will have
# to calculate how many characters are between these two positions and increment
# currIndex by that value. If the total characters in a section are charsInSection
# and we are in the ith row, then the number of characters above the current row
# will be 2*i and the number of characters left will be
# charsInBetween = charsInSection - 2*i
# So, secondIndex = currIndex + charsInBetween
