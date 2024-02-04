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
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbors = []
        for direction in directions:
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
            neighbors.append(Node(node, neighbor_pos))
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
    open_set = set()  # Zestaw dla szybkiego sprawdzania obecności
    open_list.put((0, start_node))
    open_set.add(start_node)
    visited = {}  # Słownik zamiast zestawu

    while not open_list.empty():
        current_node = open_list.get()[1]
        open_set.remove(current_node)

        if current_node == end_node:
            return current_node.path[start_node.path_len::]

        visited[current_node.position] = current_node

        for neighbor in get_neighbors(current_node):
            if neighbor.position in visited:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor.position in visited and visited[neighbor.position].f <= neighbor.f:
                continue

            if neighbor in open_set:
                for (priority, open_node) in open_list.queue:
                    if open_node == neighbor and priority <= neighbor.f:
                        break
                else:
                    open_list.put((neighbor.f, neighbor))
                    visited[neighbor.position] = neighbor
            else:
                open_list.put((neighbor.f, neighbor))
                open_set.add(neighbor)
                visited[neighbor.position] = neighbor

    return None
