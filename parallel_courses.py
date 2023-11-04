from enum import Enum
from typing import List
from graphlib import TopologicalSorter, CycleError

# Parallel Courses (Medium)
# You are given an integer n, which indicates that there are n courses labeled from 1 to n.
# You are also given an array relations where relations[i] = [prevCoursei, nextCoursei],
# representing a prerequisite relationship between course prevCoursei and course nextCourse:
# course prevCoursei has to be taken before course nextCoursei. In one semester, you can take
# any number of courses as long as you have taken all the prerequisites in the previous semester
# for the courses you are taking. Return the minimum number of semesters needed to take all
# courses. If there is no way to take all the courses, return -1.


# Simple solution using graphlib TopologicalSorter datastructure
def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    if not relations:
        return 0

    # Create dictionary holding predecessors for each node
    graph = {}
    for prev, nxt in relations:
        graph.setdefault(nxt, [])
        graph[nxt].append(prev)

    # Prepare graph and check for cycles
    try:
        ts = TopologicalSorter(graph=graph)
        ts.prepare()
    except CycleError:
        return -1

    semesters = 0
    while ts:
        layer = ts.get_ready()
        if not layer:
            break
        for node in layer:
            ts.done(node)
        semesters += 1
    
    return semesters


def DfsMinimumSemesters(n: int, relations: List[List[int]]) -> int:
    """
        Solution that uses DFS algorithm
        Time complexity: O(|V| + |E|)
        Space complexity: O(|V| + |E|)
    """
    class Color(Enum):
        WHITE = 1
        GREY = 2
        BLACK = 3

    class CycleException(Exception):
        pass
    
    # Create adjacency lists
    graph = {i: [] for i in range(1, n + 1)}
    for start, end in relations:
        graph[start].append(end)

    visited = {i: Color.WHITE for i in range(1, n + 1)}
    longest = {i: 0 for i in range(1, n + 1)}

    def dfs_visit(node):
        if visited[node] == Color.GREY:
            raise CycleException
        elif visited[node] == Color.BLACK:
            return longest[node]
        
        visited[node] = Color.GREY

        max_length = 1
        for neighbor in graph[node]:
            length = dfs_visit(neighbor)
            max_length = max(max_length, length + 1)

        visited[node] = Color.BLACK
        longest[node] = max_length
        return longest[node]

    try:
        max_length = 0
        for node in range(1, n + 1):
            length = dfs_visit(node)
            max_length = max(max_length, length)
        return max_length
    except CycleException:
        return -1

            
def KahnMinimumSemesters(n: int, relations: List[List[int]]) -> int:
    """
        Solution that uses Kahn's algorithm (BFS)
        Time complexity: O(|V| + |E|)
        Space complexity: O(|V| + |E|)
    """
    # Indegree and adjacency-lists O(|V|)
    indegree = {i: 0 for i in range(1, n + 1)}
    graph = {i: [] for i in range(1, n + 1)}

    # Iterate over edges and initialize graph O(|E|)
    for start, end in relations:
        indegree[end] += 1
        graph[start].append(end)

    # Courses which have no prerequisite can be taken in one semester
    # Initialize queue with vertices that have zero indegree O(|V|)
    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # Do topological sorting. Each vertex is enqueud and dequeued exactly once.
    # Each directed edge is considered exactly once
    # O(|V| + |E|)
    nqueue = []
    semesters = 0
    while True:
        while queue:
            node = queue.pop()
            try:
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        nqueue.append(neighbor)
            except KeyError:
                pass

        semesters += 1
        if not nqueue:
            break
        queue, nqueue = nqueue, queue
    
    # If any node has indegree higher than 0, it means there is a cycle
    # and there's no possibility to tak all courses, return -1
    for degree in indegree.values():
        if degree:
            return -1

    return semesters

