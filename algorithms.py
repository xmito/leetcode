
# You are climbing a staircase. It takes n steps to reach the top. Each time you
# can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climbStairs(n: int) -> int:
    r = [0] * (n + 2)
    r[1], r[2] = 1, 2
    for i in range(3, n + 1):
        r[i] = r[i - 1] + r[i -2]
    return r[n]

# Number of palindromic substrings. Solution for s[i][j] (number of palindrome substrings in substring):
# s[i][j-1] + s[i+1][j] - s[i+1][j-1] + 1   if substring from i to j is palindrome
# s[i][j-1] + s[i+1][j] + s[i+1][j-1]       if substring from i to j is not palindrome
def countSubstrings(s: str) -> int:
        sub = [[0] * len(s) for i in range(len(s))]
        is_palindrome = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            sub[i][i] = 1
            is_palindrome[i][i] = True
        
        for slen in range(2, len(s) + 1):
            for i in range(len(s) - slen + 1):
                j = i + slen - 1
                sub[i][j] = sub[i][j-1] + sub[i+1][j] - sub[i+1][j-1]
                if s[i] == s[j] and (is_palindrome[i+1][j-1] or i + 1 > j - 1):
                    sub[i][j] += 1
                    is_palindrome[i][j] = True
                
        return sub[0][len(s) - 1]


# Longest palindromic substring/s
def longestPalindrome(s: str) -> tuple[int, list[str]]:
        length = 1
        longest = []

        is_palindrome = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            is_palindrome[i][i] = True
            longest.append(s[i])

        for slen in range(2, len(s) + 1):
            for i in range(len(s) - slen + 1):
                j = i + slen - 1
                if s[i] == s[j] and (is_palindrome[i+1][j-1] or i + 1 > j - 1):
                    is_palindrome[i][j] = True
                    if j - i + 1 == length:
                        longest.append(s[i:j+1])
                    elif j - i + 1 > length:
                        length = j - i + 1
                        longest = [s[i:j+1]]
                
        return length, longest

# There is a robot on an m x n grid. The robot is initially located at the top-left
# corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner
# (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
# point in time. Given the two integers m and n, return the number of possible unique
# paths that the robot can take to reach the bottom-right corner. Solution:
# if i==0 and j==0  => 1
# if i - 1 < 0 .    => t[i][j-1]
# if j - 1 < = .    => t[i-1][j]
# else t[i-1][j] + t[i][j-1]
def combinations(slen, m, n) -> tuple[int, int]:
        for i in range(slen + 1):
            j = slen - i
            if i < m and j < n:
                yield i, j

def uniquePaths(m: int, n: int) -> int:
    t = [[0] * n for i in range(m)]
    for slen in range(m + n - 2 + 1):
        for i, j in combinations(slen, m, n):
            print(f'{i}, {j}')
            if i == 0 and j == 0:
                t[i][j] = 1
            elif i - 1 < 0:
                t[i][j] = t[i][j-1]
            elif j - 1 < 0:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] + t[i][j-1]
    return t[m-1][n-1]

# You are given an m x n integer array grid. There is a robot initially located at
# the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
# corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at
# any point in time. An obstacle and space are marked as 1 or 0 respectively in grid.
# A path that the robot takes cannot include any square that is an obstacle. Return
# the number of possible unique paths that the robot can take to reach the bottom-right corner.
# Solution:
# 1         if i==0 and j==0
# 0         if obstacleGrid[i][j] == 1
# t[i][j-1] if j-1>=0 AND obstacleGrid[i][j-1] == 0 AND (i-1 < 0 or obstacleGrid[i-1][j] == 1)
# t[i-1][j] if i-1>=0 AND obstacleGrid[i-1][j] == 0 AND (j-1 < 0 or obstacleGrid[i][j-1] == 1)
# t[i][j-1] + t[i-1][j] if i-1 >= 0 AND j-1 >= 0 AND obstacleGrid[i][j-1] == 0 AND obstacleGrid[i-1][j] == 0
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    print(f'grid: {m}, {n}')
    t = [[0] * n for i in range(m)]
    for slen in range(m + n - 2 + 1):
        for i, j in combinations(slen, m, n):
            if obstacleGrid[i][j] == 1:
                continue
            if i == 0 and j == 0:
                t[i][j] = 1
            if i - 1 >= 0 and obstacleGrid[i - 1][j] == 0:
                t[i][j] += t[i - 1][j]
            if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                t[i][j] += t[i][j - 1]
    return t[m-1][n-1]

