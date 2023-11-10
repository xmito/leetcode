from typing import List

# Text justification (Hard)
# Given an array of strings words and a width maxWidth, format the text such that
# each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you
# can in each line. Pad extra spaces ' ' when necessary so that each line has exactly
# maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number
# of spaces on a line does not divide evenly between words, the empty slots on the left
# will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted
# between words.
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

# Constraints:
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

# Time complexity: O(n*m) where n is number of words and m is maximum length of
# each word maxWidth. In alg. we take length of each word + forming line out of words
# Space complexity: O(m) for holding line we are constructing
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    end = 0
    result = []
    while end < len(words):
        # Compute number of words that fit into line
        start = end
        length = len(words[start])
        while end + 1 < len(words) and length + len(words[end + 1]) + 1 <= maxWidth:
            length += len(words[end + 1]) + 1
            end = end + 1
        end = end + 1

        # Compute number of spaces between words and extra spaces
        try:
            wlength = length - (end - start - 1)
            spaces = (maxWidth - wlength) // (end - start - 1)
            espaces = (maxWidth - wlength) % (end - start - 1)
        except ZeroDivisionError:
            spaces, espaces = 0, 0

        line = words[start]
        for i in range(start + 1, end):
            # Compose last line
            if end == len(words):
                line += ' ' + words[i]
                continue

            line += ' ' * spaces
            if espaces:
                line += ' '
                espaces -= 1
            line += words[i]

        line += ' ' * (maxWidth - len(line))
        result.append(line)
    
    return result


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    res = fullJustify(words, maxWidth=16)
    print(res)
    assert res == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]

    words = ["What","must","be","acknowledgment","shall","be"]
    res = fullJustify(words, maxWidth=16)
    print(res)
    assert res == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]

    words = [
        "Science","is","what","we","understand","well","enough","to","explain","to",
        "a","computer.","Art","is","everything","else","we","do",
    ]
    res = fullJustify(words, maxWidth=20)
    print(res)
    assert res == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
