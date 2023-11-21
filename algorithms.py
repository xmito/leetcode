
# Given an integer array nums, find the  subarray with the largest sum
def maxSubArray(nums: List[int]) -> int:
    global_max = -float('inf')
    local_max = 0
    for i in range(len(nums)):
        local_max = max(nums[i], local_max + nums[i])
        if local_max > global_max:
            global_max = local_max
    return global_max


# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2. You have the following three operations
# permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# o(i - 1, j - 1) if word1[i] == word2[j]
# o(i - 1, j - 1) + 1 if replace word1[i] with word2[j] letter
# o(i, j - 1) + 1 if insert word2[j] after word1[i]
# o(i - 1, j) + 1 if delete word1[i] letter
def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    x = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        x[i][0] = x[i - 1][0] + 1
    for j in range(1, m + 1):
        x[0][j] = x[0][j - 1] + 1

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if word1[j - 1] != word2[i - 1]:
                x[i][j] = min(
                    x[i][j - 1],
                    x[i - 1][j],
                    x[i - 1][j - 1],
                ) + 1
            else:
                x[i][j] = x[i - 1][j - 1]

    return x[n][m]


# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial). Solution:
# Solution: Let c[i][j] be True if pattern prefix of length i matches word
# prefix of length j. Recursive solution for c[i][j] is as follows:
# c[i-1][j] or c[i-1][j-1] or c[i][j-1]     if pattern[i] == '*'
# c[i-1][j-1]                               if pattern[i] == '?'
# c[i-1][j-1] and pattern[i] == word[j]     if pattern[i] not in ['*', '?']
def isMatch(s: str, p: str) -> bool:
    n = len(p)
    m = len(s)
    t = [[False] * (m + 1) for _ in range(n + 1)]

    t[0][0] = True
    for i in range(1, m + 1):
        t[0][i] = False
    for i in range(1, n + 1):
        t[i][0] = t[i - 1][0] and p[i - 1] == '*'
    
    for pi in range(1, n + 1):
        for wi in range(1, m + 1):
            if p[pi - 1] == '*':
                t[pi][wi] = t[pi - 1][wi] or t[pi - 1][wi - 1] or t[pi][wi - 1]
            elif p[pi - 1] == '?':
                t[pi][wi] = t[pi - 1][wi - 1]
            else:
                t[pi][wi] = t[pi - 1][wi - 1] and p[pi - 1] == s[wi - 1]
    return t[n][m]


# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial). Solution:
# c[i-1][j-1] and (word[j] == pattern[i] or pattern[i] == '.')                                      if pattern[i] != '*'
# c[i-2][j] or (c[i-2][j-1] or c[i][j-1]) and (word[j] == pattern[i-1] or pattern[i-1] == '.')      if pattern[i] == '*'
def isMatch(s: str, p: str) -> bool:
    n = len(p)
    m = len(s)
    t = [[False] * (m + 1) for _ in range(n + 1)]

    t[0][0] = True
    for i in range(1, m + 1):
        t[0][i] = False
    for i in range(1, n + 1):
        if p[i - 1] == '*' or (i < n and p[i] == '*'):
            t[i][0] = t[i - 1][0]

    for pi in range(1, n + 1):
        for wi in range(1, m + 1):
            if p[pi - 1] == '*':
                no_match = t[pi - 2][wi]
                single_match = t[pi - 2][wi - 1] and (s[wi - 1] == p[pi - 2] or p[pi - 2] == '.')
                more_match = t[pi][wi - 1] and (s[wi - 1] == p[pi - 2] or p[pi - 2] == '.')
                t[pi][wi] = no_match or single_match or more_match
            else:
                t[pi][wi] = t[pi - 1][wi - 1] and (s[wi - 1] == p[pi - 1] or p[pi - 1] == '.')

    return t[n][m]


# You are given an array of k linked-lists lists, each linked-list is sorted
# in ascending order. Merge all the linked-lists into one sorted linked-list
# and return it.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    begin, end = None, None
    while lists:
        lists = sorted(lists, key=lambda x: x.val)
        if begin is None:
            begin = lists[0]
            end = begin
        else:
            end.next = lists[0]
            end = end.next

        lists[0] = lists[0].next
        if lists[0] is None:
            del lists[0]

    return begin


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    begin, end = None, None
    lists = list(filter(lambda x: x is not None, lists))
    while lists:
        lists = sorted(lists, key=lambda x: x.val)
        
        minval = lists[0].val
        i = 0
        while i < len(lists):
            if lists[i].val != minval:
                break

            if begin is None:
                begin = lists[i]
                end = begin
            else:
                end.next = lists[i]
                end = end.next

            lists[i] = lists[i].next
            if lists[i] is None:
                del lists[i]
                continue
            i = i + 1
    return begin


