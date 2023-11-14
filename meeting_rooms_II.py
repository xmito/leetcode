import heapq
from typing import List
from collections import defaultdict

# Meeting Rooms (Medium)
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required.
# Constraints:
# 1 <= intervals.length <= 10ˆ4
# 0 <= starti < endi <= 10ˆ6

# Time complexity: O(nlogn) - due to sorting
# Space complexity: O(n) - space for table
def minMeetingRoomsOpen(intervals: List[List[int]]) -> int:
    table = defaultdict(int)
    for start, end in intervals:
        table[start] += 1
        table[end] -= 1
    
    rooms, count = 0, 0
    for _, value in sorted(table.items()):
        count += value
        rooms = max(rooms, count)

    return rooms


# Time complexity: O(nlogn) - due to sorting
# Space complexity: O(n) - sorted intervals
# Loop invariant: At the start of each iteration where start[i] < end[j], there
# are i - j meetings currently taking place and i - j rooms are required
def minMeetingRooms(intervals: List[List[int]]) -> int:
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    i, j = 0, 0
    rooms = 0
    count = 0

    while i < len(intervals):
        if start[i] >= end[j]:
            count -= 1
            j += 1

        count += 1
        rooms = max(rooms, count)
        i += 1

    return rooms


# Time complexity: O(nlogn)
# Space complexity: O(n)
def minMeetingRoomsHeap(intervals: List[List[int]]) -> int:
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key=lambda x: x[0])

    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)


if __name__ == "__main__":
    res = minMeetingRooms([[1,8],[6,20],[9,16],[13,17]])
    print(res)
    assert res == 3

    res = minMeetingRooms([[0,30],[5,10],[15,20]])
    print(res)
    assert res == 2

    res = minMeetingRooms([[7,10],[2,4]])
    print(res)
    assert res == 1