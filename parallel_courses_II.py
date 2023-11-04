import sys
from typing import List
from itertools import combinations
from functools import lru_cache

# Parallel Courses II (Hard)
# You are given an integer n, which indicates that there are n courses labeled from 1 to n.
# You are also given an array relations where relations[i] = [prevCourse, nextCourse],
# representing a prerequisite relationship between course prevCourse and course nextCourse:
# course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer
# k. In one semester, you can take at most k courses as long as you have taken all the prerequisites
# in the previous semesters for the courses you are taking. Return the minimum number of semesters
# needed to take all courses. The testcases will be generated such that it is possible to take every course.

class CycleException(Exception):
    pass

# Time complexity for minNumberOfSemesters:
# O(n) - initialization of indegree
# O(nˆ2) - initialization for adjacency lists (in case we have complete graph)
# Number of solve calls is given by specific structure of graph we are given.
# As a result, we are not able to give more tight bound than 2ˆn, which are all
# combinations of ones and zeroes. Within solve call, we examine all subsets/combinations
# of courses C(n, k), we can take in one semester. For each subset, we have to create
# new mask O(k) and lower indegrees for their neighbors O(n - k). All in all we
# have time complexity O(2ˆn * C(n, k) * k * (n - k)). Since k is bounded from
# above by number of courses n, we can simplify to O(2ˆn * C(n, k) * nˆ2)
def minNumberOfSemesters(n: int, relations: List[List[int]], k: int) -> int:
    # Indegree and adjacency-lists O(|V|)
    indegree = {i: 0 for i in range(1, n + 1)}
    graph = {i: [] for i in range(1, n + 1)}

    # Iterate over edges and initialize graph O(|E|)
    for start, end in relations:
        indegree[end] += 1
        graph[start].append(end)

    # 0 in mask indicates that the course has been taken
    # 1 in mask indicates that the course is still to be taken
    mask = (1 << n + 1) - 2

    subproblems = {}
    def solve(mask, indegree):
        if mask in subproblems:
            return subproblems[mask]

        # Collect courses that we can take in this semester
        courses = []
        for i in range(1, n + 1):
            if mask & 1 << i and indegree[i] == 0:
                courses.append(i)

        if not courses:
            if any(indegree.values()):
                raise CycleException
            subproblems[mask] = 0
            return 0

        semesters = sys.maxsize
        for subset in combinations(courses, min(k, len(courses))):
            # Compute new mask that has 0 for taken courses
            nmask, nindegree = mask, dict(indegree)
            for course in subset:
                nmask &= ~(1 << course)

                for node in graph[course]:
                    nindegree[node] -= 1

            semesters = min(semesters, solve(nmask, nindegree) + 1)

        subproblems[mask] = semesters
        return semesters
    
    try:
        return solve(mask, indegree)
    except CycleException:
        return -1


if __name__ == '__main__':
    relations = [[2,1],[3,1],[1,4]]
    res = minNumberOfSemesters(4, relations, k=2)
    print(res)
    assert res == 3

    relations = [[2,1],[3,1],[4,1],[1,5]]
    res = minNumberOfSemesters(5, relations, k=2)
    print(res)
    assert res == 4