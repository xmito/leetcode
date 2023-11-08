from typing import List

# Merge Intervals (Medium)
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
# intervals, and return an array of the non-overlapping intervals that cover all the
# intervals in the input.
# Constraints:
# 1 <= intervals.length <= 10ˆ4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10ˆ4

# Time complexity: O(nlogn) because of sorting
# Space complexity: O(n) timsort space complexity
def merge(intervals: List[List[int]]) -> List[List[int]]:
    results = []
    if not intervals:
        return results

    intervals = sorted(intervals)
    merged = intervals[0]
    for i in range(1, len(intervals)):
        x1, y1 = merged
        x2, y2 = intervals[i]
        if y1 < x2:
            results.append(merged)
            merged = intervals[i]
            continue
        merged = [min(x1, x2), max(y1, y2)]

    results.append(merged)
    return results

# Lemma: Algorithm merges all intervals that overlap
# Proof by contradiction:
# Suppose not, iow. that there are at least two overlapping intervals
# that are not merged when the algorithm finishes. Let's denote these
# two intervals as (x1, y1) and (x3, y3). In order for them to be not
# merged, there has to be another interval (x2, y2) inbetween, that
# does not overlap with (x1, y1) and y1 < x2. However, since all
# intervals are sorted, we know that x2 <= x3 and y1 < x2 <= x3,
# which contradicts assumption that intervals (x1, y1) a (x3, y3)
# are overlapping

if __name__ == "__main__":
    res = merge([[1,3],[2,6],[8,10],[15,18]])
    print(res)
    assert res == [[1,6],[8,10],[15,18]]

    res = merge([[1,4],[4,5]])
    print(res)
    assert res == [[1,5]]
