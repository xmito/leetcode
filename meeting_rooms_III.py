import heapq
from typing import List

# Meeting Rooms III (Hard)
# You are given an integer n. There are n rooms numbered from 0 to n - 1.
# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means
# that a meeting will be held during the half-closed time interval [starti, endi).
# All the values of starti are unique.
# Meetings are allocated to rooms in the following manner:
# * Each meeting will take place in the unused room with the lowest number.
# * If there are no available rooms, the meeting will be delayed until a room becomes
# free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should
# be given the room.
# Return the number of the room that held the most meetings. If there are multiple
# rooms, return the room with the lowest number.
# A half-closed interval [a, b) is the interval between a and b including a and not
# including b.
# Constraints:
# 1 <= n <= 100
# 1 <= meetings.length <= 10ˆ5
# meetings[i].length == 2
# 0 <= starti < endi <= 5 * 10ˆ5
# All the values of starti are unique.


# Time complexity: O(m * lognm) where m is number of meetings and n is number of rooms:
# Sorting of m meetings costs O(m * logm) 
# For each meeting, we extract and insert room once from both available_rooms and
# occupied_rooms over all iterations of for loop. Once insert/extract operation costs
# O(logn) and we do 4m of them what has complexity bound O(m * logn)
# Combined time complexity is thus O(m * logm + m * logn) => O(m * lognm)
# Space complexity: O(m + n) - heaps and memory used during sorting of meetings
def mostBooked(n: int, meetings: List[List[int]]) -> int:
    meetings.sort(key=lambda x: x[0])
    occupied_rooms = []
    available_rooms = [i for i in range(n)]
    count = [0] * n

    for start, end in meetings:
        while occupied_rooms and occupied_rooms[0][0] <= start:
            _, room = heapq.heappop(occupied_rooms)
            heapq.heappush(available_rooms, room)

        if available_rooms:
            room = heapq.heappop(available_rooms)
            heapq.heappush(occupied_rooms, (end, room))
        else:
            new_end, room = heapq.heappop(occupied_rooms)
            duration = end - start
            heapq.heappush(occupied_rooms, (new_end + duration, room))

        count[room] += 1

    return count.index(max(count))


if __name__ == "__main__":
    res = mostBooked(2, [[4,11],[1,13],[8,15],[9,18],[0,17]])
    print(res)
    assert res == 1

    res = mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]])
    print(res)
    assert res == 0

    res = mostBooked(2, [[10,11],[2,10],[1,17],[9,13],[18,20]])
    print(res)
    assert res == 1

    # At time 0, both rooms are not being used. The first meeting starts in room 0.
    # At time 1, only room 1 is not being used. The second meeting starts in room 1.
    # At time 2, both rooms are being used. The third meeting is delayed.
    # At time 3, both rooms are being used. The fourth meeting is delayed.
    # At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
    # At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
    # Both rooms 0 and 1 held 2 meetings, so we return 0. 
    res = mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])
    print(res)
    assert res == 0

    # At time 1, all three rooms are not being used. The first meeting starts in room 0.
    # At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
    # At time 3, only room 2 is not being used. The third meeting starts in room 2.
    # At time 4, all three rooms are being used. The fourth meeting is delayed.
    # At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
    # At time 6, all three rooms are being used. The fifth meeting is delayed.
    # At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
    # Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
    res = mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
    print(res)
    assert res == 1
