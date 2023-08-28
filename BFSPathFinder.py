from collections import deque


class BFSPathFinder:
    def __init__(self, maze):
        self.maze = maze

    def find_shortest_path(self):
        if not self.maze.startingPoint or not self.maze.endingPoint:
            return []

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        i = 0
        while i < 10:
            queue = deque()
            queue.append((self.maze.startingPoint[0], self.maze.startingPoint[1], []))

            while queue:
                row, col, path = queue.popleft()

                if row == self.maze.endingPoint[0] and col == self.maze.endingPoint[1]:
                    return path

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    new_path = path + [(row, col)]
                    if self.isValid(new_row, new_col, row, col, new_path, i):
                        queue.append((new_row, new_col, new_path))
            i = i + 1
        return []

    def isValid(self, new_row, new_col, row, col, path, i):
        if not (0 <= new_row < self.maze.size and 0 <= new_col < self.maze.size):
            return False
        if not (abs(self.maze.elevation[new_row][new_col] - self.maze.elevation[row][col]) <= 2):
            return False
        if path.count((new_row, new_col)) >= i:
            return False
        if not (self.maze.doors[new_row][new_col] == 0):
            if self.maze.doors[new_row][new_col] == 1:
                if not self.can_use_doors(1, path):
                    return False
            if self.maze.doors[new_row][new_col] == 2:
                if not self.can_use_doors(2, path):
                    return False
            if self.maze.doors[new_row][new_col] == 3:
                if not self.can_use_doors(3, path):
                    return False
        return True

    def can_use_doors(self, keyType, visitedSpots):
        keys_to_use = self.maze.keysArr[keyType - 1]
        if len(keys_to_use) == 0:
            return False
        for key_cell in keys_to_use:
            if tuple(key_cell) not in visitedSpots:
                return False
        return True
