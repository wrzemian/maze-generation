from Maze import Maze
from Astar import astar
from Solver import Solver


if __name__ == '__main__':
    solver = Solver()

    # i = 0
    # while i < 2:
    maze = Maze(4, True)

    player =      [[2, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 1, 0, 0]]

    elevation =   [[2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2]]

    doors =       [[0, 0, 0, 0],
                   [2, 2, 2, 2],
                   [1, 1, 1, 0],
                   [0, 0, 1, 0]]

    keys =       [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 2],
                  [1, 0, 0, 0]]

    maze.override(player, elevation, doors, keys, True, [True, True, False])
    maze.toString()

    # path = astar(maze, maze.startingPoint, maze.endingPoint)
    Solver.solveMaze(solver, maze)

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




