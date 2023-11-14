from typing import List
from collections import defaultdict

# Employee Free Time (Hard)
# We are given a list schedule of employees, which represents the working time for
# each employee. Each employee has a list of non-overlapping Intervals, and these
# intervals are in sorted order. Return the list of finite intervals representing
# common, positive-length free time for all employees, also in sorted order. Even
# though we are representing Intervals in the form [x, y], the objects inside are
# Intervals, not lists or arrays. For example, schedule[0][0].start = 1,
# schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't
# include intervals like [5, 5] in our answer, as they have zero length.
# Constraints:
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
    
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


def merge(i1: List[Interval], i2: List[Interval]) -> List[Interval]:
    j, k = 0, 0
    result = []
    while j < len(i1) and k < len(i2):
        # if max(i1[j].start, i2[k].start) <= min(i1[j].end, i2[k].end):
        if not (i1[j].start > i2[k].end or i2[k].start > i1[j].end):
            start = min(i1[j].start, i2[k].start)
            end = max(i1[j].end, i2[k].end)
            interval = Interval(start, end)
            j += 1
            k += 1
        elif i1[j].start < i2[k].start:
            interval = i1[j]
            j += 1
        else:
            interval = i2[k]
            k += 1

        if not result or interval.start > result[-1].end:
            result.append(interval)
        else:
            result[-1].end = max(result[-1].end, interval.end)

    while j < len(i1):
        if not result or i1[j].start > result[-1].end:
            result.append(i1[j])
        else:
            result[-1].end = max(result[-1].end, i1[j].end)
        j += 1

    while k < len(i2):
        if not result or i2[k].start > result[-1].end:
            result.append(i2[k])
        else:
            result[-1].end = max(result[-1].end, i2[k].end)
        k += 1

    return result


def merge_list(intervals: List[List[Interval]]) -> List[Interval]:
    """ Merge lists of intervals into one list """
    if len(intervals) == 1:
        return intervals[0]
    elif len(intervals) == 2:
        return merge(intervals[0], intervals[1])

    mid = len(intervals) // 2
    return merge(
        merge_list(intervals[:mid + 1]),
        merge_list(intervals[mid + 1:]),
    )


# Time complexity: O(nk * logn) where n is number of people and k is the most intervals per person
# Space complexity: O(nk)
def employeeFreeTimeRecursive(schedule: List[List[Interval]]) -> List[Interval]:
    # Merge sorted intervals lists into one list in O(nk * logn) where n is number of
    # people and k is the most intervals for one person. We have logn recursion depth
    # and at each level we merge two lists with 2^i*k (assuming there are no overlaps)
    # 2^(logn - 1) * 2k => 2^logn * k => nk
    # 2^(logn - 2) * 4k => 2^logn * k => nk
    # ...
    # Complexity is O(nk * logn)
    merged = merge_list(schedule)
    
    # Find free time intervals in O(nk)
    results = []
    for i1, i2 in zip(merged[:-1], merged[1:]):
        results.append(Interval(i1.end, i2.start))

    return results


# Sweep line solution:
# 1. Store two ends of intervals of all employees into a map, where the value of start
# point and end point is 1 and -1, respectively.
# 2. Sort the key-value pair of the map based on the key.
# 3. Traverse the sorted pair, maintain the count by adding the value of the key-value pair.
# 4. When the count becomes 0, the current timestamp is the start point of a free time period. Record it.
# 5. When the count becomes non-0, if we have recorded a start point, then the current
# timestamp is the end point of that free time period. Append them into the result list,
# and clear the record of that start point.
# Time complexity: O(nk * lognk) n persons, k intervals
# Space complexity: O(nk)
# Correctness:
# Lemma: If count reaches 0 at timestamp t, the it is start time of free-time interval
# Proof: Suppose not, iow. count reaches 0 at timestamp t and it is not start time of free
# interval. Then there should exist work-time interval (s, e) such that t>=s and t<e.
# Then the count cannot be zero, because at timestamp t, we have not yet closed work-time
# interval and count must be at least 1, what contradicts our assumption that count is zero
# Lemma: Once count reaches non-zero value at timestamp x, after being zero, we have
# end-time for free-time interval
# Proof: Correctness comes from the previous lemma, because timestamp t is not in any
# work-time interval and when the count is increased at timestamp x, we hit work-time
# interval with the smallest start time larger than t, which is x
def employeeFreeTimeSweep(schedule: '[[Interval]]') -> '[Interval]':
    time = defaultdict(int)
    for employee in schedule:
        for interval in employee:
            time[interval.start] += 1
            time[interval.end] -= 1
    result = []
    count = 0
    start = None
    for index, value in sorted(time.items()):
        count += value
        if count == 0:
            start = index
        elif start != None:
            result.append(Interval(start, index))
            start = None
    return result


if __name__ == "__main__":
    schedule = [[Interval(45,56), Interval(89,96)], [Interval(5,21), Interval(57,74)]]
    res = employeeFreeTimeRecursive(schedule)
    assert res == [Interval(21,45), Interval(56,57), Interval(74,89)]

    schedule = [[Interval(1,2), Interval(5,6)], [Interval(1,3)], [Interval(4,10)]]
    res = employeeFreeTimeRecursive(schedule)
    assert res == [Interval(3,4)]

    schedule = [[Interval(1,3), Interval(6,7)], [Interval(2,4)], [Interval(2,5), Interval(9,12)]]
    res = employeeFreeTimeRecursive(schedule)
    assert res == [Interval(5,6), Interval(7,9)]


    schedule = [[Interval(45,56), Interval(89,96)], [Interval(5,21), Interval(57,74)]]
    res = employeeFreeTimeSweep(schedule)
    assert res == [Interval(21,45), Interval(56,57), Interval(74,89)]

    schedule = [[Interval(1,2), Interval(5,6)], [Interval(1,3)], [Interval(4,10)]]
    res = employeeFreeTimeSweep(schedule)
    assert res == [Interval(3,4)]

    schedule = [[Interval(1,3), Interval(6,7)], [Interval(2,4)], [Interval(2,5), Interval(9,12)]]
    res = employeeFreeTimeSweep(schedule)
    assert res == [Interval(5,6), Interval(7,9)]