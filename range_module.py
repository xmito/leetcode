from typing import List
from bisect import bisect_left, bisect_right

from sortedcontainers import SortedSet

# Range Module (Hard)
# A Range Module is a module that tracks ranges of numbers. Design a data structure to
# track the ranges represented as half-open intervals and query about them. A half-open
# interval [left, right) denotes all the real numbers x where left <= x < right.
# Implement the RangeModule class:
# * RangeModule() Initializes the object of the data structure.
# * void addRange(int left, int right) Adds the half-open interval [left, right), tracking
# every real number in that interval. Adding an interval that partially overlaps with
# currently tracked numbers should add any numbers in the interval [left, right) that
# are not already tracked.
# * boolean queryRange(int left, int right) Returns true if every real number in the
# interval [left, right) is currently being tracked, and false otherwise.
# * void removeRange(int left, int right) Stops tracking every real number currently
# being tracked in the half-open interval [left, right).
# Constraits:
# 1 <= left < right <= 10ˆ9
# At most 10ˆ4 calls will be made to addRange, queryRange, and removeRange.

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def covers(self, other):
        return self.start <= other.start and other.end <= self.end

    def __lt__(self, other):
        """ Intervals are not overlapping and consecutive """
        return self.end < other.start

    def __le__(self, other):
        """ Intervals are not overlapping but can be consecutive """
        return self.end <= other.start
    
    def __gt__(self, other):
        """ Intervals are not overlapping and consecutive """
        return self.start > other.end

    def __ge__(self, other):
        """ Intervals are not overlapping but can be consecutive """
        return self.start >= other.end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end
       

class RangeNode(Range):
    def __init__(self, start, end, left=None, right=None, height=None):
        super().__init__(start, end)
        self.left = left
        self.right = right
        self.height = height if height else 1

    def query(self, other: Range):
        if self.covers(other):
            return True

        if self > other:
            if self.left:
                return self.left.query(other)
            return False
        elif self < other:
            if self.right:
                return self.right.query(other)
            return False

        left, right = True, True
        if self.end < other.end:
            right = self.right.query(Range(self.end, other.end))
        if other.start < self.start:
            left = self.left.query(Range(other.start, self.start))

        return left and right

    def add(self, other: Range):
        if self > other:
            if self.left:
                self.left.add(other)
            else:
                self.left = RangeNode(other.start, other.end)
        elif self < other:
            if self.right:
                self.right.add(other)
            else:
                self.right = RangeNode(other.start, other.end)
        else:
            # Ranges overlap
            # if other.end > self.end, look for node in the right subtree that covers other.end. If there
            # is such, take its end as a new end for this node. Otherwise take other.end
            # as new end for this node
            if other.end > self.end:
                end = None
                prev = self
                x = self.right
                while x:
                    if other.end >= x.end:
                        # other range covers node x, x will be removed along with its
                        # whole left subtree
                        if x is prev.left:
                            prev.left = x.right
                        elif x is prev.right:
                            prev.right = x.right

                        # prev.left = x.right
                        x = x.right
                    elif other.end < x.start:
                        # other range does not cover this node, it will stay
                        prev = x
                        x = x.left
                    else:
                        end = x.end
                        if x is prev.right:
                            prev.right = x.right
                        elif x is prev.left:
                            prev.left = x.right
                        break
                
                self.end = end if end else other.end

            if other.start < self.start:
                start = None
                prev = self
                x = self.left
                while x:
                    if other.start < x.start:
                        # other range covers node x, x will be removed along with its
                        # whole right subtree
                        prev.left = x.left
                        x = x.left
                    elif other.start > x.end:
                        # other range does not cover this node, it will stay
                        prev = x
                        x = x.right
                    else:
                        start = x.start
                        prev.left = x.left
                        break

                self.start = start if start else other.start


    def remove(self, range):
        pass

    def __str__(self):
        return f"RangeNode(({self.start}, {self.end}), left={self.left}, right={self.right})"

class RangeTree:
    def __init__(self):
        self.root = None

    def add(self, range):
        if self.root is None:
            self.root = RangeNode(range.start, range.end)
        else:
            self.root.add(range)

    def remove(self, range):
        pass

    def query(self, range):
        return self.root.query(range)


