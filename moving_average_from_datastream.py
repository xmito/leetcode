from collections import deque

# Moving Average From Datastream (Easy)
# Given a stream of integers and a window size, calculate the moving average of all
# integers in the sliding window. Implement the MovingAverage class:
# * MovingAverage(int size) Initializes the object with the size of the window size.
# * double next(int val) Returns the moving average of the last size values of the stream.
# Constraints:
# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    # Time complexity: O(1)
    # Space complexity: O(n)
    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.window.append(val)
            prev = self.window.popleft()

            self.window_sum -= prev - val
            return self.window_sum / self.size

        self.window.append(val)
        self.window_sum += val
        return self.window_sum / len(self.window)


class MovingAverageCyclic:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    # Time complexity: O(1)
    # Space complexity: O(n)
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


if __name__ == "__main__":
    ma = MovingAverage(3)
    # return 1 / 1 = 1.0
    res = ma.next(1)
    print(res)
    assert res == 1.0

    # return 5.5 = (1 + 10) / 2
    res = ma.next(10)
    print(res)
    assert res == 5.5

    # return 4.66667 = (1 + 10 + 3) / 3
    res = ma.next(3)
    print(res)
    assert res == 4.666666666666667

    # return 6.0 = (10 + 3 + 5) / 3
    res = ma.next(5)
    print(res)
    assert res == 6.0
