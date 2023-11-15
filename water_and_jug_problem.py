from math import gcd

# Water and Jug Problem (Medium)
# You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is
# an infinite amount of water supply available. Determine whether it is possible to
# measure exactly targetCapacity liters using these two jugs.
# If targetCapacity liters of water are measurable, you must have targetCapacity liters
# of water contained within one or both buckets by the end. Operations allowed:
# * Fill any of the jugs with water.
# * Empty any of the jugs.
# * Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
# Constraints:
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10ˆ6

# Time complexity: O(jug1Capacity + jug2Capacity) - we must visit number of nodes
# Space complexity: O(jug1Capacity + jug2Capacity)
def canMeasureWaterDfs(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    seen = set()
    def jugging(total):
        if total < 0 or total > jug1Capacity + jug2Capacity or total in seen:
            return False

        if total == targetCapacity:
            return True

        seen.add(total)

        for off in [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]:
            if jugging(total + off):
                return True
        
        return False

    return jugging(0)


def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    if targetCapacity == 0:
        return True

    if jug1Capacity + jug2Capacity < targetCapacity:
        return False
    
    # Bezout's identity
    # Check if target capacity is divisible by the greatest common divisor of jug capacities
    return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0


if __name__ == "__main__":
    res = canMeasureWater(3, 5, 4)
    assert res == True

    res = canMeasureWater(2, 6, 5)
    assert res == False

    res = canMeasureWater(1, 2, 3)
    assert res == True

    res = canMeasureWater(3, 4, 5)
    assert res == True

    res = canMeasureWater(3, 4, 6)
    assert res == True