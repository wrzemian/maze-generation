from Maze import Maze
from Astar import astar
from Solver import solve_maze

from Manager import Manager

if __name__ == '__main__':
    # maze = Maze(12, True)
    # maze.randomize()
    # maze.visualize(False)

    maze = Maze(12, False)

    # maze.player =      [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]]
    # maze.startingPoint = (0, 0)
    # maze.endingPoint = (11, 11)
    #
    # maze.elevation =   [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    #
    # maze.doors =       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]]
    #
    # maze.keys =        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # maze.findKeys()
    # maze.randomize()
    # maze.visualize(True)
    # outcome = solve_maze(maze)
    # print(outcome)

    manager = Manager(2000, 12, False, 3)
    manager.experiment()
    # for gene in manager.genePool:
    #     print(gene.visualize(True))
    # maze.overrideFormGenes(12, 3, manager.genePool)
    # maze.visualize(True)



    # path = astar(maze, maze.startingPoint, maze.endingPoint)
    # if not path:
    #     print("NO ROUTE")
    # else:
    #     print("FOUND ", len(path))
    #     print(path)

    # maze.randomize()
    # maze.visualize(True)
    # path = astar(maze, maze.startingPoint, maze.endingPoint)
    # print(path)
    # path_finder = BFSPathFinder(maze)
    # shortest_path = path_finder.find_shortest_path()
    # if not shortest_path:
    #     print("NO ROUTE")
    # else:
    #     print("FOUND ", len(shortest_path))

    # start = time.time()
    # paths = []
    # times = []
    # for i in range(100):
    #     start2 = time.time()
    #     maze.randomize()
    #     maze.visualize(True)
    #     shortest_path = astar(maze, maze.startingPoint, maze.endingPoint)
    #     if not shortest_path:
    #         print("NO ROUTE")
    #     else:
    #         print("FOUND ", len(shortest_path))
    #     paths.append(shortest_path)
    #     end2 = time.time()
    #     print("TIME: ", (end2 - start2))
    #     times.append(end2 - start2)
    #
    # end = time.time()
    # print("\n\nELAPSED TIME: ", end - start)
    # print("solvable: ", len(paths))
    # print("max: ", max(paths))
    # print("avg: ", sum(paths)/len(paths))
    # print("max T: ", max(times))
    # print("avg T: ", sum(times) / len(times))


    # if shortest_path:
    #     print("Shortest path from start to exit:")
    #     print(shortest_path)
    #     print("Steps:")
    #     print(len(shortest_path))
    # else:
    #     print("No path found to the exit.")
