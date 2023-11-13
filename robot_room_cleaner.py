
# Robot Room Cleaner (Hard)
# You are controlling a robot that is located somewhere in a room. The room is
# modeled as an m x n binary grid where 0 represents a wall and 1 represents an
# empty slot.
# The robot starts at an unknown location in the room that is guaranteed to be
# empty, and you do not have access to the grid, but you can move the robot using
# the given API Robot.
# You are tasked to use the robot to clean the entire room (i.e., clean every empty
# cell in the room). The robot with the four given APIs can move forward, turn left,
# or turn right. Each turn is 90 degrees.
# When the robot tries to move into a wall cell, its bumper sensor detects the
# obstacle, and it stays on the current cell.
# Design an algorithm to clean the entire room using the following APIs:
# interface Robot {
#  // returns true if next cell is open and robot moves into the cell.
#  // returns false if next cell is obstacle and robot stays on the current cell.
#  boolean move();
#
#  // Robot will stay on the same cell after calling turnLeft/turnRight.
#  // Each turn will be 90 degrees.
#  void turnLeft();
#  void turnRight();
#
#  // Clean the current cell.
#  void clean();
#}
# Note that the initial direction of the robot will be facing up. You can assume
# all four edges of the grid are all surrounded by a wall.
# Constraints:
# m == room.length
# n == room[i].length
# 1 <= m <= 100
# 1 <= n <= 200
# room[i][j] is either 0 or 1.
# 0 <= row < m
# 0 <= col < n
# room[row][col] == 1
# All the empty cells can be visited from the starting position.
from typing import List, Tuple

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Robot:
    def __init__(self, room: List[List[int]], pos: Tuple[int, int], dir=None):
        self.room = room
        self.pos = pos
        self.dir = dir or 0
    
    def move(self) -> bool:
        nx, ny = (
            self.pos[0] + DIRECTIONS[self.dir][0],
            self.pos[1] + DIRECTIONS[self.dir][1],
        )
        try:
            if self.room[nx][ny]:
                self.pos = (nx, ny)
                return True
        except IndexError:
            pass

        return False

    def turnLeft(self):
        self.dir = (self.dir - 1) % 4

    def turnRight(self):
        self.dir = (self.dir + 1) % 4
    
    def clean(self):
        x, y = self.pos
        self.room[x][y] = 2


# Time complexity: O(n - m) where n is number of cells and m number of obstacles.
# Over all recursive calls we visit each cell exactly once and do constant amount
# of work. Specifically, we check if we can make a move in 4 directions
# Space complexity: O(n - m) - storing visited cells in hashset
def cleanRoom(robot):
    def go_back(robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    visited = set()
    def backtrack(robot, pos, dir):
        visited.add(pos)
        robot.clean()

        for i in range(4):
            next_dir = (dir + i) % 4
            next_pos = (
                pos[0] + DIRECTIONS[next_dir][0],
                pos[1] + DIRECTIONS[next_dir][1],
            )
            if next_pos not in visited and robot.move():
                backtrack(robot, next_pos, next_dir)
                go_back(robot)
            robot.turnRight()

    backtrack(robot, (0, 0), 0)


if __name__ == "__main__":
    room = [
        [1,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,0],
    ]
    robot = Robot(room, (1, 1))
    cleanRoom(robot)
    for i in range(len(room)):
        for j in range(len(room[0])):
            assert room[i][j] in [0, 2]

    room = [
        [1,1,1,1,1,0,1,1],
        [1,1,1,1,1,0,1,1],
        [1,0,1,1,1,1,1,1],
        [0,0,0,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
    ]
    robot = Robot(room, (1, 3))
    cleanRoom(robot)
    for i in range(len(room)):
        for j in range(len(room[0])):
            assert room[i][j] in [0, 2]