from Maze import Maze


from queue import PriorityQueue

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = tuple(position)
        self.g = 0
        self.h = 0
        self.f = 0
        self.steps = 0

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f


def astar(maze, start, end):
    def get_neighbors(node):
        neighbors = []
        for direction in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor_pos = (node.position[0] + direction[0], node.position[1] + direction[1])
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= maze.size or neighbor_pos[1] < 0 or neighbor_pos[1] >= maze.size:
                continue
            if abs(maze.elevation[node.position[0]][node.position[1]] - maze.elevation[neighbor_pos[0]][neighbor_pos[1]]) > 2:
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 1 and not maze.doorsStatus[0]:
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 2 and not maze.doorsStatus[1]:
                continue
            if maze.hasDoors and maze.doors[node.position[0]][node.position[1]] == 3 and not maze.doorsStatus[2]:
                continue
            new_node = Node(node, neighbor_pos)
            neighbors.append(new_node)
        return neighbors

    def heuristic(node):
        return abs(node.position[0] - end[0]) + abs(node.position[1] - end[1])

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = PriorityQueue()
    open_list.put((0, start_node))
    visited = set()

    while not open_list.empty():
        current_node = open_list.get()[1]

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
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