class RangeModuleBisect:
    def __init__(self):
        # This list will store the endpoints of the ranges in sorted order.
        # Every even-indexed element (0-based) represents a start point,
        # while every odd-indexed element represents an end point.
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        # Find the position to insert 'left' (i) and 'right' (j).
        i, j = bisect_left(self.track, left), bisect_right(self.track, right)
        
        # Modify the list:
        # If i is even, add 'left' as it represents the start of a new range.
        # If j is even, add 'right' as it represents the end of a new range.
        self.track[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        # Find the position just after 'left' (i) and the position for 'right' (j).
        i, j = bisect_right(self.track, left), bisect_left(self.track, right)
        
        # Return True if and only if:
        # 1. i is equal to j, meaning 'left' and 'right' fall into the same range in the list.
        # 2. i is odd, meaning 'left' is within a tracked range.
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        # Find the position to insert 'left' (i) and 'right' (j).
        i, j = bisect_left(self.track, left), bisect_right(self.track, right)
        
        # Modify the list:
        # If i is odd, add 'left' as it now represents the end of a range.
        # If j is odd, add 'right' as it now represents the start of a range.
        self.track[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


# Time complexity:
# queryRange: O(n)
# removeRange: O(n)
# addRange: O(n)
# Space complexity: O(n)
class RangeModuleSimple:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        inserted = False

        for start, end in self.ranges:
            if end < left:
                new_ranges.append([start, end])
            elif right < start:
                if not inserted:
                    new_ranges.append([left, right])
                    inserted = True
                new_ranges.append([start, end])
            else:
                left = min(left, start)
                right = max(right, end)

        if not inserted:
            new_ranges.append([left, right])

        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if start <= left and right <= end:
                return True
            elif end >= right:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []

        for start, end in self.ranges:
            if end <= left or start >= right:
                new_ranges.append([start, end])
            else:
                if start < left:
                    new_ranges.append([start, left])
                if end > right:
                    new_ranges.append([right, end])

        self.ranges = new_ranges


# Time complexity: O(logn) for operations in most cases.
# In special cases, the time complexity cound be O(nlogn). For example delete [1,30]
# for sorted_set_ = [1,10,11,20,21,30], all elements need to be popped.
# Space complexity: O(n)
class RangeModuleSortedSet:
    def __init__(self):
        self.sorted_set_ = SortedSet()

    def addRange(self, left: int, right: int) -> None:
        left_i = self.sorted_set_.bisect_left(left)
        right_i = self.sorted_set_.bisect_right(right)
        # Add [4,5] to [1, 3, 10, 100]. left_i = 2, right_i = 2, add both 4,5.
        # Add [11,12] to [1, 3, 10, 100], left_i = 3, right_i = 3, do nothing since added elements are already tracked.    
        if left_i == right_i:
            if left_i % 2 == 0:
                self.sorted_set_.add(left)
                self.sorted_set_.add(right)
        else:
            # Add [3,10] to [1, 3, 10, 100], left_i = 1, right_i = 3
            # Add [2,11] to [1, 3, 10, 100], left_i = 1, right_i = 3
            # Pop all elements between left_i and right_i since ranges are merged.
            for i in range(left_i, right_i):
                self.sorted_set_.pop(left_i)
            # Add [1,10] to [2, 3, 10, 100], left_i = 0. The left element needs to be added.
            if left_i % 2 == 0:
                self.sorted_set_.add(left)
            # Add [11,101] to [2, 3, 10, 100], right_i = 4. The right element needs to be added.
            if right_i % 2 == 0:
                self.sorted_set_.add(right)

    def queryRange(self, left: int, right: int) -> bool:
        left_i = self.sorted_set_.bisect_right(left)
        right_i = self.sorted_set_.bisect_left(right)
        # Query [2,3] in [1,10], left_i = right_i = 1.    
        return left_i == right_i and left_i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        # Removing could be tricky since elements in the range may not be tracked. 
        # Here the range is first added to sorted_set_ and all elements are tracked. 
        # The range is then deleted.
        self.addRange(left, right)
        left_i = self.sorted_set_.bisect_left(left)
        right_i = self.sorted_set_.bisect_right(right)
        # Remove[1,10] from [1,10], right_i = 2, 10 needs to be popped.
        if right_i % 2 == 0:
            self.sorted_set_.pop(right_i-1)
        # Remove[3,4] from [1,10], right_i = 1, 4 needs to be added to make the sorted_set_ = [1,3,4,10]
        else:
            self.sorted_set_.add(right)
        # Process the right point first since operations for left may change the  "desired" index of the right point.
        # Remove[1,10] from [1,10], left_i = 0, 1 needs to be popped.
        if left_i % 2 == 0:
            self.sorted_set_.pop(left_i)
        # Remove[3,4] from [1,10], left_i = 1, 3 needs to be added to make the sorted_set_ = [1,3,4,10]
        else:
            self.sorted_set_.add(left)


import sys
if __name__ == "__main__":
    rm = RangeModuleBisect()
    rm.addRange(14, 100)
    rm.removeRange(1, 8)
    assert rm.queryRange(77, 80) == True
    assert rm.queryRange(8, 43) == False
    assert rm.queryRange(4, 13) == False
    rm.removeRange(3, 9)
    rm.removeRange(45, 49)
    rm.removeRange(41, 90)
    rm.addRange(58, 79)
    rm.addRange(4, 83)
    rm.addRange(34, 39)
    rm.removeRange(84, 100)
    rm.addRange(8, 9)
    assert rm.queryRange(32, 56) == True
    rm.addRange(35, 46)
    rm.addRange(9, 100)
    assert rm.queryRange(85, 99) == True
    assert rm.queryRange(23, 33) == True
    rm.addRange(10, 31)
    rm.removeRange(15, 45)
    rm.removeRange(52, 70)
    rm.removeRange(26, 42)
    assert rm.queryRange(30, 70) == False
    assert rm.queryRange(60, 69) == False
    rm.addRange(10, 94)
    rm.addRange(2, 89)
    assert rm.queryRange(26, 39) == True
    rm.addRange(46, 93)
    rm.addRange(30, 83)
    rm.removeRange(42, 48)
    rm.addRange(47, 74)
    rm.addRange(39, 45)
    assert rm.queryRange(14, 64) == False
    rm.removeRange(3, 97)
    assert rm.queryRange(16, 34) == False
    rm.removeRange(28, 100)
    rm.addRange(19, 37)
    rm.addRange(27, 91)
    assert rm.queryRange(55, 62) == True
    rm.removeRange(64, 65)
    rm.removeRange(2, 48)
    rm.addRange(55, 78)
    assert rm.queryRange(21, 89) == False
    assert rm.queryRange(31, 76) == False
    rm.removeRange(13, 32)
    rm.removeRange(2, 84)
    rm.removeRange(21, 88)
    assert rm.queryRange(12, 31) == False
    rm.addRange(89, 97)
    rm.removeRange(56, 72)
    rm.removeRange(16, 75)
    assert rm.queryRange(18, 90) == False
    rm.removeRange(46, 60)
    rm.removeRange(20, 62)
    assert rm.queryRange(28, 77) == False
    rm.addRange(5, 78)
    rm.addRange(58, 61)
    rm.removeRange(38, 70)
    assert rm.queryRange(24, 73) == False
    assert rm.queryRange(72, 96) == False
    rm.addRange(5, 24)
    rm.removeRange(43, 49)
    rm.removeRange(2, 20)
    rm.addRange(4, 69)
    rm.addRange(18, 98)
    rm.addRange(26, 42)
    rm.addRange(14, 18)
    assert rm.queryRange(46, 58) == True
    rm.removeRange(16, 90)
    rm.addRange(32, 47)
    rm.addRange(19, 36)
    rm.addRange(26, 78)
    assert rm.queryRange(7, 58) == False
    rm.addRange(42, 54)
    rm.removeRange(42, 83)
    assert rm.queryRange(3, 83) == False
    rm.removeRange(54, 82)
    rm.removeRange(71, 91)
    rm.removeRange(22, 37)
    assert rm.queryRange(38, 94) == False
    assert rm.queryRange(20, 44) == False
    assert rm.queryRange(37, 89) == False
    assert rm.queryRange(15, 54) == False
    assert rm.queryRange(1, 64) == False
    rm.removeRange(63, 65)
    assert rm.queryRange(55, 58) == False
    rm.removeRange(23, 44)
    assert rm.queryRange(25, 87) == False
    rm.addRange(38, 85)
    assert rm.queryRange(27, 71) == False

    rm = RangeModuleBisect()
    rm.addRange(6, 8)
    rm.removeRange(7, 8)
    rm.removeRange(8, 9)
    rm.addRange(8, 9)
    rm.removeRange(1, 3)
    rm.addRange(1, 8)
    assert rm.queryRange(2, 4) == True
    assert rm.queryRange(2, 9) == True
    assert rm.queryRange(4, 6) == True

    rm = RangeModuleBisect()
    rm.addRange(5, 8)
    assert rm.queryRange(3, 4) == False
    rm.removeRange(5, 6)
    rm.removeRange(3, 6)
    rm.addRange(1, 3)
    assert rm.queryRange(2, 3) == True
    rm.addRange(4, 8)
    assert rm.queryRange(2, 3) == True
    rm.removeRange(4, 9)

    # ["RangeModule","addRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","queryRange"]
    # [[],[10,180],[150,200],[250,500],[50,100],[180,300],[600,1000],[50,150],[50,100]]

    sys.exit(0)
    tree = RangeTree()    
    tree.add(Range(50, 54))
    tree.add(Range(72, 78))
    tree.add(Range(30, 34))
    tree.add(Range(20, 25))
    tree.add(Range(40, 45))
    tree.add(Range(60, 61))
    tree.add(Range(64, 68))
    tree.add(Range(63, 64))
    tree.add(Range(69, 70))
    tree.add(Range(58, 59))
    #tree.add(Range(52, 65))
    #tree.add(Range(68, 69))

    globals()["stop"] = True
    tree.add(Range(32, 74))

    rangem = RangeModule()
    rangem.addRange(10, 20)
    rangem.removeRange(14, 16)
    assert rangem.queryRange(10, 14) == True
    assert rangem.queryRange(13, 15) == False
    assert rangem.queryRange(16, 17) == True
