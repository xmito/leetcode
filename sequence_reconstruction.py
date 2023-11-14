from typing import List, Dict
from collections import deque
from itertools import permutations, chain, product

# Sequence Reconstruction (Medium)
# You are given an integer array nums of length n where nums is a permutation of the
# integers in the range [1, n]. You are also given a 2D integer array sequences where
# sequences[i] is a subsequence of nums.
# Check if nums is the shortest possible and the only supersequence. The shortest
# supersequence is a sequence with the shortest length and has all sequences[i] as
# subsequences. There could be multiple valid supersequences for the given array
# sequences.
# * For example, for sequences = [[1,2],[1,3]], there are two shortest supersequences,
# [1,2,3] and [1,3,2]
# * While for sequences = [[1,2],[1,3],[1,2,3]], the only shortest supersequence
# possible is [1,2,3]. [1,2,3,4] is a possible supersequence but not the shortest.
# Return true if nums is the only shortest supersequence for sequences, or false otherwise.
# A subsequence is a sequence that can be derived from another sequence by deleting
# some or no elements without changing the order of the remaining elements.
# Constraints:
# n == nums.length
# 1 <= n <= 104
# nums is a permutation of all the integers in the range [1, n].
# 1 <= sequences.length <= 104
# 1 <= sequences[i].length <= 104
# 1 <= sum(sequences[i].length) <= 105
# 1 <= sequences[i][j] <= n
# All the arrays of sequences are unique. sequences[i] is a subsequence of nums.

# Time complexity: O(V + E) - bfs search 
# Space complexity: O(V + E) - indegree + graph adjacency lists
def sequenceReconstruction(nums: List[int], sequences: List[List[int]]) -> bool:
    if len(sequences) == 1 and nums != sequences[0]:
        return False

    values = {x for seq in sequences for x in seq}
    graph = {i: [] for i in values}
    for seq in sequences:
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i + 1])

    indegree = {}
    for seq in sequences:
        indegree.setdefault(seq[0], 0)
        for i in range(1, len(seq)):
            indegree.setdefault(seq[i], 0)
            indegree[seq[i]] += 1

    queue = deque()
    for node, degree in indegree.items():
        if degree == 0:
            queue.append(node)
        
    result = []
    while queue:
        # If there is more than one node, what means there are
        # more than one topological orderings
        if len(queue) > 1:
            return False
    
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result == nums
    

if __name__ == "__main__":
    res = sequenceReconstruction([4,5,7,8,6,3,2,10,9,1], [[4,5,7,8,6,3,2,10,9,1]])
    assert res == True

    res = sequenceReconstruction([1,2,3], [[1,2], [1,3]])
    assert res == False
    # Explanation: There are two possible supersequences: [1,2,3] and [1,3,2].
    # The sequence [1,2] is a subsequence of both: [1,2,3] and [1,3,2].
    # The sequence [1,3] is a subsequence of both: [1,2,3] and [1,3,2].
    # Since nums is not the only shortest supersequence, we return false.

    res = sequenceReconstruction([1,2,3], [[1,2]])
    assert res == False
    # Explanation: The shortest possible supersequence is [1,2].
    # The sequence [1,2] is a subsequence of it: [1,2].
    # Since nums is not the shortest supersequence, we return false.

    res = sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]])
    assert res == True
    # Explanation: The shortest possible supersequence is [1,2,3].
    # The sequence [1,2] is a subsequence of it: [1,2,3].
    # The sequence [1,3] is a subsequence of it: [1,2,3].
    # The sequence [2,3] is a subsequence of it: [1,2,3].
    # Since nums is the only shortest supersequence, we return true.
