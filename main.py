import time

from Maze import Maze
from BFSPathFinder import BFSPathFinder

if __name__ == '__main__':
    # maze = Maze(12, True)
    # maze.randomize()
    # maze.visualize(False)

    maze = Maze(12, False)

    start = time.time()
    paths = []
    times = []
    for i in range(100):
        start2 = time.time()
        maze.randomize()
        maze.visualize(True)
        path_finder = BFSPathFinder(maze)
        shortest_path = path_finder.find_shortest_path()
        paths.append(shortest_path)
        end2 = time.time()
        times.append(end2 - start2)

    end = time.time()
    print("\n\nELAPSED TIME: ", end - start)
    print("solvable: ", len(paths))
    print("max: ", max(paths))
    print("avg: ", sum(paths)/len(paths))
    print("max T: ", max(times))
    print("avg T: ", sum(times) / len(times))
    # if shortest_path:
    #     print("Shortest path from start to exit:")
    #     print(shortest_path)
    #     print("Steps:")
    #     print(len(shortest_path))
    # else:
    #     print("No path found to the exit.")
