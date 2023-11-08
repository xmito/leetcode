from typing import List

# Insert Interval (Medium)
# You are given an array of non-overlapping intervals where
# intervals[i] = [starti, endi] represent the start and the end of the
# ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents
# the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary). Return intervals after
# the insertion.
# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 105
# intervals is sorted by start_i in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

# Time complexity: O(n), binary search in O(logn), but actual worst case for merging is O(n)
# Space complexity: O(1)
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
        return [newInterval]

    # Find position i such that intervals[:i] have start
    # lower than start from interval we want to insert
    start = newInterval[0]
    i, j = 0, len(intervals) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if intervals[mid][0] < start:
            # position i will be at most first value equal to start
            i = mid + 1
        else:
            j = mid - 1
    
    # Interval (x_i-1, y_i-1) on position i - 1 has strictly smaller start value
    # x_i-1 < x_i but its end value y_i-1 can be y_i-1 > x_i and thus overlap with
    # interval (x_i, y_i) we are trying to insert. Any other interval on position
    # i - 2 or lower cannot overlap with inserted interval because we have
    # y_i-2 < x_i-1 (intervals in list are not overlapping)
    if i > 0 and intervals[i - 1][1] >= newInterval[0]:
        merged = [
            min(intervals[i - 1][0], newInterval[0]),
            max(intervals[i - 1][1], newInterval[1]),
        ]
        end = i - 1
    else:
        merged = newInterval
        end = i

    begin = i
    for begin in range(i, len(intervals)):
        x1, y1 = merged
        x2, y2 = intervals[begin]
        if y1 < x2:
            break
        merged = [x1, max(y1, y2)]
    else:
        # If the last interval from intervals was merged, than
        # we don't want to include it in the final result
        begin = begin + 1

    return intervals[:end] + [merged] + intervals[begin:]


if __name__ == "__main__":
    res = insert([], [2,5])
    print(res)
    assert res == [[2,5]]

    res = insert([[1,5]], [1,7])
    print(res)
    assert res == [[1,7]]

    res = insert([[1,5]], [2,3])
    print(res)
    assert res == [[1,5]]

    res = insert([[1,3],[6,9]], [2,5])
    print(res)
    assert res == [[1,5],[6,9]]

    res = insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    print(res)
    assert res == [[1,2],[3,10],[12,16]]