# Given the head of a linked list, reverse the nodes of the list k at a time,
# and return the modified list. k is a positive integer and is less than or
# equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
def swap(start, end):
    prev = ListNode(None, None)
    while start != end:
        next = start.next
        start.next = prev
        prev = start
        start = next
    start.next = prev

def jump(node, steps):
    for i in range(steps):
        if node is None:
            break
        node = node.next
    return node

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    initial = None
    pre = ListNode(None, None)
    start, end = head, head

    end = jump(end, steps=k - 1)

    while end:
        post = end.next
        swap(start, end)
        pre.next = end
        start.next = post

        if initial is None:
            initial = end
        
        pre = start
        start, end = post, post
        end = jump(end, steps=k - 1)

    return initial            


# (32) Given a string containing just the characters '(' and ')', return the
# length of the longest valid (well-formed) parentheses substring. Solution:
def longestValidParentheses(s: str) -> int:
    stack = [-1]
    sublen = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
                sublen = max(sublen, i - stack[-1])
            except IndexError:
                stack.append(i)

    return sublen

# Dynamic programming solution (wrong complexity... check for loop)
def longestValidParenthesesDynamic(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    mtx = [[0] * n for i in range(n)]
    for k in range(2, n + 1): # over each substring length
        for i in range(n - k + 1): # start index
            j = i + k - 1 # end index
            if s[i] == '(' and s[j] == ')':
                # ith and jth char bracket match each other
                if k % 2 == 0 and mtx[i + 1][j - 1] == j - i - 1:
                    mtx[i][j] = mtx[i + 1][j - 1] + 2
                elif k % 2 == 0:
                    value = 0
                    for t in range(i + 1, j, 2):
                        if mtx[i][t] == t - i + 1 and mtx[t + 1][j] == j - t:
                            value = max(value, mtx[i][t] + mtx[t + 1][j])
                        else:
                            value = max(value, mtx[i][t], mtx[t + 1][j])
                    mtx[i][j] = value
                elif k % 2 == 1:
                    mtx[i][j] = max(mtx[i + 1][j], mtx[i][j - 1])
                else:
                    print('Unknown case')
            elif s[i] == ')' and s[j] == ')':
                mtx[i][j] = mtx[i + 1][j]
            elif s[i] == '(' and s[j] == '(':
                mtx[i][j] = mtx[i][j - 1]
            elif s[i] == ')' and s[j] == '(':
                mtx[i][j] = mtx[i + 1][j - 1]

    return mtx[0][n - 1]


# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.
# Following solution has O(nˆ2) time complexity and O(1) spatial complexity
def trap(heights: List[int]) -> int:
    i = 0
    units = 0
    while i < len(heights) - 1:
        h = heights[i]
        higher, hh = -1, -1
        for j in range(i + 1, len(heights)):
            if heights[j] > hh:
                higher = j
                hh = heights[j]
            if hh >= h:
                break

        for j in range(i + 1, higher):
            units += min(h, hh) - heights[j]
        i = higher
    return units

# O(n) time complexity and O(n) space complexity
def trap(height: List[int]) -> int:
    n = len(height)
    l = [0] * n  
    r = [0] * n
    ans = 0
    lm, rm = 0, 0

    for i in range(n):
        l[i] = lm
        if lm < height[i]:
            lm = height[i]
    for i in range(n - 1, -1, -1):
        r[i] = rm
        if rm < height[i]:
            rm = height[i]
    for i in range(n):
        trapped = min(l[i], r[i]) - height[i]
        if trapped > 0:
            ans += trapped

    return ans


# Two Sum
# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target. You may assume that each
# input would have exactly one solution, and you may not use the same element
# twice. You can return the answer in any order.
from bisect import bisect, insort
# O(nˆ2) time complexity solution
def twoSumSq(nums: List[int], target: int) -> List[int]:
    remnants = []
    for i, num in enumerate(nums):
        remnant = target - num
        try:
            index = remnants.index(remnant)
            return index, i
        except ValueError:
            pass
        remnants.append(num)

# O(nlogn) time complexity solution
def twoSum(nums: List[int], target: int) -> List[int]:
    remnants = []
    for idx, num in enumerate(nums):
        try:
            rem = target - num
            rem_idx = bisect(remnants, rem, key=lambda x: x[0])
            if remnants[rem_idx - 1][0] == rem:
                _, value_idx = remnants[rem_idx - 1]
                return idx, value_idx
        except IndexError:
            pass
        insort(remnants, (num, idx), key=lambda x: x[0])


# Add Two Numbers
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list. You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
from math import floor
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    final, result = None, None
    takeover = 0
    while l1 or l2 or takeover:
        if l1 and l2:
            value = (l1.val + l2.val + takeover) % 10
            takeover = floor((l1.val + l2.val + takeover) / 10)
            l1 = l1.next
            l2 = l2.next
        elif l1:
            value = (l1.val + takeover) % 10
            takeover = floor((l1.val + takeover) / 10)
            l1 = l1.next
        elif l2:
            value = (l2.val + takeover) % 10
            takeover = floor((l2.val + takeover) / 10)
            l2 = l2.next
        else:
            value = takeover
            takeover = 0
        
        if result is None:
            final = ListNode(value)
            result = final
        else:
            result.next = ListNode(value)
            result = result.next
    
    return final


# Longest Substring Withour Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example: "abkcbkptne" longest substring of length 7: "cbkptne"
# TODO Do amortized analysis? O(n)
# Assume that every kth position we encounter duplicate letter. Than we need
# to verify n/k times at most k letters (largest possible substring without
# repeated letters), which gives us O(n) complexity
def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    letters = set()
    start, end = 0, 0
    while end < len(s):
        letter = s[end]
        if letter in letters:
            longest = max(longest, end - start)
            start = (end - start) - s[start:end][::-1].index(letter) + start 
            end = end + 1
            letters = set(s[start:end])
            continue
        letters.add(letter)
        end = end + 1

    longest = max(longest, end - start)
    return longest

# Similar solution - O(n) complexity - each letter is added and removed once
def lengthOfLongestSubstring(s: str) -> int:
    start, longest = 0, 0
    letters = set()

    for end in range(len(s)):
        # close window
        while s[end] in letters:
            letters.remove(s[l])
            start += 1
        # expand window
        letters.add(s[end])
        longest = max(longest, (end - start + 1))
    
    return longest 


# Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given
# number of rows like this: (you may want to display this pattern in a
# fixed font for better legibility)
#P   A   H   N
#A P L S I I G
#Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
def decstep(step):
    x = step
    y = 0
    while x != 0:
        yield x, y
        x = x - 2
        y = y + 2
    
    yield x, y 

def cycle(iterable, skip=None):
    while True:
        for value in iterable:
            if value == 0:
                continue
            yield value 

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    result = ''
    step = numRows + (numRows - 2)
    for i, (x, y) in enumerate(decstep(step)):
        generator = cycle([x, y])
        while i < len(s):
            result += s[i]
            i += next(generator)
    
    return result


# Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer
# range [-2**31, 2**31 - 1], then return 0.
MAX = 2**31 - 1
MIN = -2**31
def reverse(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1
        x = abs(x)
    
    init_zero = True
    while x:
        value = x % 10
        if value > 0 or not init_zero:
            if res > (MAX - value) // 10:
                return 0
            if res < MIN // 10 - value // 10:
                return 0
            res = res * 10 + value
        x = (x - value) // 10
        init_zero = False

    return sign * res


# Palindrome number
# Given an integer x, return true if x is a palindrome, and false otherwise.
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
def isPalindromeEasy(x: int) -> bool:
        xstr = str(x)
        rxstr = xstr[::-1]
        if rxstr[-1] == '-':
            rxstr = rxstr[:-1]
        return xstr == rxstr

# Uses reverse function from "Reverse Integer" issue
def isPalindrome(x: int) -> bool:
        rx = reverse(x)
        if rx < 0:
            rx *= -1
        return x == rx

# Integer To Roman
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


# Roman To Integer
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


# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array
# of strings. If there is no common prefix, return an empty string "".
# ['flower', 'flow', 'flight'] => 'fl'
# ['dog', 'racecar', 'car'] => ''
def commonPrefix(str1, str2):
    i = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            break
        i += 1
    return str1[:i]

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    cpref = strs[0]
    for string in strs[1:]:
        cpref = commonPrefix(cpref, string)
        if not cpref:
            break
    return cpref