if __name__ == '__main__':
    relations = [[1,5],[2,3],[2,5],[2,4],[2,1],[5,3]]
    res = DfsMinimumSemesters(5, relations)
    print(res)
    assert res == 4

    relations = [[5,10],[11,14],[21,22],[16,19],[21,25],[6,18],[1,9],[4,7],[10,23],[5,14],[9,18],[18,21],[11,22],[1,15],[1,2],[5,18],[7,20],[2,23],[12,13],[9,14],[10,16],[11,21],[5,12],[2,24],[8,17],[15,17],[10,13],[11,16],[20,22],[7,11],[9,15],[16,22],[18,20],[19,22],[10,18],[3,20],[16,25],[10,15],[1,23],[13,16],[23,25],[1,8],[4,10],[19,24],[11,20],[3,18],[6,25],[11,13],[13,15],[22,24],[6,24],[17,20],[2,25],[15,24],[8,21],[14,16],[5,16],[19,23],[1,5],[4,22],[19,20],[12,15],[16,18],[9,13],[13,22],[14,22],[2,8],[3,13],[9,23],[14,15],[14,17],[8,20],[9,17],[3,19],[8,25],[2,12],[7,24],[19,25],[1,13],[6,11],[14,21],[7,15],[3,14],[15,23],[10,17],[4,20],[6,14],[10,21],[2,13],[3,21],[8,11],[5,21],[6,23],[17,25],[16,21],[12,22],[1,16],[6,19],[7,25],[3,23],[11,25],[3,10],[6,7],[2,3],[5,25],[1,6],[4,17],[2,16],[13,17],[17,22],[6,13],[5,6],[4,11],[4,23],[4,8],[12,23],[7,21],[5,20],[3,24],[2,10],[13,14],[11,24],[1,3],[2,7],[7,23],[6,17],[5,17],[16,17],[8,15],[8,23],[7,17],[14,18],[16,23],[23,24],[4,12],[17,19],[5,9],[10,11],[5,23],[2,9],[1,19],[2,19],[12,20],[2,14],[11,12],[1,12],[13,23],[4,9],[7,13],[15,20],[21,24],[8,18],[9,11],[8,19],[6,22],[16,20],[22,25],[20,21],[6,16],[3,17],[1,22],[9,22],[20,24],[2,6],[9,16],[2,4],[2,20],[20,25],[9,10],[3,11],[15,18],[1,20],[3,6],[8,14],[10,22],[12,21],[7,8],[8,16],[9,20],[3,8],[15,21],[17,21],[11,18],[13,24],[17,24],[6,20],[4,15],[6,15],[3,22],[13,21],[2,22],[13,25],[9,12],[4,19],[1,24],[12,19],[5,8],[1,7],[3,16],[3,5],[12,24],[3,12],[2,17],[18,22],[4,25],[8,24],[15,19],[18,23],[1,4],[1,21],[10,24],[20,23],[4,14],[16,24],[10,20],[18,24],[1,14],[12,14],[10,12],[4,16],[5,19],[4,5],[19,21],[15,25],[1,18],[2,21],[4,24],[7,14],[4,6],[15,16],[3,7],[21,23],[1,17],[12,16],[13,18],[5,7],[9,19],[2,15],[22,23],[7,19],[17,23],[8,22],[11,17],[7,16],[8,9],[6,21],[4,21],[4,13],[14,24],[3,4],[7,18],[11,15],[5,11],[12,17],[6,9],[1,25],[12,18],[6,12],[8,10],[6,8],[11,23],[7,10],[14,25],[14,23],[12,25],[5,24],[10,19],[3,25],[7,9],[8,12],[5,22],[24,25],[13,19],[3,15],[5,15],[15,22],[10,14],[3,9],[13,20],[1,10],[9,21],[10,25],[9,24],[14,20],[9,25],[8,13],[7,12],[5,13],[6,10],[2,5],[2,18],[14,19],[1,11],[7,22],[18,25],[11,19],[18,19],[4,18],[17,18],[2,11]]
    res = DfsMinimumSemesters(25, relations)
    print(res)
    assert res == 25

    relations = [[1,3],[2,3]]
    res = DfsMinimumSemesters(3, relations)
    print(res)
    assert res == 2

    relations = [[1,2],[2,3],[3,1]]
    res = DfsMinimumSemesters(3, relations)
    print(res)
    assert res == -1