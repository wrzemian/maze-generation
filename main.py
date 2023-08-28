import time

from Maze import Maze
from BFSPathFinder import BFSPathFinder

if __name__ == '__main__':
    # maze = Maze(12, True)
    # maze.randomize()
    # maze.visualize(False)

    maze = Maze(5, True)
    maze.player = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2]
    ]
    maze.elevation = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    maze.startingPoint = (0, 0)
    maze.endingPoint = (4, 4)
    maze.doors = [
        [0, 0, 0, 0, 0],
        [3, 0, 2, 2, 2],
        [0, 2, 0, 0, 0],
        [0, 2, 0, 1, 1],
        [0, 2, 0, 1, 0]
    ]
    maze.keys = [
        [0, 0, 0, 0, 2],
        [0, 2, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]
    maze.findKeys()
    maze.visualize(True)

    path_finder = BFSPathFinder(maze)
    start = time.time()
    # for i in range(100):
    shortest_path = path_finder.find_shortest_path()
    end = time.time()
    print("\n\nELAPSED TIME: ", end - start)
    if shortest_path:
        print("Shortest path from start to exit:")
        print(shortest_path)
        print(len(shortest_path))
    else:
        print("No path found to the exit.")
