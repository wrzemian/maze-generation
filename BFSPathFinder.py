from collections import deque

class BFSPathFinder:
    def __init__(self, maze):
        self.maze = maze

    def find_shortest_path(self):
        if not self.maze.startingPoint or not self.maze.endingPoint:
            return []  # Return an empty list if starting or ending point is not set.

        # Define the movement directions (up, down, left, right).
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Create a queue for BFS traversal.
        queue = deque()
        queue.append((self.maze.startingPoint[0], self.maze.startingPoint[1], []))
        # Create a set to store visited cells.
        visited = set()
        visited.add((self.maze.startingPoint[0], self.maze.startingPoint[1]))

        while queue:
            # print(len(queue))
            row, col, path = queue.popleft()

            if row == self.maze.endingPoint[0] and col == self.maze.endingPoint[1]:
                return path

            # Explore adjacent cells.
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if self.isValid(new_row, new_col, visited, row, col, path):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path + [(row, col)]))
                    # print(path + [(row, col)])

        return []  # Return an empty list if no valid path is found.

    def isValid(self, new_row, new_col, visited, row, col, path):
        i = 0
        while i < 3:
            if not (0 <= new_row < self.maze.size and 0 <= new_col < self.maze.size):
                return False
            if not (abs(self.maze.elevation[new_row][new_col] - self.maze.elevation[row][col]) <= 2):
                return False
            # if not (path.count((new_row, new_col)) <= i):
            #     continue
            # print("TRYING FOR i:", i)
            if path.count((new_row, new_col)) >= i:
                i = i + 1
                continue
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
        # print("AAAAAAA: ", keys_to_use)
        # print("VISITED: ", visitedSpots)
        if len(keys_to_use) == 0:
            return False
        for key_cell in keys_to_use:
            if tuple(key_cell) not in visitedSpots:
                return False
        return True