
from Maze import Maze
from Astar import astar
from Solver import Solver
from Manager import Manager
import time


if __name__ == '__main__':
    start = time.time()
    manager = Manager(20000, 4, False, 2)
    manager.generateShards()
    end = time.time()
    print("ELAPSED TIME: ", end - start)
    manager.stats()

    # for mz in manager.mazes:
    #     mz.toString()
    # for temp in manager.shards:
    #     temp.toString()



    # solver = Solver()
    #
    # # i = 0
    # # while i < 2:
    # maze = Maze(4, False)
    #
    # player =      [[0, 2, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1]]
    #
    # elevation =   [[2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2]]
    #
    # doors =       [[0, 0, 0, 0, 0],
    #                [0, 1, 1, 1, 1],
    #                [1, 0, 3, 3, 3],
    #                [1, 3, 0, 2, 2],
    #                [1, 3, 2, 0, 0]]
    #
    # keys =        [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 3, 0, 0],
    #                [0, 0, 0, 2, 0]]
    #
    # maze.override(player, elevation, doors, keys, False, [False, False, False])
    # maze.toString()
    #
    # # print("\n\n\nRED KEY: " + str(maze.getKeyPos(1)))
    # # path = astar(maze, maze.startingPoint, maze.endingPoint)
    # Solver.solveMaze(solver, maze)



        # print("\n\nPATH")
        # print(path)
        # if path is not None:
        #     print("\nPATH VALUES")
        #     temp = []
        #     for pos in path:
        #         temp.append(maze.elevation[pos[0]][pos[1]])
        #     print(temp)
        #     print("\nMOVES REQUIRED")
        #     print(len(path) - 1)
        #     print("\n")
        # i += 1

    # print("\n\nSOLVER TOTAL")
    # print(solver.stats())