# Given a m x n grid filled with non-negative numbers, find a path from top left to
# bottom right, which minimizes the sum of all numbers along its path. Solution t[i][j]:
# min(t[i-1][j], t[i][j-1]) + grid[i][j]    if i-1 >= 0 AND j-1 >= 0
# t[i-1][j] + grid[i][j]                    if j-1 < 0
# t[i][j-1] + grid[i][j]                    if i-1 < 0
# grid[i][j]                                if i==0 AND j==0
def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    t = [[0] * n for i in range(m)]
    for slen in range(m + n - 2 + 1):
        for i, j in combinations(slen, m, n):
            if i == 0 and j == 0:
                t[i][j] = grid[i][j]
            elif i - 1 < 0:
                t[i][j] = t[i][j-1] + grid[i][j]
            elif j - 1 < 0:
                t[i][j] = t[i-1][j] + grid[i][j]
            else:
                t[i][j] = min(t[i-1][j], t[i][j-1]) + grid[i][j]
    
    return t[m-1][n-1]

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
def canJump(nums: List[int]) -> bool:
    n = len(nums)
    reach = [False for i in range(n)]
    reach[0] = True
    for i in range(n):
        preach = reach.copy()
        for j in range(n):
            if reach[j] == True:
                reach[j + 1:j+nums[j]+1] = [True]*nums[j]
        if reach[n-1] == True or preach == reach:
            break
    return reach[n-1]


# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0]. Each element nums[i] represents the
# maximum length of a forward jump from index i. In other words, if you
# are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]
def jump(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    lo, hi = 0, 0
    for i in range(1, len(nums) + 1):
        nlo, nhi = hi + 1, 0
        for j in range(lo, hi + 1):
            nhi = max(nhi, j + nums[j])
        if nhi >= len(nums) - 1:
            break
        lo, hi = nlo, nhi
    return i


# Generate all permutations for the list of numbers
def permute(self, nums: List[int]) -> List[List[int]]:
    permutations = [[nums[0]]]
    for i in range(1, len(nums)):
        temp = []
        for p in permutations:
            for k in range(len(p)):
                temp += [p[:k] + [nums[i]] + p[k:]]
        permutations = temp
    return permutations


# Generate all permutations without duplicates ([1,1,2,2])
def perrmuteUnique(nums: List[int]) -> List[List[int]]:
    def backtrack(start):
        if start == len(arr) - 1:
            unique_permutations.append(arr[:])
            return

        used = set()
        for i in range(start, len(arr)):
            if arr[i] in used:
                continue
            used.add(arr[i])

            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    unique_permutations = []
    backtrack(0)
    return unique_permutations


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


# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# [-1, 0, 1, 2, -1, 4] => [[-1, -1, 2], [-1, 0, 1]]
def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()
    for i1 in range(len(nums) - 2):
        # Number at index i1 will be the smallest in a triplet of values
        if nums[i1] > 0:
            break

        # Skip duplicate solutions
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        i2, i3 = i1 + 1, len(nums) - 1
        while i2 < i3:
            total = nums[i1] + nums[i2] + nums[i3]
            if total > 0:
                i3 -= 1
            elif total < 0:
                i2 += 1
            else:
                result = [nums[i1], nums[i2], nums[i3]]
                results.append(result)
                # Skip duplicate solutions
                while i2 < i3 and nums[i2] == result[1]:
                    i2 += 1
                while i2 < i3 and nums[i3] == result[2]:
                    i3 -= 1 
    return results


# 4Sum
# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# [1,0,-1,0,-2,2] => [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# [2,2,2,2,2] => [[2,2,2,2]]
# Time complexity O(nˆ3). For each two pairs of numbers (nˆ2), we look for another
# pair of numbers what has linear O(n) complexity 
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    results = []
    n = len(nums)
    nums.sort()
    for i1 in range(n - 3):
        # Skip duplicates
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        for i2 in range(i1 + 1, n - 2):
            # Skip duplicates only if we are not at initial iteration. Why?
            # because if we move two pointers at once, we could skip a combination
            if i2 > 1 and nums[i2] == nums[i2 - 1] and i2 != i1 + 1:
                continue

            i3, i4 = i2 + 1, n - 1
            subtotal = nums[i1] + nums[i2]
            while i3 < i4:
                if subtotal + nums[i3] + nums[i4] > target:
                    i4 -= 1
                elif subtotal + nums[i3] + nums[i4] < target:
                    i3 += 1
                else:
                    result = [nums[i1], nums[i2], nums[i3], nums[i4]]
                    results.append(result)
                    # Move two pointers at once, because if we moved only one
                    # numbers at i3 and i4 would not sum up with i2, i3 to target
                    while i3 < i4 and nums[i3] == result[2]:
                        i3 += 1
                    while i3 < i4 and nums[i4] == result[3]:
                        i4 -= 1
    return results


# Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in
# any order. A mapping of digits to letters (just like on the telephone
# buttons) is given below. Note that 1 does not map to any letters.
# "23" => ["ad","ae","af","bd","be","bf","cd","ce","cf"]
from typing import List

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
def letterCombinations(digits: str) -> List[str]:
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


# Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end
# of the list and return its head.
# head = [1,2,3,4,5], n=2 => [1,2,3,5]
# head = [1], n=1 => []
# head = [1,2], n=1 => [1]
from typing import List, Optional
def list_len(head):
    if head is None:
        return 0

    count = 1
    while head.next:
        count += 1
        head = head.next
    return count

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Index for node to remove
    length = list_len(head)
    index = length - n
    
    # In case index to remove is not valid
    if index < 0:
        raise ValueError

    prev, curr = head, head
    for i in range(index):
        prev = curr
        curr = curr.next

    prev.next = curr.next
    if prev is curr:
        return curr.next
    
    return head


# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
OPENING = ['(', '{', '[']
CLOSING = [')', '}', ']']

def isValid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket in CLOSING:
            try:
                idx = CLOSING.index(bracket)
                value = stack.pop()
                if value != OPENING[idx]:
                    return False
            except IndexError:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0


# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists. Return the head of
# the merged linked list.
from typing import Optional

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(None)
    merged = head
    while list1 and list2:
        if list1.val < list2.val:
            merged.next = list1
            list1 = list1.next
        else:
            merged.next = list2
            list2 = list2.next
        merged = merged.next
    
    if list1:
        merged.next = list1
    elif list2:
        merged.next = list2

    return head.next


# Generate Parenthesis
# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.
# Let F(n) denote valid strings of length 2n. The problem F(n) can be decomposed
# into smaller subproblems of generating valid strings of smaller lengths. By
# leveraging solutions to these subproblems we can construct solution for the original
# problem. We can decompose F(n) into F(0)+F(n), F(1)+F(n-1) ... F(n)+F(0), but problem
# F(n) repeats itself (it is computed multiple times). Instead, we can use
# '( F[0] ) + F[n-1]', '( F[1] ) + F[n - 2]' ... '( F[n - 1] ) + F[0]'
# Number of solutions is the same as nth Catalan number. Time complexity is
# O(4ˆn / sqrt(n)) and space complexity O(n)
def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return [""]
    
    answer = []
    for left_count in range(n):
        for left_string in generateParenthesis(left_count):
            for right_string in generateParenthesis(n - 1 - left_count):
                answer.append("(" + left_string + ")" + right_string)
    
    return answer


# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# [1, 2, 3, 4] => [2, 1, 4, 3]
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return
    
    prev = ListNode(None)
    final = head.next or head
    while head:
        next = head.next
        if next is None:
            break
        
        head.next = next.next
        next.next = head
        prev.next = next

        prev = head
        head = head.next

    return final


# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same. Then return the
# number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:
# * Change the array nums such that the first k elements of nums contain the
# unique elements in the order they were present in nums initially. The
# remaining elements of nums are not important as well as the size of nums.
# * Return k
def removeDuplicates(nums: List[int]) -> int:
    place = None
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            if place is None:
                place = i
            continue
        
        if place:
            nums[place] = nums[i]
            place += 1
    
    return place if place else len(nums)


# Remove Element
# Given an integer array nums and an integer val, remove all occurrences of
# val in nums in-place. The order of the elements may be changed. Then return
# the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:
# * Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# * Return k.
def removeElement(nums: List[int], val: int) -> int:
    place = None
    for i in range(len(nums)):
        if place is None and nums[i] == val:
            place = i
        elif place is not None and nums[i] != val:
            nums[place] = nums[i]
            place = place + 1

    return place if place is not None else len(nums)


# Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or
# linear order. For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]. The next permutation of
# an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container according
# to their lexicographical order, then the next permutation of that array is the permutation
# that follows it in the sorted container. If such arrangement is not possible, the array must
# be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a
# lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
# The replacement must be in place and use only constant extra memory.
def bisect(nums, value):
    """ 
        Returns index i such that values a[:i] are higher than value
        and values in a[i:] are lower or equal than value
    """
    i, j = 0, len(nums)
    while i < j:
        k = (i + j) // 2
        if nums[k] <= value:
            j = k
        else:
            i = k + 1
    
    return i

def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    if n == 1:
        return

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break
    else:
        # Digits sorted in decreasing order, reverse them
        nums.reverse()
        return

    # Else find the closest higher digit and replace them
    pos = bisect(nums[i + 1:], nums[i]) -1 + i + 1
    nums[i], nums[pos] = nums[pos], nums[i]

    # Once replaced, reverse order to ascending
    j, k = i + 1, n - 1
    while j < k:
        nums[j], nums[k] = nums[k], nums[j]
        j = j + 1
        k = k - 1

    return


# Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values). Prior to
# being passed to your function, nums is possibly rotated at an unknown pivot index k
# (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index
# of target if it is in nums, or -1 if it is not in nums. You must write an algorithm with
# O(log n) runtime complexity.
# nums = [4,5,6,7,0,1,2], target = 0 => 4
# nums = [4,5,6,7,0,1,2], target = 3 => -1
# nums = [1], target = 0 => -1

# First try
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1

    # Find number of rotations performed
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            break
    else:
        i = 0
    rotations = (n - i) % n

    # Translation layer for indices
    def tr(index, n, k):
        if index >= k:
            return index - k
        return index + n - k

    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        tr_mid = tr(mid, n, rotations)
        mid_value = nums[tr_mid]

        if mid_value == target:
            return tr_mid
        elif mid_value > target:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1

# Final solution
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0:
        return -1

    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] > nums[-1]:
            i = mid + 1
        else:
            j = mid - 1

    shift = n - i

    i, j = 0, n - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[(mid - shift) % n] == target:
            return (mid - shift) % n
        elif nums[(mid - shift) % n] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1


