from typing import List

# The Earliest Moment When Everyone Become Friend (Medium)
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


if __name__ == '__main__':
    logs = [[1,3,2],[0,2,0]]
    res = earliestAcq(logs, 4)
    print(res)
    assert res == -1

    logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
    res = earliestAcq(logs, n=4)
    print(res)
    assert res == 3

    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
    res = earliestAcq(logs, n=6)
    print(res)
    assert res == 20190301

    logs = [[9,0,3],[0,2,7],[12,3,1],[5,5,2],[3,4,5],[1,5,0],[6,2,4],[2,5,3],[7,7,3]]
    res = earliestAcq(logs, 8)
    print(res)
    assert res == -1
