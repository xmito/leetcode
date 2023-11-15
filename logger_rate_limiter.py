from collections import deque

# Logger Rate Limiter (Easy)
# Design a logger system that receives a stream of messages along with their timestamps.
# Each unique message should only be printed at most every 10 seconds (i.e. a message
# printed at timestamp t will prevent other identical messages from being printed
# until timestamp t + 10).
# All messages will come in chronological order. Several messages may arrive at the
# same timestamp. Implement the Logger class:
# * Logger() Initializes the logger object.
# * bool shouldPrintMessage(int timestamp, string message) Returns true if the message
# should be printed in the given timestamp, otherwise returns false.
# Constraints:
# 0 <= timestamp <= 10ˆ9
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 10ˆ4 calls will be made to shouldPrintMessage.
    
class Logger:

    def __init__(self):
        self.queue = deque()
        self.messages = set()

    # Time complexity: O(n) - one call may expire all stored messages. However, in one
    # call, it can remove only those messages that had been added prior. Using aggregate
    # analysis, amortized complexity for single operation is O(1)
    # Space complexity: O(n * m) - deque and messages set (n messages with length at most)
    # Without cleaning messages, we could do this in O(1) with single dictionary,
    # but the required memory would grow infinitely
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Use min-heap to store messages based on end-time
        while self.queue:
            if self.queue[0][0] > timestamp:
                break
            
            finish, text = self.queue.popleft()
            self.messages.remove(text)
            
        if message in self.messages:
            return False
    
        self.messages.add(message)
        self.queue.append((timestamp + 10, message))
        return True


if __name__ == "__main__":
    logger = Logger()
    # Return true, next allowed timestamp for "foo" is 1 + 10 = 11
    assert logger.shouldPrintMessage(1, "foo") == True

    # Return true, next allowed timestamp for "foo" is 1 + 10 = 11
    assert logger.shouldPrintMessage(2, "bar") == True

    # 3 < 11, return false
    assert logger.shouldPrintMessage(3, "foo") == False

    # 8 < 12, return false
    assert logger.shouldPrintMessage(8, "bar") == False

    # 10 < 11, return false
    assert logger.shouldPrintMessage(10, "foo") == False
    
    # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
    assert logger.shouldPrintMessage(11, "foo") == True