# There are n people in a social group labeled from 0 to n - 1. You are given an array logs
# where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time
# timestamp. Friendship is symmetric. That means if a is friends with b, then b is friends
# with a. Also, person a is acquainted with a person b if a is friends with b, or a is a
# friend of someone acquainted with b. Return the earliest time for which every person became
# acquainted with every other person. If there is no such earliest time, return -1.
# Time complexity:
# * O(n) - creating sets
# * O(m * logm) - sorting logs
# * O(m * alpha(n)) - m FIND, UNION operations
# => O(n + mlogm + m * alpha(n))
# Space complexity: O(n + m) - n sets + m logs (timsort)
class unionfind:
    """
        Union find with path compression and union by rank. Time complexity
        for m MAKE-SET, FIND and UNION operations out which n are MAKE-SET
        and at most n - 1 UNION is O(m * alpha(n))
    
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.ranks = [0] * n

    def make_set(self):
        self.parent.append(len(self.parent))
        self.ranks.append(0)
        return self.parent[-1]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return False

        if self.ranks[i] > self.ranks[j]:
            i, j = j, i

        self.parent[i] = j
        if self.ranks[i] == self.ranks[j]:
            self.ranks[j] += 1
        
        return True

    def issame(self, i, j):
        return self.find(i) == self.find(j)

    def groups(self):
        r = range(len(self.parent))
        return [[j for j in r if self.issame(j, i)] for i in r if i == self.parent[i]]

    def __len__(self):
        return sum([i == parent for i, parent in enumerate(self.parent)])

def earliestAcq(logs: List[List[int]], n: int) -> int:
    # We need at least n - 1 union operations
    if len(logs) < n - 1:
        return - 1

    # No people or one person form a social group implicitely
    if n < 2:
        return - 1

    # Logs need to be in a chronological order
    logs.sort(key=lambda x: x[0])

    u = unionfind(n)
    for timestamp, f1, f2 in logs:
        if u.union(f1, f2):
            n = n - 1
        if n == 1:
            return timestamp

    return -1
