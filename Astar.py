from Maze import Maze

from queue import PriorityQueue


class Node:
    def __init__(self, parent=None, position=None, path=None):
        self.parent = parent
        self.position = tuple(position)
        self.g = 0
        self.h = 0
        self.f = 0
        self.steps = 0
        self.path = []
        self.path_len = 0
        if path:
            self.path = path[::-1]
            self.path_len = len(path)
        else:
            if parent:
                self.path = parent.path[:]
            if position:
                self.path.append(self.position)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.position == other.position
        return False

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f


def astar(maze, start, end, past_path=None):
    def get_neighbors(node):
        neighbors = []
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_pos = (node.position[0] + direction[0], node.position[1] + direction[1])
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= maze.size or neighbor_pos[1] < 0 or neighbor_pos[
                1] >= maze.size:
                continue
            if abs(maze.elevation[node.position[0]][node.position[1]] - maze.elevation[neighbor_pos[0]][
                neighbor_pos[1]]) > 2:
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 1 and not can_use_doors(1, node):
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 2 and not can_use_doors(2, node):
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 3 and not can_use_doors(3, node):
                continue
            new_node = Node(node, neighbor_pos)
            neighbors.append(new_node)
        return neighbors

    def heuristic(node):
        return abs(node.position[0] - end[0]) + abs(node.position[1] - end[1])

    def can_use_doors(keyType, node):
        keys_to_use = maze.keysArr[keyType - 1]
        if len(keys_to_use) == 0:
            return False
        for key_cell in keys_to_use:
            if tuple(key_cell) not in node.path:
                return False
        return True

    start_node = Node(None, start, past_path)
    end_node = Node(None, end)

    open_list = PriorityQueue()
    open_list.put((0, start_node))
    visited = set()

    while not open_list.empty():
        current_node = open_list.get()[1]

        if current_node == end_node:
            path = current_node.path
            return path[start_node.path_len::]
            # return len(path[::-1]) - 1

        visited.add(current_node)

        for neighbor in get_neighbors(current_node):
            if neighbor in visited:
                continue
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor)
            neighbor.f = neighbor.g + neighbor.h

            for (priority, open_node) in open_list.queue:
                if open_node == neighbor and priority < neighbor.f:
                    break
            else:
                open_list.put((neighbor.f, neighbor))

    return None
