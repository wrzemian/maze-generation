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
        debug = False
        # print(path)
        if debug:
            # print("\n")
            print(path)
        # print(new_row, new_col)
        if not(0 <= new_row < self.maze.size and 0 <= new_col < self.maze.size):
            if debug:
                print("OUTSIDE MAZE")
            return False
        if not(abs(self.maze.elevation[new_row][new_col] - self.maze.elevation[row][col]) <= 2):
            if debug:
                print("SIZE DIFF")
            return False
        # if not((new_row, new_col) not in path):
        #     if debug:
        #         print("ALREADY VISITED")
        #     return False
        if not(self.maze.doors[new_row][new_col] == 0):
            if debug:
                print("HITTING DOOR")
        if self.maze.doors[new_row][new_col] == 1: # and (new_row, new_col) not in visited:
            if debug:
                print("CHECKING FOR RED KEY")
            if not self.can_use_doors(1, path):
                if debug:
                    print("NO RED KEY")
                return False
        if self.maze.doors[new_row][new_col] == 2: # and (new_row, new_col) not in visited:
            if debug:
                print("CHECKING FOR GREEN KEY")
            if not self.can_use_doors(2, path):
                if debug:
                    print("NO GREEN KEY")
                return False
        if self.maze.doors[new_row][new_col] == 3: # and (new_row, new_col) not in visited:
            if debug:
                print("CHECKING FOR RED KEY")
            if not self.can_use_doors(3, path):
                if debug:
                    print("NO RED KEY")
                return False
            if debug:
                print("RED KEY ACHIEVED")
            # return False

        # print("IS VALIDDDDDDDDDDDDDDDDDDDDDDDDD")
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