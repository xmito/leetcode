
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

RIGHT = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}
LEFT = {
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
}

class Robot:
    def __init__(self, room: List[List[int]], pos: Tuple[int, int], dir=None):
        self.room = room
        self.pos = pos
        self.dir = dir or (-1, 0)
    
    def move(self) -> bool:
        x, y = self.pos
        dirx, diry = self.dir
        nx, ny = x + dirx, y + diry
        if nx < 0 or nx >= len(room):
            return False
        if ny < 0 or ny >= len(room[0]):
            return False
        if self.room[nx][ny]:
            self.pos = (nx, ny)
            return True

        return False

    def turnLeft(self):
        self.dir = LEFT[self.dir]

    def turnRight(self):
        self.dir = RIGHT[self.dir]
    
    def clean(self):
        x, y = self.pos
        self.room[x][y] = 2


def cleanRoom(robot):
    room = {}

    def steer(robot, pos, dir):
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if next_pos not in room:
            return next_pos, dir

        left = LEFT[dir]
        next_pos = (pos[0] + left[0], pos[1] + left[1])
        if next_pos not in room:
            robot.turnLeft()
            return next_pos, left

        right = RIGHT[dir]
        next_pos = (pos[0] + right[0], pos[1] + right[1])
        if next_pos not in room:
            robot.turnRight()
            return next_pos, right

        rev = RIGHT[right]
        next_pos = (pos[0] + rev[0], pos[1] + rev[1])
        if next_pos not in room:
            robot.turnRight()
            robot.turnRight()
            return next_pos, rev

        return None, dir

    def dfs_visit(robot, pos, dir):
        room[pos] = "PROCESS"
        initial_dir = dir
        next_pos, dir = steer(robot, pos, dir)
        while next_pos and next_pos not in room:
            success = robot.move()
            if not success:
                room[next_pos] = "WALL"
                next_pos, dir = steer(robot, pos, dir)
                continue
            
            dir = dfs_visit(robot, next_pos, dir)
            next_pos, dir = steer(robot, pos, dir)
        
        # Make move back 
        robot.clean()
        room[pos] = "CLEANED"

        reverse_dir = (initial_dir[0] * -1, initial_dir[1] * -1)
        while dir != reverse_dir:
            dir = RIGHT[dir]
            robot.turnRight()
        robot.move()
        return reverse_dir

    dfs_visit(robot, (0, 0), (-1, 0))


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